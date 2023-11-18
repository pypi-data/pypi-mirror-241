import os
import pandas as pd
import pytest
import shutil

from pyexifwrangle import wrangle


@pytest.fixture(scope='session')
def filename_col():
    return 'SourceFile'


@pytest.fixture(scope='session')
def df(filename_col):
    return wrangle.read_exif(path='tests/fixtures/exif_s21.csv', filename_col=filename_col)


@pytest.fixture(scope="session")
def temp_dir(tmp_path_factory):
    """Make a temporary directory"""
    return tmp_path_factory.mktemp("temp_dir")


@pytest.fixture(scope="session")
def temp_dir2(tmp_path_factory):
    """Make a temporary directory"""
    return tmp_path_factory.mktemp("temp_dir2")


def test_filename2columns(df, filename_col):
    """Check that filename2columns() adds the correct columns."""
    actual = wrangle.filename2columns(df=df, filename_col=filename_col, columns=['model', 'phone', 'scene_type',
                                                                                 'camera', 'image'])
    expected = pd.read_csv('tests/fixtures/exif_s21_columns.csv')
    pd.testing.assert_frame_equal(actual, expected, check_dtype=False)


def test_check_missing_exif(df):
    actual = wrangle.check_missing_exif(df=df, column='Aperture').reset_index(drop=True)
    # change dtype from object to int64 or float64 so test passes
    actual['ImageHeight'] = actual['ImageHeight'].astype('int64')
    actual['ImageWidth'] = actual['ImageWidth'].astype('int64')
    actual['MaxApertureValue'] = actual['MaxApertureValue'].astype('float64')
    actual['Megapixels'] = actual['Megapixels'].astype('float64')
    actual['ScaleFactor35efl'] = actual['ScaleFactor35efl'].astype('float64')
    actual['SubSecTimeDigitized'] = actual['SubSecTimeDigitized'].astype('float64')
    actual['ThumbnailLength'] = actual['ThumbnailLength'].astype('float64')
    actual['ThumbnailOffset'] = actual['ThumbnailOffset'].astype('float64')
    actual['XResolution'] = actual['XResolution'].astype('float64')
    # load expected
    expected = pd.read_csv('tests/fixtures/missing.csv')
    pd.testing.assert_frame_equal(actual, expected, check_dtype=False)


def test_count_images_by_columns(df):
    actual = wrangle.count_images_by_columns(df=df, columns=['model', 'phone', 'scene_type', 'camera'])
    expected = pd.read_csv('tests/fixtures/counts.csv')
    pd.testing.assert_frame_equal(actual, expected)


def test_count_images_by_columns_sorted(df):
    actual = wrangle.count_images_by_columns(df=df, columns=['model', 'phone', 'scene_type', 'camera', 'Aperture'],
                                             sort=['model', 'camera', 'phone', 'scene_type'])
    expected = pd.read_csv('tests/fixtures/aperture_sorted.csv')
    pd.testing.assert_frame_equal(actual, expected)


def test_find_images_all_columns(df):
    actual = wrangle.find_images(df=df, filter_dict={'phone': 's21_1', 'Aperture': 2.2})
    # change dtype from object to float64 so test passes
    actual['GPSLatitude'] = actual['GPSLatitude'].astype('float64')
    actual['GPSLongitude'] = actual['GPSLongitude'].astype('float64')
    actual['GPSPosition'] = actual['GPSPosition'].astype('float64')
    actual['GPSProcessingMethod'] = actual['GPSProcessingMethod'].astype('float64')
    expected = pd.read_csv('tests/fixtures/found_images_all_columns.csv')
    pd.testing.assert_frame_equal(actual, expected)


def test_find_images_selected_columns(df):
    actual = wrangle.find_images(df=df, filter_dict={'phone': 's21_1', 'Aperture': 2.2},
                                 return_columns=['model', 'phone', 'scene_type', 'camera', 'image'])
    expected = pd.read_csv('tests/fixtures/found_images.csv')
    pd.testing.assert_frame_equal(actual, expected)


def test_get_exif(temp_dir):
    actual = wrangle.get_exif(input_dir='tests/fixtures/images', output_csv=os.path.join(temp_dir, 'output.csv'))
    # FileAccessDate will change each time get_exif() runs
    actual.drop(columns=['FileAccessDate'], inplace=True)
    expected = pd.read_csv('tests/fixtures/get_exif.csv')
    expected.drop(columns=['FileAccessDate'], inplace=True)
    pd.testing.assert_frame_equal(actual, expected)

def test_wipe_gps(temp_dir2):
    # copy image with gps data to temp dir
    shutil.copy2(os.path.join('tests', 'fixtures', 'images', 'gps_example.JPG'), os.path.join(temp_dir2, 'gps_example.JPG'))
    # check copied image has GPS tags
    df = wrangle.get_exif(input_dir=str(temp_dir2), output_csv=os.path.join(temp_dir2, 'gps.csv'))
    gps_tags = [f for f in df.columns if f.startswith('GPS')]
    assert gps_tags

    # wipe gps
    wrangle.wipe_gps(os.path.join(temp_dir2, 'gps_example.JPG'))
    # check copied image has GPS tags
    df = wrangle.get_exif(input_dir=str(temp_dir2), output_csv=os.path.join(temp_dir2, 'gps.csv'))
    gps_tags = [f for f in df.columns if f.startswith('GPS')]
    assert not gps_tags

def test_wipe_gps_file_w_parentheses(temp_dir2):
    # copy image with gps data to temp dir
    shutil.copy2(os.path.join('tests', 'fixtures', 'images', 'gps_example.JPG'), os.path.join(temp_dir2, 'gps_example (0).JPG'))
    # check copied image has GPS tags
    df = wrangle.get_exif(input_dir=str(temp_dir2), output_csv=os.path.join(temp_dir2, 'gps.csv'))
    gps_tags = [f for f in df.columns if f.startswith('GPS')]
    assert gps_tags

    # wipe gps
    wrangle.wipe_gps(os.path.join(temp_dir2, 'gps_example (0).JPG'))
    # check copied image has GPS tags
    df = wrangle.get_exif(input_dir=str(temp_dir2), output_csv=os.path.join(temp_dir2, 'gps.csv'))
    gps_tags = [f for f in df.columns if f.startswith('GPS')]
    assert not gps_tags
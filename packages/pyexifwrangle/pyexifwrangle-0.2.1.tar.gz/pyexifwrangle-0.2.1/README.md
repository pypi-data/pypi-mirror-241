# Wrangle EXIF Data in Python

A Python package for wrangling EXIF data extracted from images using Phil Harvey's EXIFTool.

## Set-up
### Install pyexifwrangle with pip

```bash
$ pip install pyexifwrangle
```

### Install Phil Harvey's EXIFTool
Install Phil Harvey's EXIFTool from https://exiftool.org/. This site has installation instructions if you need them.

## Usage
### Get EXIF data
After installing EXIFTool, you can extract EXIF data from every image in a folder, including subdirectories, save the 
results in a csv file, and return the results in a Pandas DataFrame.

```python
import pyexifwrangle.wrangle as wr

df = wr.get_exif(input_dir='path/to/images', output_csv='path/to/output.csv')
```

### Load the EXIF data
If you already used get_exif() to save the EXIF to a csv file, you can use read_exif() to
load the csv file into a Pandas data frame. In this case, the output of get_exif() is the same as the output
from read_exif().

```python
import pyexifwrangle.wrangle as wr

df = wr.read_exif('path/to/output.csv', filename_col='SourceFile')
```
The function *wrangle.read_exif* uses the Pandas package to load the csv into a data frame. The parameter 
*filename_col* is the name of the column that contains the filenames of the images.  The absolute file paths are 
included with the filenames in the *filename_col*. After reading the EXIF data into a Pandas data frame, this function removes any images whose filename starts with '.'. 

### Make columns from folder names
I often organize my images into folders and sub-folders. For example one of my projects has the following folder tree:
```
├── Samsung_phones  # main directory
│   ├── s21  # model
│   │   ├── s21_1  # phone name
│   │   │ 	├── blank  # scene type
│   │   │	│	├── front  # camera
│   │   │	│	│	├──image1.jpg
│   │   │	│	│	├──image2.jpg
│   │   │	│	│	├──...
│   │   │	│	├── telephoto
│   │   │	│	│	├──image1.jpg
│   │   │	│	│	├──image2.jpg
│   │   │	│	│	├──...
│   │   │	│	├── ultra
│   │   │	│	│	├──image1.jpg
│   │   │	│	│	├──image2.jpg
│   │   │	│	│	├──...
│   │   │	│	├── wide
│   │   │	│	│	├──image1.jpg
│   │   │	│	│	├──image2.jpg
│   │   │	│	│	├──...
│   │   │ 	├── natural
│   │   │	│	├── front  
│   │   │	│	├── telephoto
│   │   │	│	├── ultra
│   │   │	│	├── wide
│   │   ├── s21_2 
│   │   │ 	├── blank
│   │   │	│	├── front
│   │   │	│	├── telephoto
│   │   │	│	├── ultra
│   │   │	│	├── wide
│   │   │ 	├── natural
│   │   │	│	├── front  
│   │   │	│	├── telephoto
│   │   │	│	├── ultra
│   │   │	│	├── wide
```
Extract the folder names from the images' absolute filepaths and make a new column for each folder.
```python
df = wr.filename2columns(df=df, filename_col='SourceFile', columns=['model', 'phone', 'scene_type', 'camera', 'image'])
```

### Search for missing EXIF data
Find images missing EXIF data. For example, search the data frame for images that don't have an Aperture.
```python
missing = wr.check_missing_exif(df=df, column='Aperture')
```

### Count images per group(s)
Group images by column(s) and count the number of images per group.
```python
counts = wr.count_images_by_columns(df=df, columns=['model', 'phone', 'scene_type', 'camera'])
```

Optionally, you can sort the output of *count_images_by_columns*
```python
counts_sorted = wr.count_images_by_columns(df=df, columns=['model', 'phone', 'scene_type', 'camera'], sorted=
['phone', 'camera', 'Aperture'])
```

## Table of contents
* [General Information](#general-information)
* [Step of using](#step-of-using)
* [Installation](#installation)
* [Room for Improvement](#room-for-improvementlimitation)
* [remark](#remark)


# General Information
Instagram allow users to upload multiple media at once for each post, however, the photos are automatically cropped if the aspect ratio of them are not consistent. To advoid cropping on Instagram, users have to make sure that all the media that they upload are in the union aspect ratio, or they may resize the photo by using some thrid-party app which take some times to do it.
The main purpose of this project is to facilitate the resizing and uploading process. After login, user can choose the photos/video that they need to upload for the same post, this application will automatically resize the photos and video and post them without any cropping.

# Step of Using
1. Execute main.py
```
python main.py
```
2. Login your Instagram account
3. Input your post detail (include caption, hastag and media)
4. Preview the media (before transformation) after photos/video selected
5. Press "Submit" for resizing the media and posting


# Installation
```
pip install -r requirements.txt
```
 

# Room for Improvement/Limitation
- not able to handle some raw photo, e.g. heic format
- no preview function for general post detail
- preview function for media is not available for .cr2 format (but able to be processed)
- simple layout design


# Remark
- default ratio of the photo are 4:3 / 3:4 (depends on the proportion of number for each orientation)

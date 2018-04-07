# Kobee Raveendran
# YouTube to mp3 download script

import pytube
from pytube import YouTube
import os
import subprocess

# get video link from user
link = input("Enter video URL: ")

# create a pytube object out of that link
yt = YouTube(link)
print("Video title: " + yt.title)

# get the specific stream with audio only (mp4)
video = yt.streams.get_by_itag(140)
print("get stream successful")

# my default directory for downloads
# (change this to whatever path suits your needs, i.e. "C:/Downloads")
default_directory = "D:/Downloads"
video.download(default_directory)

print("video download successful")

# get default filename
#default_filename = stream[videonum].default_filename
default_filename = video.default_filename
mp3_filename = yt.title.replace(" ", "_") + ".mp3"

subprocess.call(['ffmpeg', '-i', os.path.join(default_directory, default_filename), os.path.join(default_directory, mp3_filename)])

print("\n\nVideo conversion complete. For source code or issues, visit github.com/kobeeraveendran")
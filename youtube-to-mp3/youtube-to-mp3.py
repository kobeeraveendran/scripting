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

# create default directory to store downloaded files in
# (change this to whatever path suits your needs, i.e. "C:/Users/[name]/Downloads")
default_directory = "D:/YouTubeDownloads"

if not os.path.exists(default_directory):
    os.makedirs(default_directory)

video.download(default_directory)

# get default filename
default_filename = video.default_filename
mp3_filename = yt.title.replace(" ", "_") + ".mp3"

subprocess.call(['ffmpeg', '-i', os.path.join(default_directory, default_filename), os.path.join(default_directory, mp3_filename)], shell = True)

# deletes mp4 file after conversion
os.remove(os.path.join(default_directory, default_filename))

# source code/bug reports
print("\n\nVideo conversion complete. For source code or issues, visit github.com/kobeeraveendran")
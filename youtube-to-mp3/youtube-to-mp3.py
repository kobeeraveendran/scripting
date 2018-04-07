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

# get all stream formats for the video and display them
stream = yt.streams.all()

i = 1
for videos in stream:
    print(str(i) + ") " + str(videos))
    i += 1

# request stream format from user
videonum = int(input("Enter video stream number: "))

# my default directory for downloads
# (change this to whatever path suits your needs)
default_directory = "D:/Downloads"
stream[videonum].download(default_directory)

# get default filename
default_filename = stream[videonum].default_filename
mp3_filename = yt.title.strip() + ".mp3"

subprocess.run(['ffmpeg', '-i', os.path.join(default_directory, default_filename), os.path.join(default_directory, mp3_filename)])

print("Video conversion complete. For source code or issues, visit github.com/kobeeraveendran")

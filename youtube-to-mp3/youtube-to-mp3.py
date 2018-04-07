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
#videos = yt.streams.get_by_itag("140")
video = yt.streams.get_by_itag(140)
print("get stream successful")
#i = 1
#for videos in videos:
#    print(str(i) + ") " + str(videos))
#    i += 1

# request stream format from user
#videonum = int(input("Enter video stream number: "))

# my default directory for downloads
# (change this to whatever path suits your needs, i.e. "C:/Downloads")
default_directory = "D:/Downloads"
video.download(default_directory)

print("video download successful")
#stream[videonum].download(default_directory)

# get default filename
#default_filename = stream[videonum].default_filename
default_filename = video.default_filename
mp3_filename = yt.title.replace(" ", "_") + ".mp3"

subprocess.call(['ffmpeg', '-i', os.path.join(default_directory, default_filename), os.path.join(default_directory, mp3_filename)])

print("Video conversion complete. For source code or issues, visit github.com/kobeeraveendran")
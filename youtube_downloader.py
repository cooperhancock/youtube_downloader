# importing the module 
from pytube import YouTube 
import os

# where to save - default downloads folder
SAVE_PATH = os.path.expanduser("~")+"\Downloads\\" 

# check save path
print(SAVE_PATH)
check = input("Use save path? y or enter new path: ")
if(check != 'y'):
    SAVE_PATH = check

# link of the video to be downloaded 
link=input("Enter video link: ")

try: 
	# object creation using YouTube 
	# which was imported in the beginning 
	yt = YouTube(link) 
except: 
	print("Connection Error") #to handle exception 
stream = yt.streams.filter(progressive=True).last()
print(stream)
stream.download(SAVE_PATH)

 


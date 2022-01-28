# لا اله لا الله محمدا رسول الله
import os
from unicodedata import name
from pytube import YouTube
def finshed():
    print("Allah Akbar \n--------Download Complet.---------")
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path

link = input("Please Enter URL of Video : ")
print("Entering to URL ...")
Vname = input("Enter Name for vedio : \n")
passs = input("Enter Pass of folder to dwonload video in: \n")
video = YouTube(link)
print(f"the video length : {video.length / 60} min.")
x = input("Enter num\n1)for highst_resolution\n2)for lowest_resolution\n")

if(x == '1'):
    Vtype = video.streams.get_highest_resolution()
    x = "highst_resolution"
else:
    Vtype = video.streams.get_lowest_resolution()
    x = "lowest_resolution"

Vtype.download(output_path=passs,filename = Vname)

print(f"Video Downl loading on D Drive: as {x}\n...\
Downloading ...")
video.register_on_complete_callback(finshed())
    

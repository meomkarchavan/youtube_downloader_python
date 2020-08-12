# pip install pytube3
#This will install the pytube3 which will be required.

from pytube import YouTube

def humanbytes(B):
   'Return the given bytes as a human friendly KB, MB, GB, or TB string'
   B = float(B)
   KB = float(1024)
   MB = float(KB ** 2) # 1,048,576
   GB = float(KB ** 3) # 1,073,741,824
   TB = float(KB ** 4) # 1,099,511,627,776

   if B < KB:
      return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
   elif KB <= B < MB:
      return '{0:.2f} KB'.format(B/KB)
   elif MB <= B < GB:
      return '{0:.2f} MB'.format(B/MB)
   elif GB <= B < TB:
      return '{0:.2f} GB'.format(B/GB)
   elif TB <= B:
      return '{0:.2f} TB'.format(B/TB)


import time

links=[]
# Asking for all the video links
if(input('Do you want to dowanlod multiple videos?(y/n): ').lower()==('y')):
    if(input('Do you want to send links via a txt file?(y/n)').lower()=='y'):
        path=input('Give the path of txt file with video links on each line: ')
        links=open(path, "r").read().splitlines()
    else:
        n = int(input("Enter the number of youtube videos to download:   "))
        print("\nEnter all the links one per line:")
        for i in range(0,n):
            temp = input()
            links.append(temp)
else:
    print("\nEnter the link of Video:")
    links.append(input())
    
SAVE_PATH=input('Enter Destination Path("." for this dir):')

links=['https://youtu.be/qbW6FRbaSl0']

#Showing all details for videos and downloading them one by one
def progress(*args):
    N=100
    for i in range(N):
        time.sleep(0.5)
        print(f"{i/N*100:.1f} %", end="\r")

import os
for i in range(0,len(links)):
    link = links[i]
    print("\nGetting Details of Video",end="\r")
    yt = YouTube(link)
    os.system('cls')
    print("\nDetails for Video","\n")
    print("Title:   ",yt.title)
    print("Length of video:  ",yt.length,"seconds")
    stream_ = yt.streams.filter(progressive=True)
    stream=str(stream_)
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll available options for downloads:\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1,") ",st[1]," ",st[3],' size=',humanbytes(stream_[i].filesize),sep='')
    tag = int(input("\nEnter the itag of your preferred stream to download:   "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading...")
    ys.download(SAVE_PATH)
    print("\nDownload completed!!")

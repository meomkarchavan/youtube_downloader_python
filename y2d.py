# pip install pytube3
#This will install the pytube3 which will be required.
from helper import humanbytes,fileExists,urlChecker,pathExistsElseCreate,connect
from pytube import YouTube
import time
import os

# Asking for all the video links
def main():
    if not connect():
        print('No Internet Connection!\nExiting....')
        exit()
    else:
        
        while True:
            multiple=input('\nDo you want to dowanlod multiple videos?(y/n): ').lower()
            if(multiple==('y')):
                while True:
                    via_txt=input('\nDo you want to send links via a txt file?(y/n)').lower()
                    if(via_txt=='y'):
                        while True:
                            path=input('\nEnter the path of txt file with video links on each line: ')
                            if(fileExists):
                                links=[]
                                links=open(path, "r").read().splitlines()
                                break
                            else:
                                print('File Not Found!, Please Check the file path')
                    elif(via_txt=='n'):
                        while True:
                            try:
                                n = int(input("Enter the number of youtube videos to download:   "))
                                print("\nEnter all the links one per line:")
                                links=[]
                                for i in range(0,n):
                                    while True:
                                        url=input()
                                        if(urlChecker(url)):
                                            links.append(url)
                                            break
                                        else:
                                            print('Invalid Input!')
                            except ValueError:
                                print('Invalid Input!')
                    else:
                        print('Invalid Input!')
            elif(multiple=='n'):
                while True:
                    print("\nEnter the link of Video:")
                    url=input()
                    links=[]
                    if(urlChecker(url)):
                        links.append(url)
                        break
                    else:print('Invalid Input!')
                break
            else:
                print('Invalid Input!')
        while True:
            temp=pathExistsElseCreate(input('\nEnter Destination Path("." for this dir):'))
            if temp is not None:
                SAVE_PATH=temp
                break
            else:print('Invalid Path!')

        #Showing all details for videos and downloading them one by one
        for i in range(0,len(links)):
            link = links[i]
            print("\nGetting Details of Video")
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

if __name__ == '__main__':
    main()
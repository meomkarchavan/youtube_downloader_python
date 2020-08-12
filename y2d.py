from helper import humanbytes,fileExists,urlChecker,pathExistsElseCreate,connect
from pytube import YouTube
import os

# Asking for all the video links
def main():
    # check is user is conncted to internet
    if not connect():
        print('No Internet Connection!\nExiting....')
        exit() #exit is not
    else:
        while True:
            # check is user want to download multiple files
            multiple=input('\nDo you want to dowanlod multiple videos?(y/n): ').lower()
            if(multiple==('y')):
                while True:
                    # get txt file from user
                    via_txt=input('\nDo you want to send links via a txt file?(y/n)').lower()
                    if(via_txt=='y'):
                        while True:
                            path=input('\nEnter the path of txt file with video links on each line: ')
                            if(fileExists):
                                # urlChecker checks if the url is valid youtube link
                                links=[url for url in open('Example_links.txt', "r").read().splitlines() if urlChecker(url)]                                break
                            else:
                                print('File Not Found!, Please Check the file path')
                    elif(via_txt=='n'):
                        # get one by one link from user
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
                # get single link from user
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

        for i in range(0,len(links)):
            link = links[i]
            print("\nGetting Details of Video")
            # get video object
            yt = YouTube(link)
            os.system('cls')
            print("\nDetails for Video","\n")
            print("Title:   ",yt.title)
            print("Length of video:  ",yt.length,"seconds")
            # get progressive streams i.e audio+video
            stream_ = yt.streams.filter(progressive=True)
            stream=str(stream_)
            stream = stream[1:]
            stream = stream[:-1]
            streamlist = stream.split(", ")
            # display available options
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
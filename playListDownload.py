from helper import humanbytes,fileExists,urlChecker,pathExistsElseCreate,connect
from pytube import Playlist
import os

def main():
    # check is user is conncted to internet
    if not connect():
        print('No Internet Connection!\nExiting....')
        exit() #exit if not
    else:
        while True:
        	# url='https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU'
        	url=input('Enter the Playlist link to Download: ')
        	if urlChecker(url):
        		break
        	else:print('Invalid Url!')
        while True:
            temp=pathExistsElseCreate(input('\nEnter Destination Path("." for this dir):'))
            if temp is not None:
                SAVE_PATH=temp
                break
            else:print('Invalid Path!')

        
        print("\nGetting Details of Playlist")
        pl = Playlist(url)
        os.system('cls')
        print("\nDetails for Playlist","\n")
        print("Title:   ",pl.title()) #may not work for some playlist
        print("\nDownloading...")
        pl.download_all(SAVE_PATH)
        print("\nDownload completed!!")
if __name__ == '__main__':
    main()
from helper import humanbytes,fileExists,urlChecker,pathExistsElseCreate,connect
from pytube import Playlist
import os

def main():
    # check is user is conncted to internet
    if not connect():
        print('No Internet Connection!\nExiting....')
        exit() #exit is not
    else:
        while True:
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

        print("\nGetting Details of Video")
        # get Playlist object
        pl = Playlist(url)
        os.system('cls')
        print("\nDownloading...")
        pl.download_all(SAVE_PATH)
        print("\nDownload completed!!")
if __name__ == '__main__':
    main()
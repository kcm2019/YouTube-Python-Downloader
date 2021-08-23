from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os, requests
from colorama import Fore
import youtube_dl, platform
import subprocess

DEFAULTLINK = "https://www.youtube.com/"
LIST = "list="
WATCH = "watch"
URL = ""
FOLDERNAME = "C:/"

#file location
def openLocation():
    global FOLDERNAME
    FOLDERNAME = filedialog.askdirectory()
    print(FOLDERNAME)
    if(len(FOLDERNAME) > 1):
        locationError.config(text=FOLDERNAME,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")
#  NEED TO ADD CHECK WHERE IF LINK IS A PLAYLIST OF VIDEOS, CURRENTLY WILL THINK EVERYLINK IS A PLAYLIST
def download():
    global FOLDERNAME
    global URL
    URL = ytdEntry.get()
    curr_path = os.getcwd()
    os.chdir(FOLDERNAME)
    isPlaylist = TRUE
    if not isPlaylist:
        subprocess.call("youtube-dl -u temp -p temp --no-playlist --extract-audio {0}".format(URL))
    else:
        ydl_opts = {}
        subprocess.call("youtube-dl -u temp -p temp --yes-playlist --extract-audio {0}".format(URL))
        #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #    ydl.download([URL])
    print("[INFO] Video saved at '{0}'".format(os.getcwd()))
    os.chdir(curr_path) 


root = Tk()
root.title("YouTube Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video/Playlist",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="- - -",fg="black",font=("jost",10))
ytdError.grid()

#Select YouTube Link
#playlistTxtLabel = Label (root, text="Get a playlist of videos downloaded",font=("jost",15,"bold"))
#playlistTxtLabel.grid()

#btn of selecting txt file of video titles
# playlistTxtButton = Button(root,width=28,bg="red",fg="white",text="Choose Path for Playlist of Titles",command=txtVideoTitles)
# playlistTxtButton.grid()

#label to confirm txt playlist found
# playlistTxtConfirmLabel = Label(root,text="- - -",fg="red",font=("jost",10))
# playlistTxtConfirmLabel.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video(s) File(s)",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=28,bg="red",fg="white",text="Choose Path to Save File(s) To",command=openLocation)
saveEntry.grid()

#Error Msg location
locationError = Label(root,text="- - -",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

#download btn
downloadbtn = Button(root,text="Download URL",width=10,bg="red",fg="white",command=download)
downloadbtn.grid()

#btn for initiating download of txt playlist
# downloadTxtPlaylistButton = Button(root,width=20,bg="red",fg="white",text="Download Txt Playlist",command=txtPlaylistDownloader)
# downloadTxtPlaylistButton.grid()

#btn for getting a txt file of YouTube Links 
# txtYouTubeLinksButton = Button(root,width=28,bg="red",fg="white",text="YouTube Links from Text File of Titles",command=txtYouTubeLinks)
# txtYouTubeLinksButton.grid()

#developer Label
developerlabel = Label(root,text="Kurt Muller",font=("jost",15))
developerlabel.grid()
root.mainloop()
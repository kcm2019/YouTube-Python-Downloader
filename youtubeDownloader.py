from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3
from bs4 import BeautifulSoup as bs #pip install beautifulsoup4
import requests
from youtube_search import YoutubeSearch #pip install YoutubeSearch
import time

Folder_Name = ""
Txt_Video_Titles = []


#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

def txtVideoTitles():
    global Txt_Video_Titles
    myFile = filedialog.askopenfile()
    for line in myFile:
        Txt_Video_Titles += [line]
    playlistTxtConfirmLabel.config(text="Text File Selected", fg="green")

#download video
def DownloadVideo():
    ytdError.config(text="Downloading...",fg="blue")
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    #download function
    select = yt.streams.filter(only_audio=True).first()
    select.download(Folder_Name)
    ytdError.config(text="DOWNLOAD COMPLETED!!",fg="green")

def txtPlaylistDownloader():
    global Txt_Video_Titles
    global Folder_Name
    print(Txt_Video_Titles)

    choice = ytdchoices.get()
    print(ytdchoices.get())

    for x in range(len(Txt_Video_Titles)):
        ytdError.config(text=Txt_Video_Titles[x])
        print(Txt_Video_Titles[x])
        
        results = YoutubeSearch(Txt_Video_Titles[x], max_results=1).to_json()
        parseString = "\"url_suffix\": \""
        locations = results.find(parseString) 
        num = locations + len(parseString)
        tempString = results[num:]
        urlEnd = tempString[:tempString.find("\"")] 
        print(urlEnd)
        url = "https://www.youtube.com/" + urlEnd
        print(url +"\n")
             
        if(len(url)>1):
            ytdError.config(text="")
            yt = YouTube(url)

            if(choice == choices[0]):
                select = yt.streams.filter(progressive=True).first()

            elif(choice == choices[1]):
                select = yt.streams.filter(progressive=True,file_extension='mp4').last()

            elif(choice == choices[2]):
                select = yt.streams.filter(only_audio=True).first()

            else:
                ytdError.config(text="Paste Link again!!",fg="red")
        
        select = yt.streams.filter(only_audio=True).first()
        try:
            select.download(Folder_Name)
        except:
            print("Error Downloading Song")
        time.sleep(1)
    
    ytdError.config(text="DOWNLOAD COMPLETED!!",fg="green")


root = Tk()
root.title("YouTube Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.

#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#Error Msg
ytdError = Label(root,text="- - -",fg="black",font=("jost",10))
ytdError.grid()

#Select YouTube Link
playlistTxtLabel = Label (root, text="Get a playlist of videos downloaded",font=("jost",15,"bold"))
playlistTxtLabel.grid()

#btn of selecting txt file of video titles
playlistTxtButton = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=txtVideoTitles)
playlistTxtButton.grid()

#label to confirm txt playlist found
playlistTxtConfirmLabel = Label(root,text="- - -",fg="red",font=("jost",10))
playlistTxtConfirmLabel.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video(s) File(s)",font=("jost",15,"bold"))
saveLabel.grid()

#btn of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
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
downloadbtn = Button(root,text="Download URL",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#btn for initiating download of txt playlist
downloadTxtPlaylistButton = Button(root,width=20,bg="red",fg="white",text="Download Txt Playlist",command=txtPlaylistDownloader)
downloadTxtPlaylistButton.grid()

#developer Label
developerlabel = Label(root,text="Kurt Muller",font=("jost",15))
developerlabel.grid()
root.mainloop()

from pytube import YouTube

def Download(link):
    yt = YouTube(link)  # this is the link of the video you want to download
    streams = yt.streams  # this will give you all the available formats of the video
    title = yt.title  # this will give you the title of the video
    stream = streams.get_highest_resolution()
    URL = stream.url
    print(f"\n\n\nname: {title}\n\nDownload URL: {URL}\n")


Download(input("Enter URL: "))

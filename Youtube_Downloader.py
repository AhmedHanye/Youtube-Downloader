from pytube import YouTube

def Download(link):
    yt = YouTube(link)  # this is the link of the video you want to download
    streams = yt.streams  # this will give you all the available formats of the video
    title = yt.title  # this will give you the title of the video
    l = len(streams)
    for i in range(l):
        # this will split the info into a list
        stream = str(streams[i]).split()
        # this will print the format ,resolution and fps of the video
        print(f"{i}- " + " ".join(stream[2:5]))
    while True:  # this will make sure that the user enters a valid number
        choice = int(input("Which number do you choose: "))
        if choice in range(l):
            break
    # this will give you the download link of the video
    URL = streams[choice].url
    print(f"\n\n\nname: {title}\n\nDownload URL: {URL}\n")


Download(input("Enter URL: "))

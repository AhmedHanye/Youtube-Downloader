from pytube import YouTube


def Download(link):
    yt = YouTube(link)
    # Get the streams
    while True:
        choice1 = int(input(
            "Do you want to download the video or audio or both?\n1. Video\n2. Audio\n3. Both\nEnter the number of your choice: "))
        if choice1 == 1:
            # Get streams that only have video
            streams = yt.streams.filter(only_video=True)
            break
        elif choice1 == 2:
            # Get streams that only have audio
            streams = yt.streams.filter(only_audio=True)
            break
        elif choice1 == 3:
            # Get streams that include both video and audio
            streams = yt.streams.filter(progressive=True, file_extension='mp4')
            break
    # Print the streams
    l = len(streams)
    for i in range(l):
        stream = str(streams[i]).split()[2:5]
        print(f"{i}: {stream}")
    # Get the choice of the stream
    while True:
        choice2 = int(
            input("Enter the number of the stream you want to download: "))
        if choice2 in range(l):
            break
    # Get the title and URL of the stream
    title = yt.title
    URL = streams[choice2].url
    print(f"\n\n\nname: {title}\n\nDownload URL: {URL}\n")


Download(input("Enter the link: "))

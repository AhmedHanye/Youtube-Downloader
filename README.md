# YouTube Video Downloader
This Python script uses the `pytube` library to download YouTube videos. It provides a simple command-line interface to select the desired video format and resolution.
## Prerequisites

Make sure you have Python installed on your machine. You can install the required library using the following:
```
pip install pytube
```
## Example

```
Enter URL: [Paste your YouTube video URL here]
0- mime_type="video/3gpp" res="144p" fps="8fps"
1- mime_type="video/mp4" res="360p" fps="30fps"
2- mime_type="video/mp4" res="720p" fps="30fps"
3- mime_type="video/webm" res="2160p" fps="30fps"
4- mime_type="video/webm" res="1440p" fps="30fps"
5- mime_type="video/webm" res="1080p" fps="30fps"
6- mime_type="video/webm" res="720p" fps="30fps"
7- mime_type="video/mp4" res="1080p" fps="30fps"
8- mime_type="video/webm" res="480p" fps="30fps"
9- mime_type="video/mp4" res="720p" fps="30fps"
10- mime_type="video/webm" res="360p" fps="30fps"
11- mime_type="video/mp4" res="480p" fps="30fps"
12- mime_type="video/webm" res="240p" fps="30fps"
13- mime_type="video/mp4" res="360p" fps="30fps"
14- mime_type="video/webm" res="144p" fps="30fps"
15- mime_type="video/mp4" res="240p" fps="30fps"
16- mime_type="video/mp4" res="144p" fps="30fps"
17- mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5"
18- mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2"
19- mime_type="audio/webm" abr="50kbps" acodec="opus"
20- mime_type="audio/webm" abr="70kbps" acodec="opus"
21- mime_type="audio/webm" abr="160kbps" acodec="opus"
Which number do you choose: 7

name: [Video Title]
Download URL: [Download Link]

```
Replace `[Paste your YouTube video URL here]` with the actual Youtube URL.

## Downloading with External Download Manager

If you encounter any issues with direct download using the provided link, or if you prefer using a download manager, you can follow these steps:

1. Copy the download link provided by the script.

2. Open your preferred download manager, such as [Free Download Manager (FDM)](https://www.freedownloadmanager.org/).

3. Paste the copied download link into the download manager's URL or Add New Download section.

4. Start the download using your download manager.

This allows you to leverage the features and benefits of external download managers for a smoother download experience.

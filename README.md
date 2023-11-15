# YouTube Video Downloader
This Python script uses the `pytube` library to download YouTube videos. It provides a simple command-line interface to get the download link of the youtube video.
## Prerequisites

Make sure you have Python installed on your machine. You can install the required library using the following:
```
pip install pytube
```
## Example

```
Enter URL: [Paste your YouTube video URL here]
Do you want to download the video or audio or both?
1. Video
2. Audio
3. Both
Enter the number of your choice: number
0: ['mime_type="video/mp4"', 'res="144p"', 'fps="30"']
1: ['mime_type="video/mp4"', 'res="240p"', 'fps="30"']
2: ['mime_type="video/mp4"', 'res="360"', 'fps="30"']
3: ['mime_type="video/mp4"', 'res="480p"', 'fps="30"']
4: ['mime_type="video/mp4"', 'res="720p"', 'fps="30"']
5: ['mime_type="video/mp4"', 'res="1080p"', 'fps="30"']
Enter the number of the stream you want to download: number

name: [Video Title]
Download URL: [Download Link]

```

## Downloading with External Download Manager

If you encounter any issues with direct download using the provided link, or if you prefer using a download manager, you can follow these steps:

1. Copy the download link provided by the script.

2. Open your preferred download manager, such as [Free Download Manager (FDM)](https://www.freedownloadmanager.org/).

3. Paste the copied download link into the download manager's URL or Add New Download section.

4. Start the download using your download manager.

This allows you to leverage the features and benefits of external download managers for a smoother download experience.

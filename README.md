# Python YouTube Downloader

This Python script enables you to download YouTube videos and playlists quickly and efficiently using the `yt-dlp` library. It supports downloading both video and audio formats in various resolutions.

## Features

- Download single YouTube videos or entire playlists.
- Choose preferred video resolution for playlist downloads.
- Fast and efficient downloading using yt-dlp.
- You Can Download and Resolution Available.

## Requirements

- Install [Python 3.x](https://www.python.org/downloads/)
- Install [yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/Installation) Library.
- Install [FFmpeg](https://ffmpeg.org/download.html) :

  1. Windows : https://phoenixnap.com/kb/ffmpeg-windows
  2. Linux : https://phoenixnap.com/kb/install-ffmpeg-ubuntu
  3. Mac : https://phoenixnap.com/kb/ffmpeg-mac

- install colorama :
  ```
    pip install colorama
  ```
## Example :
### youtube audio:
```
azureuser@ubuntu:~/Downloads$ python3 main.py
Enter the video URL: https://youtu.be/vKyd7k0-OBw?si=nd7NMw0UlRXEhghU
[youtube] Extracting URL: https://youtu.be/vKyd7k0-OBw?si=nd7NMw0UlRXEhghU
[youtube] vKyd7k0-OBw: Downloading webpage
[youtube] vKyd7k0-OBw: Downloading ios player API JSON
[youtube] vKyd7k0-OBw: Downloading android player API JSON
[youtube] vKyd7k0-OBw: Downloading m3u8 information
Youtube Video : I Compared Best VPN Services In 2024_ Surfshark Vs NordVPN
Enter the type of the download (video/audio): audio
Enter the path to save: ./
[youtube] Extracting URL: https://youtu.be/vKyd7k0-OBw?si=nd7NMw0UlRXEhghU
[youtube] vKyd7k0-OBw: Downloading webpage
[youtube] vKyd7k0-OBw: Downloading ios player API JSON
[youtube] vKyd7k0-OBw: Downloading android player API JSON
[youtube] vKyd7k0-OBw: Downloading m3u8 information
[info] vKyd7k0-OBw: Downloading 1 format(s): 140
[download] Destination: ./I Compared Best VPN Services In 2024_ Surfshark Vs NordVPN.m4a
[download] 100% of    9.57MiB in 00:00:00 at 24.86MiB/s
[FixupM4a] Correcting container of "./I Compared Best VPN Services In 2024_ Surfshark Vs NordVPN.m4a"
```
### youtube video:
```
azureuser@ubuntu:~/Downloads$ python3 main.py
Enter the video URL: https://youtu.be/vKyd7k0-OBw?si=nd7NMw0UlRXEhghU
[youtube] Extracting URL: https://youtu.be/vKyd7k0-OBw?si=nd7NMw0UlRXEhghU
[youtube] vKyd7k0-OBw: Downloading webpage
[youtube] vKyd7k0-OBw: Downloading ios player API JSON
[youtube] vKyd7k0-OBw: Downloading android player API JSON
[youtube] vKyd7k0-OBw: Downloading m3u8 information
Youtube Video : I Compared Best VPN Services In 2024_ Surfshark Vs NordVPN
Enter the type of the download (video/audio): video
1.  mp4 res: 256x144    fps: 15  SDR
2.  mp4 res: 256x144    fps: 30  SDR
3.  mp4 res: 426x240    fps: 30  SDR
4.  mp4 res: 640x360    fps: 30  SDR
5.  mp4 res: 640x360    fps: 30  SDR
6.  mp4 res: 854x480    fps: 30  SDR
7.  mp4 res: 1280x720   fps: 30  SDR
8.  mp4 res: 1280x720   fps: 30  SDR
9.  mp4 res: 1920x1080  fps: 30  SDR
Enter the index of the format you want to download: 9
Enter the path to save: ./
https://youtu.be/vKyd7k0-OBw?si=nd7NMw0UlRXEhghU
```
### youtube list:
```
azureuser@ubuntu:~/Downloads$ python3 main.py
Enter the video URL: https://www.youtube.com/playlist?list=PLa8oKYy_2UcN9ZEJ2GNll15voCRJX4gKz
Youtube Playlist : VPN reviews It has 24 videos.
Enter the path to save: ./
Enter the preferred resolution (e.g. 1080) or enter best or worst: worst
[download] 100% of    2.27MiB in 00:00:00 at 11.64MiB/sDownload complete: ./VPN reviews/01 - I Compared Best VPN Services In 2024： Surfshark Vs NordVPN.f597.mp4
[download] 100% of    2.28MiB in 00:00:00 at 34.01MiB/sDownload complete: ./VPN reviews/01 - I Compared Best VPN Services In 2024： Surfshark Vs NordVPN.f599.m4a
[download] 100% of    2.44MiB in 00:00:00 at 8.65MiB/sDownload complete: ./VPN reviews/02 - Full NordVPN Review and Tutorial ｜ Is the hype deserved？.f597.mp4
[download] 100% of    2.34MiB in 00:00:00 at 19.99MiB/sDownload complete: ./VPN reviews/02 - Full NordVPN Review and Tutorial ｜ Is the hype deserved？.f599.m4a
[download] 100% of    2.26MiB in 00:00:00 at 10.27MiB/sDownload complete: ./VPN reviews/03 - Surfshark VPN review ｜ Should you use Surfshark in 2024？.f597.mp4
[download] 100% of    2.10MiB in 00:00:00 at 25.42MiB/sDownload complete: ./VPN reviews/03 - Surfshark VPN review ｜ Should you use Surfshark in 2024？.f599.m4a
[download] 100% of    2.29MiB in 00:00:00 at 9.29MiB/sDownload complete: ./VPN reviews/04 - NordVPN vs CyberGhost ｜ Which one should YOU pick？.f597.mp4
[download] 100% of    2.40MiB in 00:00:00 at 18.87MiB/sDownload complete: ./VPN reviews/04 - NordVPN vs CyberGhost ｜ Which one should YOU pick？.f599.m4a
ERROR: [youtube] q7-a7o_4_rc: Private video. Sign in if you've been granted access to this video
[download] 100% of    1.85MiB in 00:00:00 at 6.79MiB/sDownload complete: ./VPN reviews/06 - Proton VPN vs ExpressVPN ｜ Which is better？.f597.mp4
[download] 100% of    1.75MiB in 00:00:00 at 20.89MiB/sDownload complete: ./VPN reviews/06 - Proton VPN vs ExpressVPN ｜ Which is better？.f599.m4a
[download] 100% of    1.93MiB in 00:00:00 at 9.79MiB/sDownload complete: ./VPN reviews/07 - NordVPN vs Proton VPN ｜ Best VPN comparison.f597.mp4
[download] 100% of    1.99MiB in 00:00:00 at 32.47MiB/sDownload complete: ./VPN reviews/07 - NordVPN vs Proton VPN ｜ Best VPN comparison.f599.m4a
[download] 100% of    1.72MiB in 00:00:00 at 7.34MiB/sDownload complete: ./VPN reviews/08 - Atlas VPN review 2024 ｜ Does it still hold up？.f597.mp4
[download] 100% of    1.78MiB in 00:00:00 at 22.99MiB/sDownload complete: ./VPN reviews/08 - Atlas VPN review 2024 ｜ Does it still hold up？.f599.m4a
ERROR: [youtube] FZW2EAvefHA: Private video. Sign in if you've been granted access to this video
[download] 100% of    2.44MiB in 00:00:00 at 12.29MiB/sDownload complete: ./VPN reviews/10 - NordVPN vs ExpressVPN vs Surfshark ｜ Best VPN comparison.f597.mp4
[download] 100% of    2.34MiB in 00:00:00 at 20.52MiB/sDownload complete: ./VPN reviews/10 - NordVPN vs ExpressVPN vs Surfshark ｜ Best VPN comparison.f599.m4a
[download] 100% of    2.44MiB in 00:00:00 at 40.54MiB/sDownload complete: ./VPN reviews/11 - I Compared NordVPN vs Cyberghost VPN To See Which Is Better.f597.mp4
[download] 100% of    2.23MiB in 00:00:00 at 22.71MiB/sDownload complete: ./VPN reviews/11 - I Compared NordVPN vs Cyberghost VPN To See Which Is Better.f599.m4a
[download] 100% of    1.80MiB in 00:00:00 at 8.08MiB/sDownload complete: ./VPN reviews/12 - Norton VPN review ｜ Should you use the Norton Secure VPN in 2024？.f597.mp4
[download] 100% of    1.89MiB in 00:00:00 at 16.07MiB/sDownload complete: ./VPN reviews/12 - Norton VPN review ｜ Should you use the Norton Secure VPN in 2024？.f599.m4a
[download] 100% of    1.44MiB in 00:00:00 at 3.87MiB/sDownload complete: ./VPN reviews/13 - CyberGhost VPN tutorial ｜ Learn to use it today [EASY GUIDE].f597.mp4
[download] 100% of    1.38MiB in 00:00:00 at 11.37MiB/sDownload complete: ./VPN reviews/13 - CyberGhost VPN tutorial ｜ Learn to use it today [EASY GUIDE].f599.m4a
[download] 100% of    1.94MiB in 00:00:00 at 8.59MiB/sDownload complete: ./VPN reviews/14 - How to use IPVanish ｜ IPVanish TUTORIAL and REVIEW 2024.f597.mp4
[download] 100% of    1.82MiB in 00:00:00 at 26.24MiB/sDownload complete: ./VPN reviews/14 - How to use IPVanish ｜ IPVanish TUTORIAL and REVIEW 2024.f599.m4a
[download] 100% of    1.35MiB in 00:00:00 at 6.34MiB/sDownload complete: ./VPN reviews/15 - NordVPN vs Windscribe ｜ Which is more reliable？.f597.mp4
[download] 100% of    1.45MiB in 00:00:00 at 19.15MiB/sDownload complete: ./VPN reviews/15 - NordVPN vs Windscribe ｜ Which is more reliable？.f599.m4a
[download] 100% of    1.40MiB in 00:00:00 at 5.47MiB/sDownload complete: ./VPN reviews/16 - Can you trust Proton VPN and Proton Mail？ [Bundle review].f597.mp4
[download] 100% of    1.64MiB in 00:00:00 at 23.52MiB/sDownload complete: ./VPN reviews/16 - Can you trust Proton VPN and Proton Mail？ [Bundle review].f599.m4a
[download] 100% of    1.73MiB in 00:00:00 at 8.99MiB/sDownload complete: ./VPN reviews/17 - NordVPN vs MullvadVPN ｜ Best VPN comparison.f597.mp4
[download] 100% of    1.73MiB in 00:00:00 at 20.04MiB/sDownload complete: ./VPN reviews/17 - NordVPN vs MullvadVPN ｜ Best VPN comparison.f599.m4a
ERROR: [youtube] Hul3CsjHdRA: Private video. Sign in if you've been granted access to this video
[download] 100% of    2.89MiB in 00:00:00 at 12.72MiB/sDownload complete: ./VPN reviews/19 - BEST VPN picks of 2023 [Updated review].f597.mp4
[download] 100% of    2.68MiB in 00:00:00 at 20.71MiB/sDownload complete: ./VPN reviews/19 - BEST VPN picks of 2023 [Updated review].f599.m4a
[download] 100% of    2.03MiB in 00:00:00 at 22.39MiB/sDownload complete: ./VPN reviews/20 - Is Surfshark VPN Worth It？ ｜ Updated Surfshark review.f597.mp4
[download] 100% of    1.85MiB in 00:00:00 at 40.21MiB/sDownload complete: ./VPN reviews/20 - Is Surfshark VPN Worth It？ ｜ Updated Surfshark review.f599.m4a
ERROR: [youtube] JVmxh2dhSFU: Private video. Sign in if you've been granted access to this video
[download] 100% of    1.91MiB in 00:00:00 at 8.91MiB/sDownload complete: ./VPN reviews/22 - NordVPN vs ExpressVPN ｜ Best VPN comparison 2024.f597.mp4
[download] 100% of    1.83MiB in 00:00:00 at 25.23MiB/sDownload complete: ./VPN reviews/22 - NordVPN vs ExpressVPN ｜ Best VPN comparison 2024.f599.m4a
ERROR: [youtube] L7oUcxlGcUM: Private video. Sign in if you've been granted access to this video
[download] 100% of    2.46MiB in 00:00:00 at 10.42MiB/sDownload complete: ./VPN reviews/24 - Best FREE VPN for iPhone picks ｜ Free VPNs you can trust.f597.mp4
[download] 100% of    2.16MiB in 00:00:00 at 21.16MiB/sDownload complete: ./VPN reviews/24 - Best FREE VPN for iPhone picks ｜ Free VPNs you can trust.f599.m4a
```
#
Feel free to customize this app according to your specific project details and preferences. Let me know if you need further assistance!

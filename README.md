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
Enter the video URL: https://youtu.be/_4kHxtiuML0?si=Td_9k7HB-mK4N37m
[youtube] Extracting URL: https://youtu.be/_4kHxtiuML0?si=Td_9k7HB-mK4N37m 
[youtube] _4kHxtiuML0: Downloading webpage 
[youtube] _4kHxtiuML0: Downloading ios player API JSON 
[youtube] _4kHxtiuML0: Downloading android player API JSON 
[youtube] _4kHxtiuML0: Downloading m3u8 information 
Youtube Video : Focus Music for Work and Studying, Background Music for Concentration, Study Music
Enter the type of the download (video/audio): audio
Enter the path to save: "C:\Users\ahmedhanye\Downloads"
[youtube] Extracting URL: https://youtu.be/_4kHxtiuML0?si=Td_9k7HB-mK4N37m 
[youtube] _4kHxtiuML0: Downloading webpage 
[youtube] _4kHxtiuML0: Downloading ios player API JSON 
[youtube] _4kHxtiuML0: Downloading android player API JSON 
WARNING: [youtube] YouTube said: ERROR - Precondition check failed. 
WARNING: [youtube] HTTP Error 400: Bad Request. Retrying (1/3)... 
[youtube] _4kHxtiuML0: Downloading android player API JSON 
[youtube] _4kHxtiuML0: Downloading m3u8 information 
[info] _4kHxtiuML0: Downloading 1 format(s): 140 
[download] Destination: C:\Users\ahmedhanye\Downloads\Focus Music for Work and Studying, Background Music for Concentration, Study Music.m4a 
[download] 100% of  508.29MiB in 00:00:06 at 75.78MiB/s
[FixupM4a] Correcting container of "C:\Users\ahmedhanye\Downloads\Focus Music for Work and Studying, Background Music for Concentration, Study Music.m4a"
```
### youtube video:
```
Enter the video URL: https://youtu.be/7PIji8OubXU?si=H-3zMt_ALfClXGjW
[youtube] Extracting URL: https://youtu.be/7PIji8OubXU?si=H-3zMt_ALfClXGjW 
[youtube] 7PIji8OubXU: Downloading webpage 
[youtube] 7PIji8OubXU: Downloading ios player API JSON 
[youtube] 7PIji8OubXU: Downloading android player API JSON 
[youtube] 7PIji8OubXU: Downloading m3u8 information 
Youtube Video : Best of Dolby Vision 12K HDR 120fps
Enter the type of the download (video/audio): video
1.  mp4 res: 256x144    fps: 15  SDR
2.  mp4 res: 256x144    fps: 30  SDR
3.  mp4 res: 256x144    fps: 60  HDR10
4.  mp4 res: 426x240    fps: 30  SDR
5.  mp4 res: 426x240    fps: 60  HDR10
6.  mp4 res: 640x360    fps: 30  SDR
7.  mp4 res: 640x360    fps: 30  SDR
8.  mp4 res: 640x360    fps: 60  HDR10
9.  mp4 res: 854x480    fps: 30  SDR
10. mp4 res: 854x480    fps: 60  HDR10
11. mp4 res: 1280x720   fps: 30  SDR
12. mp4 res: 1280x720   fps: 30  SDR
13. mp4 res: 1280x720   fps: 60  SDR
14. mp4 res: 1280x720   fps: 60  HDR10
15. mp4 res: 1920x1080  fps: 60  SDR
16. mp4 res: 1920x1080  fps: 60  HDR10
17. mp4 res: 2560x1440  fps: 60  HDR10
18. mp4 res: 3840x2160  fps: 60  HDR10
19. mp4 res: 7680x4320  fps: 60  HDR10
Enter the index of the format you want to download: 16
Enter the path to save: "C:\Users\ahmedhanye\Downloads"
https://youtu.be/7PIji8OubXU?si=H-3zMt_ALfClXGjW
[youtube] Extracting URL: https://youtu.be/7PIji8OubXU?si=H-3zMt_ALfClXGjW 
[youtube] 7PIji8OubXU: Downloading webpage 
[youtube] 7PIji8OubXU: Downloading ios player API JSON 
[youtube] 7PIji8OubXU: Downloading android player API JSON 
[youtube] 7PIji8OubXU: Downloading player 31eb286a 
[youtube] 7PIji8OubXU: Downloading m3u8 information 
[info] 7PIji8OubXU: Downloading 1 format(s): 699+140 
[download] Destination: C:\Users\ahmedhanye\Downloads\Best of Dolby Vision 12K HDR 120fps_(1080p60_HDR).f699.mp4 
[download] 100% of  440.16MiB in 00:00:07 at 62.68MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\Best of Dolby Vision 12K HDR 120fps_(1080p60_HDR).f140.m4a 
[download] 100% of   11.36MiB in 00:00:00 at 52.52MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\Best of Dolby Vision 12K HDR 120fps_(1080p60_HDR).mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\Best of Dolby Vision 12K HDR 120fps_(1080p60_HDR).f699.mp4 (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\Best of Dolby Vision 12K HDR 120fps_(1080p60_HDR).f140.m4a (pass -k to keep)
```
### youtube list:
```
Enter the video URL: https://www.youtube.com/playlist?list=PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj
WARNING: [youtube:tab] Incomplete data received. Retrying (1/3)... 
WARNING: [youtube:tab] Incomplete data received. Retrying (2/3)... 
WARNING: [youtube:tab] Incomplete data received. Retrying (3/3)... 
WARNING: [youtube:tab] Incomplete data received. Giving up after 3 retries 
Youtube Playlist : iPhone 15 It has 12 videos.
Enter the path to save: "C:\Users\ahmedhanye\Downloads"
Enter the preferred resolution (e.g. 1080) or enter best or worst: best
[youtube:tab] Extracting URL: https://www.youtube.com/playlist?list=PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj 
[youtube:tab] PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj: Downloading webpage 
[youtube:tab] PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj: Redownloading playlist API JSON with unavailable videos 
[download] Downloading playlist: iPhone 15 
[youtube:tab] PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj page 1: Downloading API JSON 
WARNING: [youtube:tab] Incomplete data received. Retrying (1/3)... 
[youtube:tab] PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj page 1: Downloading API JSON 
WARNING: [youtube:tab] Incomplete data received. Retrying (2/3)... 
[youtube:tab] PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj page 1: Downloading API JSON 
WARNING: [youtube:tab] Incomplete data received. Retrying (3/3)... 
[youtube:tab] PLHFlHpPjgk70ntj4sBolp4X0KfkFQW8qj page 1: Downloading API JSON 
WARNING: [youtube:tab] Incomplete data received. Giving up after 3 retries 
[youtube:tab] Playlist iPhone 15: Downloading 12 items of 12
[download] Downloading item 1 of 12
[youtube] Extracting URL: https://www.youtube.com/watch?v=TPq4XRgC5gQ
[youtube] TPq4XRgC5gQ: Downloading webpage
[youtube] TPq4XRgC5gQ: Downloading ios player API JSON 
[youtube] TPq4XRgC5gQ: Downloading android player API JSON 
[youtube] TPq4XRgC5gQ: Downloading m3u8 information 
[info] TPq4XRgC5gQ: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 8 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\01 - iPhone 15 Ceramic Shield ｜ Swoop ｜ Apple.f616.mp4
[download] 100% of   14.94MiB in 00:00:01 at 10.61MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\01 - iPhone 15 Ceramic Shield ｜ Swoop ｜ Apple.f140.m4a 
[download] 100% of  602.89KiB in 00:00:00 at 14.93MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\01 - iPhone 15 Ceramic Shield ｜ Swoop ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\01 - iPhone 15 Ceramic Shield ｜ Swoop ｜ Apple.f616.mp4 (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\01 - iPhone 15 Ceramic Shield ｜ Swoop ｜ Apple.f140.m4a (pass -k to keep)
[download] Downloading item 2 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=Tcwtq9NrVd4
[youtube] Tcwtq9NrVd4: Downloading webpage 
[youtube] Tcwtq9NrVd4: Downloading ios player API JSON 
[youtube] Tcwtq9NrVd4: Downloading android player API JSON 
[youtube] Tcwtq9NrVd4: Downloading m3u8 information 
[info] Tcwtq9NrVd4: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 8 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\02 - iPhone 15 Plus Battery ｜ One More ｜ Apple.f616.mp4
[download] 100% of   11.45MiB in 00:00:00 at 17.49MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\02 - iPhone 15 Plus Battery ｜ One More ｜ Apple.f140.m4a 
[download] 100% of  602.89KiB in 00:00:00 at 18.85MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\02 - iPhone 15 Plus Battery ｜ One More ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\02 - iPhone 15 Plus Battery ｜ One More ｜ Apple.f140.m4a (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\02 - iPhone 15 Plus Battery ｜ One More ｜ Apple.f616.mp4 (pass -k to keep)
[download] Downloading item 3 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=U-7ibjo1xHc
[youtube] U-7ibjo1xHc: Downloading webpage
[youtube] U-7ibjo1xHc: Downloading ios player API JSON 
[youtube] U-7ibjo1xHc: Downloading android player API JSON 
[youtube] U-7ibjo1xHc: Downloading m3u8 information 
[info] U-7ibjo1xHc: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 8 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\03 - iPhone 15 Check In ｜ New Driver ｜ Apple.f616.mp4
[download] 100% of    5.71MiB in 00:00:00 at 9.97MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\03 - iPhone 15 Check In ｜ New Driver ｜ Apple.f140.m4a 
[download] 100% of  602.89KiB in 00:00:00 at 13.42MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\03 - iPhone 15 Check In ｜ New Driver ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\03 - iPhone 15 Check In ｜ New Driver ｜ Apple.f140.m4a (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\03 - iPhone 15 Check In ｜ New Driver ｜ Apple.f616.mp4 (pass -k to keep)
[download] Downloading item 4 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=07cKD8GK__c
[youtube] 07cKD8GK__c: Downloading webpage
[youtube] 07cKD8GK__c: Downloading ios player API JSON 
[youtube] 07cKD8GK__c: Downloading android player API JSON 
[youtube] 07cKD8GK__c: Downloading m3u8 information 
[info] 07cKD8GK__c: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 8 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\04 - iPhone 15 Plus ｜ Miss You ｜ Apple.f616.mp4
[download] 100% of    5.12MiB in 00:00:00 at 9.16MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\04 - iPhone 15 Plus ｜ Miss You ｜ Apple.f140.m4a 
[download] 100% of  602.89KiB in 00:00:00 at 14.65MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\04 - iPhone 15 Plus ｜ Miss You ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\04 - iPhone 15 Plus ｜ Miss You ｜ Apple.f140.m4a (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\04 - iPhone 15 Plus ｜ Miss You ｜ Apple.f616.mp4 (pass -k to keep)
[download] Downloading item 5 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=ei0WDdT4-6A
[youtube] ei0WDdT4-6A: Downloading webpage
[youtube] ei0WDdT4-6A: Downloading ios player API JSON 
[youtube] ei0WDdT4-6A: Downloading android player API JSON 
[youtube] ei0WDdT4-6A: Downloading m3u8 information 
[info] ei0WDdT4-6A: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest
[hlsnative] Total fragments: 21 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\05 - iPhone 15 ｜ Camera ｜ Album Cover ｜ Apple.f616.mp4
[download] 100% of   15.46MiB in 00:00:02 at 7.03MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\05 - iPhone 15 ｜ Camera ｜ Album Cover ｜ Apple.f140.m4a 
[download] 100% of    1.67MiB in 00:00:00 at 26.96MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\05 - iPhone 15 ｜ Camera ｜ Album Cover ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\05 - iPhone 15 ｜ Camera ｜ Album Cover ｜ Apple.f140.m4a (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\05 - iPhone 15 ｜ Camera ｜ Album Cover ｜ Apple.f616.mp4 (pass -k to keep)
[download] Downloading item 6 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=rN_zkpV52J0
[youtube] rN_zkpV52J0: Downloading webpage
[youtube] rN_zkpV52J0: Downloading ios player API JSON 
[youtube] rN_zkpV52J0: Downloading android player API JSON 
[youtube] rN_zkpV52J0: Downloading m3u8 information 
[info] rN_zkpV52J0: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 13 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\06 - iPhone 15 Pro ｜ On with the Show ｜ Apple.f616.mp4
[download] 100% of   23.21MiB in 00:00:01 at 19.90MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\06 - iPhone 15 Pro ｜ On with the Show ｜ Apple.f140.m4a 
[download] 100% of    1.05MiB in 00:00:00 at 17.71MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\06 - iPhone 15 Pro ｜ On with the Show ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\06 - iPhone 15 Pro ｜ On with the Show ｜ Apple.f140.m4a (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\06 - iPhone 15 Pro ｜ On with the Show ｜ Apple.f616.mp4 (pass -k to keep)
[download] Downloading item 7 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=jBFhHHpjbHk
[youtube] jBFhHHpjbHk: Downloading webpage
[youtube] jBFhHHpjbHk: Downloading ios player API JSON 
[youtube] jBFhHHpjbHk: Downloading android player API JSON 
[youtube] jBFhHHpjbHk: Downloading m3u8 information 
[info] jBFhHHpjbHk: Downloading 1 format(s): 616+140
[hlsnative] Downloading m3u8 manifest
[hlsnative] Total fragments: 8
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\07 - iPhone 15 Pro ｜ Pro Power ｜ Apple.f616.mp4
[download] 100% of    6.19MiB in 00:00:01 at 5.69MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\07 - iPhone 15 Pro ｜ Pro Power ｜ Apple.f140.m4a
[download] 100% of  602.89KiB in 00:00:00 at 6.10MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\07 - iPhone 15 Pro ｜ Pro Power ｜ Apple.mp4"
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\07 - iPhone 15 Pro ｜ Pro Power ｜ Apple.f616.mp4 (pass -k to keep)
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\07 - iPhone 15 Pro ｜ Pro Power ｜ Apple.f140.m4a (pass -k to keep)
[download] Downloading item 8 of 12
[youtube] Extracting URL: https://www.youtube.com/watch?v=xqyUdNxWazA
[youtube] xqyUdNxWazA: Downloading webpage
[youtube] xqyUdNxWazA: Downloading ios player API JSON
[youtube] xqyUdNxWazA: Downloading android player API JSON
[youtube] xqyUdNxWazA: Downloading m3u8 information
[info] xqyUdNxWazA: Downloading 1 format(s): 616+140
[hlsnative] Downloading m3u8 manifest
[hlsnative] Total fragments: 49
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\08 - Introducing iPhone 15 Pro ｜ Apple.f616.mp4
[download] 100% of   87.23MiB in 00:00:08 at 10.79MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\08 - Introducing iPhone 15 Pro ｜ Apple.f140.m4a 
[download] 100% of    3.71MiB in 00:00:00 at 29.31MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\08 - Introducing iPhone 15 Pro ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\08 - Introducing iPhone 15 Pro ｜ Apple.f616.mp4 (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\08 - Introducing iPhone 15 Pro ｜ Apple.f140.m4a (pass -k to keep) 
[download] Downloading item 9 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=XHTrLYShBRQ 
[youtube] XHTrLYShBRQ: Downloading webpage 
[youtube] XHTrLYShBRQ: Downloading ios player API JSON 
[youtube] XHTrLYShBRQ: Downloading android player API JSON 
[youtube] XHTrLYShBRQ: Downloading m3u8 information 
[info] XHTrLYShBRQ: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 9 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\09 - Introducing iPhone 15 ｜ WOW ｜ Apple.f616.mp4 
[download] 100% of    9.19MiB in 00:00:00 at 9.54MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\09 - Introducing iPhone 15 ｜ WOW ｜ Apple.f140.m4a 
[download] 100% of  745.29KiB in 00:00:00 at 19.28MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\09 - Introducing iPhone 15 ｜ WOW ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\09 - Introducing iPhone 15 ｜ WOW ｜ Apple.f140.m4a (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\09 - Introducing iPhone 15 ｜ WOW ｜ Apple.f616.mp4 (pass -k to keep) 
[download] Downloading item 10 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=EcGXCJm3XMA 
[youtube] EcGXCJm3XMA: Downloading webpage 
[youtube] EcGXCJm3XMA: Downloading ios player API JSON 
[youtube] EcGXCJm3XMA: Downloading android player API JSON 
WARNING: [youtube] YouTube said: ERROR - Precondition check failed. 
WARNING: [youtube] HTTP Error 400: Bad Request. Retrying (1/3)... 
[youtube] EcGXCJm3XMA: Downloading android player API JSON 
[youtube] EcGXCJm3XMA: Downloading m3u8 information 
[info] EcGXCJm3XMA: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 92 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\10 - A Guided Tour of iPhone 15 & iPhone 15 Pro ｜ Apple.f616.mp4
[download] 100% of  159.33MiB in 00:00:06 at 23.71MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\10 - A Guided Tour of iPhone 15 & iPhone 15 Pro ｜ Apple.f140.m4a 
[download] 100% of    7.88MiB in 00:00:00 at 57.37MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\10 - A Guided Tour of iPhone 15 & iPhone 15 Pro ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\10 - A Guided Tour of iPhone 15 & iPhone 15 Pro ｜ Apple.f616.mp4 (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\10 - A Guided Tour of iPhone 15 & iPhone 15 Pro ｜ Apple.f140.m4a (pass -k to keep) 
[download] Downloading item 11 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=w_JEezynhrc
[youtube] w_JEezynhrc: Downloading webpage
[youtube] w_JEezynhrc: Downloading ios player API JSON 
[youtube] w_JEezynhrc: Downloading android player API JSON 
[youtube] w_JEezynhrc: Downloading m3u8 information 
[info] w_JEezynhrc: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 7
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\11 - iPhone 15 Pro ｜ Titanium ｜ Apple.f616.mp4
[download] 100% of    6.18MiB in 00:00:00 at 7.74MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\11 - iPhone 15 Pro ｜ Titanium ｜ Apple.f140.m4a 
[download] 100% of  602.89KiB in 00:00:00 at 8.62MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\11 - iPhone 15 Pro ｜ Titanium ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\11 - iPhone 15 Pro ｜ Titanium ｜ Apple.f616.mp4 (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\11 - iPhone 15 Pro ｜ Titanium ｜ Apple.f140.m4a (pass -k to keep)
[download] Downloading item 12 of 12 
[youtube] Extracting URL: https://www.youtube.com/watch?v=b19w5cHUnPg
[youtube] b19w5cHUnPg: Downloading webpage
[youtube] b19w5cHUnPg: Downloading ios player API JSON 
[youtube] b19w5cHUnPg: Downloading android player API JSON 
[youtube] b19w5cHUnPg: Downloading m3u8 information 
[info] b19w5cHUnPg: Downloading 1 format(s): 616+140 
[hlsnative] Downloading m3u8 manifest 
[hlsnative] Total fragments: 50 
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\12 - iPhone + Apple Watch ｜ Another Birthday ｜ Apple.f616.mp4
[download] 100% of   60.77MiB in 00:00:08 at 6.86MiB/s
[download] Destination: C:\Users\ahmedhanye\Downloads\iPhone 15\12 - iPhone + Apple Watch ｜ Another Birthday ｜ Apple.f140.m4a 
[download] 100% of    3.82MiB in 00:00:00 at 44.32MiB/s
[Merger] Merging formats into "C:\Users\ahmedhanye\Downloads\iPhone 15\12 - iPhone + Apple Watch ｜ Another Birthday ｜ Apple.mp4" 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\12 - iPhone + Apple Watch ｜ Another Birthday ｜ Apple.f616.mp4 (pass -k to keep) 
Deleting original file C:\Users\ahmedhanye\Downloads\iPhone 15\12 - iPhone + Apple Watch ｜ Another Birthday ｜ Apple.f140.m4a (pass -k to keep)      
[download] Finished downloading playlist: iPhone 15
```
#
Feel free to customize this app according to your specific project details and preferences. Let me know if you need further assistance!

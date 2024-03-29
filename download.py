from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError, ExtractorError
import re
import os


# Check if the link is a valid YouTube video or playlist URL or none of them
def check_url(link):
    # Regular expressions to match YouTube video and playlist URLs
    video_regex = (
        r"^https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})"
    )
    shorts_regex = r"^https:\/\/www\.youtube\.com\/shorts\/[a-zA-Z0-9_-]+"
    playlist_regex = r"^https?://(?:www\.)?youtube\.com/playlist\?list=([a-zA-Z0-9_-]+)"

    # Check if the link matches video or playlist URL patterns
    video_match = re.match(video_regex, link)
    shorts_match = re.match(shorts_regex, link)
    playlist_match = re.match(playlist_regex, link)

    if video_match or shorts_match:
        return "video"
    elif playlist_match:
        return "playlist"
    else:
        return False


# Get available formats
def get_video_data(url):
    with YoutubeDL() as ydl:
        formats = ydl.extract_info(url, download=False)
        # Get video title, default to 'video' if not available
        title = formats.get("title", "video")
        formats = formats["formats"]
        return title, formats


# Function to display available formats with MP4 extension
def display_formats(formats):
    videos_formats = {}
    count = 0
    for idx, format in enumerate(formats):
        if format["video_ext"] == "mp4" and len(format["format"].split()) > 3:
            count += 1
            print(
                (str(count) + ".").ljust(3, " "),
                format["video_ext"],
                "res:",
                format["format"].split()[2].ljust(10, " "),
                "fps:",
                str(format["fps"]).ljust(3, " "),
                format["dynamic_range"],
            )
            videos_formats[count] = idx
    return videos_formats


# Remove illegal characters from video title so nothing goes wrong when saving
#     example 'The Parallax Effect // 5 Minute WebDev Project'
#     this makes a folder for the video and puts the video in it
#     this should not happen it should just make the video without folders
#     that's why I'm using the sanitize_title function to remove illegal characters
def sanitize_title(title):
    return re.sub(r'[\\/:"*?<>|]+', "_", title)


# ask for the type of the download (video/audio)
def ask_for_type():
    while True:
        type = input("Enter the type of the download (video/audio): ")
        if type.lower() in ["video", "audio"]:
            return type.lower()
        else:
            print("Invalid type. Please enter a valid type.")


# Download Audio
def download_audio(url, title, download_path):
    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "outtmpl": os.path.join(download_path, f"{title}.m4a"),
        "no_warnings": True,  # Set to True to suppress all warnings
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download Audio has been completed.")


# Prompt user to choose resolution
def ask_for_resolution(formats, video_f):
    while True:
        try:
            chosen_format = int(
                input("Enter the index of the format you want to download: ")
            )
            if chosen_format in video_f:
                break
        except ValueError:
            print("Please enter a valid number")
            continue
    chosen_format_id = formats[video_f[chosen_format]]["format_id"]
    chosen_format_res = "_".join(formats[video_f[chosen_format]]["format"].split()[3:])
    return chosen_format_id, chosen_format_res


def ask_for_path():
    while True:
        path = input("Enter the path to save: ").strip(
            '"'
        )  # Strip double quotes if present
        # Normalize the path to handle both '/' and '\'
        normalized_path = os.path.normpath(path)
        if os.path.isdir(normalized_path):
            return normalized_path
        else:
            print("Invalid path. Please enter a valid directory path.")


# Download Video
def download_video(url, title, chosen_format_id, chosen_format_res, download_path):
    ydl_opts = {
        "format": f"{chosen_format_id}+bestaudio[ext=m4a]/best[ext=mp4]/best",
        # Output file name with video title
        "outtmpl": os.path.join(download_path, f"{title}_{chosen_format_res}.mp4"),
        "quiet": True,  # Set to True to suppress youtube-dl messages
        "no_warnings": True,  # Set to True to suppress all warnings
    }
    print(url)
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download Video has been completed.")


# Get playlist info
def get_playlist_info(url):
    ydl_opts = {
        "quiet": True,  # Suppress console output
        "extract_flat": True,  # Extract only flat information (no downloading)
        # Use generic extractor to avoid extraction errors
        "force_generic_extractor": True,
        "dump_single_json": True,  # Output info in JSON format
        "no_warnings": True,  # Set to True to suppress all warnings
    }

    with YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(url, download=False)
        title = playlist_info.get("title", "Playlist")
        total_items = len(playlist_info.get("entries", []))
        return title, total_items


# ask for the preferred resolution of the playlist
def ask_for_playlist_res():
    while True:
        res = input(
            "Enter the preferred resolution (e.g. 1080) or enter best or worst: "
        )
        if res in [
            "144",
            "240",
            "360",
            "480",
            "720",
            "1080",
            "1440",
            "2160",
            "4320",
        ] or res.lower() in ["best", "worst"]:
            return res
        else:
            print("Invalid resolution. Please enter a valid resolution.")


# Download the playlist
def print_complete_message(d):
    if d["status"] == "finished":
        print(f"Download complete: {d['filename']}")


def download_playlist(url, download_path, preferred_resolution="1080"):
    ydl_opts = {
        "format": "",
        "outtmpl": os.path.join(
            download_path, "%(playlist)s", "%(playlist_index)s - %(title)s.%(ext)s"
        ),
        "quiet": True,  # Set to True to suppress youtube-dl messages
        "ignoreerrors": True,
        "no_warnings": True,  # Set to True to suppress all warnings
        "progress_hooks": [print_complete_message],
    }
    if preferred_resolution.lower() == "best":
        ydl_opts["format"] = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
    elif preferred_resolution.lower() == "worst":
        ydl_opts["format"] = (
            "worstvideo[ext=mp4]+worstaudio[ext=m4a]/worst[ext=mp4]/worst"
        )
    else:
        ydl_opts["format"] = (
            f"bestvideo[height<={preferred_resolution}][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"
        )
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(e)
        print("An error occurred while downloading the playlist.")
    
    print("Download Playlist has been completed.")

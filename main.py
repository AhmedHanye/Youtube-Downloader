from download import *
from colorama import Fore, Style


def main():
    url = input("Enter the video URL: ")
    check_result = check_url(url)
    if not check_result:
        return
    elif check_result == "video":
        title, formats = get_video_data(url)
        title = sanitize_title(title)
        print("Youtube Video :", Fore.GREEN+title+Style.RESET_ALL)
        type = ask_for_type()
        if type == "video":
            vidoe_f = display_formats(formats)
            if not vidoe_f:
                print(Fore.RED+"Error2: No video formats found!"+Style.RESET_ALL)
                return
            else:
                id, res = ask_for_resolution(formats, vidoe_f)
                path = ask_for_path()
                download_video(url, title, id, res, path)
        elif type == "audio":
            path = ask_for_path()
            download_audio(url, title, path)
        else:
            print(Fore.RED+"Error3: something went wrong!"+Style.RESET_ALL)
            return
    elif check_result == "playlist":
        path = ask_for_path()
        res = ask_for_playlist_res()
        download_playlist(url, path, res)
    else:
        print(Fore.RED+"Error1: something went wrong!"+Style.RESET_ALL)
        return


main()

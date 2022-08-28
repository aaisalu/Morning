from pytube.cli import on_progress
from pytube import Playlist, YouTube
from termcolor import cprint
import helper_func
import colorama
import pytube
import os
import re
import time
import sys

colorama.init()
t1 = time.perf_counter()


def header(url):
    yt = YouTube(url)
    cprint(f"Title: {yt.title} ", 'green')
    cprint(f"Views: {yt.views} Duration:{yt.length}", 'green')
    return yt.title


def mp3(url, save_out):
    try:
        header(url)
        out_file = YouTube(url, on_progress_callback=on_progress).streams.filter(
            only_audio=True).first().download(helper_func.create_folder(rf"Youtube\{save_out}"))
        cprint(":) \n", 'cyan')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    except FileExistsError:
        cprint(f"Looks like {header(url)} music is already present. \n", 'red')


def solo_video(url, save_out):
    header(url)
    pytube.YouTube(url, on_progress_callback=on_progress).streams.get_highest_resolution(
    ).download(helper_func.create_folder(rf"Youtube\{save_out}"))
    cprint(":) \n", 'cyan')


def regex_audio(ask):
    return re.search("audio|mp3|music|flac|wav|aac|ogg|audios", ask, flags=re.IGNORECASE)


def playlists(link, ask):
    playlist = Playlist(link)
    cprint('\nNumber of videos in playlist: %s' %
           len(playlist.video_urls), 'blue')
    if regex_audio(ask):
        cprint("Starting to download MP3s of the videos\n", 'yellow')
        for music_url in playlist.video_urls:
            yt = YouTube(music_url)
            mp3(music_url, f'Audios\{yt.author}')
    else:
        cprint("Starting to download videos in 720p\n", 'yellow')
        for video_url in playlist.video_urls:
            yt = YouTube(video_url)
            solo_video(video_url, f'Videos\{yt.author}')


def askuser(link, ask):
    try:
        if regex_audio(ask):
            cprint("\nStarting to download MP3s of the video", 'yellow')
            mp3(link, "Audios")
        else:
            cprint("\nStarting to download video in 720p", 'yellow')
            solo_video(link, "Videos")
    except pytube.exceptions.RegexMatchError:
        cprint("\nPlease enter a valid server URL!", 'red')


def roulette(link):
    ask = input("Which type do you prefer mp3 or mp4: ")
    try:
        if Playlist(link):
            cprint("Playlist Detected..calling playlist function", 'green')
            return playlists(link, ask)
        else:
            return askuser(link, ask)
    except KeyError:
        return askuser(link, ask)


t2 = time.perf_counter()


def main():
    try:
        roulette(str(input("Enter the link to the Youtube video: ")))
        helper_func.view_file(helper_func.Path)
        cprint(
            f'It took {t2-t1} seconds to download!\n', 'green')
    except (NameError, AttributeError):
        cprint(
            "Some of your input or your network connection looks fishy as my AI smells it..", 'red')
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()

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
from threading import Thread

colorama.init()
t1 = time.perf_counter()


def header(url):
    yt = YouTube(url)
    title = yt.title
    other = f"Views: {yt.views} Duration:{yt.length}"
    return title, other


def mp3(url, save_out, count):
    try:
        titles = f"{count if count else 1}. Title: {header(url)[0]}\n{header(url)[1]}"
        cprint(titles, 'green')
        out_file = YouTube(url, on_progress_callback=on_progress).streams.filter(
            only_audio=True).first().download(helper_func.create_folder(rf"Youtube\{save_out}"))
        cprint(":) \n", 'cyan')
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except pytube.exceptions.LiveStreamError:
        cprint(
            f"Unable to download {header(url)[0]} as it's streaming live..", 'red')
    except pytube.exceptions.VideoUnavailable:
        cprint(f'{header(url)[1]} music is unavailable, skipping.', 'red')
    except FileExistsError:
        cprint(
            f"Looks like {header(url)[0]} music is already present. \n", 'red')


def solo_video(url, save_out, count):
    try:
        titles = f"Title: {header(url)[0]}\n{header(url)[1]}"
        cprint(titles, 'green')
        YouTube(url, on_progress_callback=on_progress).streams.get_highest_resolution(
        ).download(helper_func.create_folder(rf"Youtube\{save_out}"))
        cprint(f":) {count if count else 1} \n", 'cyan')
    except pytube.exceptions.LiveStreamError:
        cprint(
            f"Unable to download {header(url)[0]} as it's streaming live..", 'red')
    except pytube.exceptions.VideoUnavailable:
        cprint(f'{header(url)[0]} Video is unavailable, skipping.', 'red')


def regex_audio(ask):
    return re.search("audio|mp3|music|flac|wav|aac|ogg|audios", ask, flags=re.IGNORECASE)


def playlists(link, ask):
    playlist = Playlist(link)
    cprint('\nNumber of videos in playlist: %s' %
           (final_count := len(playlist.video_urls)), 'blue')
    if regex_audio(ask):
        cprint("Starting to download MP3s of the videos\n", 'yellow')
        for count, music_url in enumerate(playlist.video_urls, start=1):
            yt = YouTube(music_url)
            mp3(music_url, f'Audios\{yt.author}', f'{count}/{final_count}')
    else:
        cprint("Starting to download videos in 720p\n", 'yellow')
        threads=[]
        for count, video_url in enumerate(playlist.video_urls, start=1):
            yt = YouTube(video_url)
            th=Thread(target=solo_video, args=(
                video_url, f'Videos\{yt.author}', f'{count}/{final_count}',))
            threads.append(th)
            th.start()
        for k in threads:
            k.join()

def askuser(link, ask):
    try:
        if regex_audio(ask):
            cprint("\nStarting to download MP3s of the video", 'yellow')
            mp3(link, "Audios", None)
        else:
            cprint("\nStarting to download video in 720p", 'yellow')
            solo_video(link, "Videos", None)
    except pytube.exceptions.RegexMatchError:
        cprint("\nPlease enter a valid server URL!", 'red')
        sys.exit(1)


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
        # cprint(
        #     f'It took {t2-t1} seconds to download!\n', 'green')
    except (NameError, AttributeError):
        cprint(
            "Some of your input or your network connection looks fishy as my AI smells it..", 'red')
    except KeyboardInterrupt:
        print("Exiting from the script....")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()

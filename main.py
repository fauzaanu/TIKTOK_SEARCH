import os
import time
from download import tdownload
from merge import start_merge
from slnm import browsing, sel_search, user_control


def getvideolinks(links):
    # clear the video list
    video_list.clear()

    # tiktok video links has "/video/" in them so filter only those and add them to the video_list global var
    for link in links:
        text = link.get_attribute("href")
        if "/video/" in text:
            video_list.append(text)


if __name__ == "__main__":
    # holds the video list
    video_list = []
    if "media" not in os.listdir():
        os.mkdir("media")
    # ask the user for a search term on TikTok
    query = input("Search term?:\n")
    video_url = f"https://www.tiktok.com/search?q={query}"
    driver = browsing(video_url)

    # pause the program for a while
    user_control()

    # search for the "a" tags
    unfiltered_links = sel_search("a", driver)

    # close driver
    driver.close()

    # valid links added to video_list
    getvideolinks(unfiltered_links)

    # limiting the number of videos we merge
    limit = 3
    downloaded = 0

    # for all videos in the video list download each - rename files to have a random string
    for vid in video_list:
        if downloaded <= limit:
            tdownload(vid, str(int(time.time())))
            downloaded += 1
        else:
            break

    # merge all the downloaded links in the directory to one file
    start_merge("mp4")



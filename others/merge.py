import os
from os import listdir
from moviepy.editor import concatenate_videoclips, VideoFileClip


def start_merge(extention, delete=True):
    # List to store the videofileclip objects for the merge (could we speedup this)
    all_videos = []
    for file in listdir():
        if file.endswith(f".{extention}"):
            print(file)
            filex = VideoFileClip(file)
            all_videos.append(filex)

    final = concatenate_videoclips(all_videos, method='compose')

    final.write_videofile("Composed.mp4")

    if delete:
        delete_except_merge("Composed", "mp4")


def delete_except_merge(name, extention):
    for file in listdir("../media"):
        if file.endswith(f".{extention}"):
            if name not in file:
                os.remove(file)

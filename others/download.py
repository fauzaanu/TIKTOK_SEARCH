import os

import requests


def tdownload(link, name):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
    video_url = link

    page_html = requests.get(video_url, headers=headers)
    main = page_html.content.decode('utf-8')

    startx = main.find('{"url":"')
    # print(startx)
    end = main.find('&mime_type')
    # print(end)

    link = f'{str(main)[startx:end]}'
    link_m = link.replace("u002F", "")
    link_m = link_m.replace('{"url":"', "")
    x = link_m.find("?")
    link_m = link_m[:x]
    link_m = link_m.replace('\\', "/")
    # print(str(link_m))

    link = link.replace('{"url":"', "")

    url = link_m
    downloaded_obj = requests.get(url, headers=headers)

    with open(f"{name}_tok.mp4", "wb") as file:
        file.write(downloaded_obj.content)

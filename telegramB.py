# not working TODO: Make it work but after finding an effective way to beat the captcha
import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler
from download import tdownload
from merge import start_merge, delete_except_merge
from slnm import browsing, sel_search, user_control
from main import getvideolinks

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


# working
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_list = []
    linkx = update.message.text
    # ask the user for a search term on TikTok
    query = linkx
    video_url = f"https://www.tiktok.com/search?q={query}"
    driver = browsing(video_url)

    # pause the program for a while
    user_control()

    # search for the "a" tags
    unfiltered_links = sel_search("a", driver)

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
    start_merge("mp4", delete=False)

    # BAD CODE TODO
    try:
        print("MAIN SEND")
        await context.bot.send_video(chat_id=update.effective_chat.id, video=open("shorts.mp4", 'rb'),
                                     supports_streaming=True,
                                     caption="See what others are watching @MultiMedium", read_timeout=100,
                                     write_timeout=100,
                                     connect_timeout=100)
    except Exception as e:
        print(f"MAIN SEND E{e}")

    delete_except_merge("Composed","mp4")


# working part
async def commd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Send me a query to search tiktok and send you a combined video")


if __name__ == '__main__':
    application = ApplicationBuilder().token('5339027696:AAEiuPlADBx02AUkT2lumz5pPWkYRCb-7hw').build()

    commands = CommandHandler('start', commd)
    links = MessageHandler(filters.TEXT, start)
    # on different commands - answer in Telegram
    application.add_handler(commands)
    application.add_handler(links)

    application.run_polling()

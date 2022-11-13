from aiogram import *
from config import *
from pytube import YouTube

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    chat_id = message.chat.id
    await bot.send_messade(chat_id, "Скачивать видео с Youtube\n"
                                    "Отправь мне ссылку")
    
    

@dp.message_handler()
async def text_message(messsade:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' ar 'https://www.youtube.com/':
        await bot.send_message(chat_id, f"*Начинаю загрузку видео* : *{yt.title}*\n"
                                        f"*С канала *: [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
        await download_youtube_video(url, message,bot)
        
        
async def download_youtube_video(url,message,bot):        
        
        
        
if __name__ == '__main__':
    executor.start_polling(dp)
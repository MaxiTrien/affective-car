import os 

from gtts import gTTS
from playsound import playsound


def feedback(text):
    tts = gTTS(text=text, lang='en')

    filename = "empathic.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)







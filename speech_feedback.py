import os 
import time 
import dataclasses

from gtts import gTTS
from playsound import playsound
from dataclasses import dataclass


@dataclass
class FeedbackSentence:
    angry: str = 'I can understand what you are feeling right now. Do you want to listen to some relaxing music?'
    happy: str = 'You can relax and lean back. I will bring you to your destination safely.'
    sad: str = 'Dont be sad!'
    

def feedback(text):
    tts = gTTS(text=text, lang='en')

    filename = "empathic.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
    
    time.sleep(5)
    
    
    







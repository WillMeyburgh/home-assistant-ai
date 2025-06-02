import io
import tempfile
from pathlib import Path
import speech_recognition
from yapper import Yapper
from google.genai import types
import wave
import pyaudio

from home_assistant_ai.v1.ai import AI

class Speech:
    def __init__(self, ai: AI):
        self.r = speech_recognition.Recognizer()
        self.mic = speech_recognition.Microphone()
        self.ai = ai
        self.yapper = Yapper()

    def __enter__(self):
        self.source = self.mic.__enter__()
        self.r.adjust_for_ambient_noise(self.source)
        return self
    
    def __exit__(self, *args):
        self.source.__exit__(*args)
        
    def listen(self):
        try:
            audio = self.r.listen(self.source, phrase_time_limit = 5)
            text = self.r.recognize_google(audio)
            return text
        except KeyboardInterrupt as e:
            raise e
        except:
            return None

    
    def say(self, text: str):
        self.yapper.yap(text)
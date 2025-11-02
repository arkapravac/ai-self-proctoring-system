import pyttsx
class TTEngine:
    def __init__(self, rate=150):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',rate)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        
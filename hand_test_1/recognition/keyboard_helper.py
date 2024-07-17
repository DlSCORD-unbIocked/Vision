from pynput.keyboard import Key, Controller
import speech_recognition as sr

keyboard = Controller()
r = sr.Recognizer()
r.energy_threshold = 1000

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)


def write_line(text):
    keyboard.type(text)


def query():
    with sr.Microphone() as source:
        print("Say something!")

        audio = r.listen(source, timeout=3)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results"


if __name__ == "__main__":
    text = ""
    while "stop" not in text:
        text = query()
        print(text)

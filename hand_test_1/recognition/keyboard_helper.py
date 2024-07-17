import winsound
from pynput.keyboard import Key, Controller
import speech_recognition as sr
import pyaudio
import threading

keyboard = Controller()
r = sr.Recognizer()
r.energy_threshold = 1000
DEVICE_INDEX = 2
STRING_TO_HOTKEY = {"control": Key.ctrl, "shift": Key.shift, "alt": Key.alt, "space": Key.space, "enter": Key.enter,
                    "delete": Key.delete}


def press_key(key):
    keyboard.press(key)
    keyboard.release(key)


def press_hotkey(hotkeys):
    hotkeys = [x[0] if (x not in STRING_TO_HOTKEY.keys()) else x for x in hotkeys]
    for x in hotkeys:
        key = STRING_TO_HOTKEY.get(x, x)
        keyboard.press(key)

    for x in hotkeys:
        key = STRING_TO_HOTKEY.get(x, x)
        keyboard.release(key)


def write_line(t):
    keyboard.type(t)


def get_devices():
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        print(p.get_device_info_by_index(i))


def query():
    with sr.Microphone(DEVICE_INDEX) as source:
        print("Say something!")
        winsound.Beep(150, 1000)
        audio = r.listen(source)


    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results"


def process_query():
    queried_text = query()
    if queried_text not in ["Could not understand audio", "Could not request results"]:
        if "hotkey" in queried_text:

            press_hotkey([x for x in queried_text.replace("hotkey", " ").split()])

        else:
            write_line(queried_text)


def start_query_thread():
    query_thread = threading.Thread(target=process_query)
    query_thread.start()


if __name__ == "__main__":
    text = ""
    while "hotkey" not in text:
        text = query()

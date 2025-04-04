import speech_recognition as sr
import os
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

def Translate_hindi_to_english(text):
    english_text = translate(text, "en-us")
    return english_text

def Speech_To_Text_Python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.YELLOW + "🎤 Speak something (Hindi)...")
        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                print(Fore.LIGHTBLACK_EX + "Recognizing...", end="\r", flush=True)
                recognizer_text = recognizer.recognize_google(audio, language="hi-IN").lower()

                if recognizer_text:
                    trans_text = Translate_hindi_to_english(recognizer_text)
                    print(Fore.BLUE + "\nNetHyTECH : " + str(trans_text))
                    return trans_text
                else:
                    print(Fore.RED + "No speech detected.")
                    return ""
            except sr.UnknownValueError:
                print(Fore.RED + "Could not understand the audio.")
            except sr.RequestError as e:
                print(Fore.RED + f"API error: {e}")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

Speech_To_Text_Python()

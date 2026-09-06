import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer=sr.Recognizer()
# engine = pyttsx3.init()
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    # engine.delete()
    # engine.stop()
def processCommand(c):
    if "open google" in c.lower():
        speak("opening")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening")
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        speak("opening")
        webbrowser.open("https://facebook.com")




if __name__ == "__main__":
    speak("initialing jarvis...")
    while True:        
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
            word=r.recognize_google(audio)
            print(word)
            if(word.lower()=="jarvis"):
                speak("ya")
            # listen for command
            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                command=r.recognize_google(audio)
                if command.lower() == "exit":
                    speak("goodbye")
                    break
                else:                
                    processCommand(command)

        except Exception as e:
            print("recognize_google error; {0}".format(e))
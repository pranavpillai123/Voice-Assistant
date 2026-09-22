import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
# import client
import ollama
recognizer=sr.Recognizer()
newsapi="your_newsapi_key"
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
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        speak("playing")
        webbrowser.open(link)
    elif "news" in c.lower():
        req=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if req.status_code == 200:
            data = req.json()
            articles=data.get('articles',[])
            speak("Top headlines are:")

            

            for article in articles:
              
                speak(article['title'])
    else:
        # openai
        conversation = [
            {
        'role': 'system',
        'content': (
            "Your name is Jarvis. You are a virtual AI assistant for PC users. "
            "Always provide clear, concise, and correct answers. "
            "Do not use any symbols, bullet points, stars, emojis, or formatting. "
            "Respond in plain text only. Keep answers short but complete."
                )
            }
        ]
        conversation.append({'role': 'user', 'content': c})
        response = ollama.chat(model='llama3', messages=conversation)


        print("working") 
        answer = response['message']['content']
        speak(answer)
        conversation.append({'role': 'assistant', 'content': answer})
        
        





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
                while True:
                        print("Jarvis Active...")
                        audio = r.listen(source,timeout=3,phrase_time_limit=2)
                        command=r.recognize_google(audio)
                        print(command)
                        if(command.lower()=="exit"):
                            speak("goodbye...")
                            break
                        else:
                            processCommand(command)
                            continue

        except Exception as e:
            print("error")
            print("recognize_google error; {0}".format(e))

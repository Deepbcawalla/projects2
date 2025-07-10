import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import gemini_request as ai



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

 # obtain audio from the microphone
def command():

    content=" "
    while content ==" ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio,language='en-in')
            print("you said...." + content)

        except Exception as e:
            print("please try again....")
    return content

def main_process():

    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome, how can i help you.")

        elif "play music"in request:
            speak("playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=c2gSzYLJ8sY&list=RDzZasH6qkn8M&index=3")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=Z8IRRphKFZA&list=RDZ8IRRphKFZA&start_radio=1")
            elif song == 3:
                webbrowser.open("https://youtu.be/knGCfzm4jWs?list=RDknGCfzm4jWs")

        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("current time is" + str( now_time))

        elif "say date" in request:
            now_time = datetime.datetime.now().strftime("%d:%m:%y")
            speak("current date is" + str( now_time))

        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task:"+ task)
                with open("todo.txt","a") as file:
                    file.write(task + "\n")

        elif "speak task" in request:
            with open("todo.txt","r") as file:
             speak("work we have to do today is:" + file.read())

        elif "my work" in request:
             with open("todo.txt","r") as file:
                 tasks = file.read()
             notification.notify(
                 title ="Today's work",
                 message = tasks) 
             
        elif "open youtube" in request:
            webbrowser.open("www.youtube.com")
                   
        elif "open" in request:
            query = request.replace("open","")
            pyautogui.press("super")         # supose window key press simulate
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif " search wikipedia " in request:
            request = request.replace("jarvis", "")
            request = request.replace("search wikipedia","")
            result = wikipedia.summary(request, sentences=2)
            print(result)
            speak(result)

        elif "search google " in request:
            request = request.replace("jarvis", "")
            request = request.replace("search google","")
            webbrowser.open("https://www.google.co.uk/search?q=" + request)

        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+919547115814", "Hi, how are you", 19,18,30)
        
        elif "ask ai" in request:
             request = request.replace("jarvis", "")
             request = request.replace("ask ai", "")
             print(request)
             response = ai.send_request(request)
             print(response)
             speak(response)

        elif "goodbye" in request or "exit" in request or "quit" in request:
            speak("Goodbye! Have a great day!")
            

main_process()




        
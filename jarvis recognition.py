import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import cv2
import requests
# import pywhatkit as kit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# speak("Initialising Jarvis...")
Master="Prakhar Kumar"
speak("Welcome back my master Prakhar Kumar,How are you")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def main():
    speak("Initialising Jarvis")
    wishMe()
    query=takeCommand()
# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.echlo()
#     server.starttls()
#     server.login('youremail@gmail.com','password')
#     server.sendmail('mishra.prakhar309@gmail.com',to,content)
#     server.close()
    if 'wikipedia' in query.lower():
         speak("Searching Wikipedia")
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         print(results)
         speak(results)
    elif 'how are you jarvis' in query.lower():
        speak("I am good sir") 

    elif 'open youtube' in query.lower():
       url="youtube.com"
       chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
       webbrowser.get(chromepath).open(url)

    elif 'open google' in query:
        speak("sir, what should i search on google")
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        url="https://www.google.com//"
        cm=takeCommand().lower()
        webbrowser.get(chromepath).open(f"{cm}") 
        

    elif 'open linkedin' in query.lower():
        url="linkedin.com"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)        
    elif 'music' in query.lower():
        url="https://gaana.com/song/vaaste"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url) 
    elif 'time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")        
        speak(f"{Master} the time is {strTime}")
    elif 'code' in query.lower():
        url="https://colab.research.google.com/drive/1eEqk4p8dfCh4nuk9gYvSZIUXiCSBqnIi#scrollTo=uBmXFUq81Vzo"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)     
    elif 'my website' in query.lower():
        url="https://ucxzhgycdg8hi6glxjtrzg-on.drv.tw/Online%20shoe%20shopping/prakhar1.html"
        chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chromepath).open(url)             
    elif 'open sublime text' in query.lower():
        url="C:\Program Files\Sublime Text 3\sublime_text.exe"
    #chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        os.startfile(url)   
    elif 'search google' in query.lower():
         speak("Searching Google")
         query=query.replace("google","")
         results=wikipedia.summary(query,sentences=2)
         print(results)
         speak(results)
    elif 'open camera' in query.lower():
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            k=cv2.waitKey(200)   
            if k==400:
                break 
            cap.release()
    elif 'open google' in query.lower():
        speak("sir, what should i search on google")
        cm=takeCommand().lower() 
        webbrowser.open(f"{cm}")
    # elif 'send message' in query.lower():
    #     kit.sendwhatmsg("+919973950290","Jarvis in process Sir",2,5)            
            # cv2.destroyAllWindows()
    # elif "ip address" in query:
    #     ip=get('https://api.ipify.org').text
    #     speak("Your ip address is {ip}")
# elif 'email to prakhar' in query.lower():
#     try:
#         speak("what should i send")
#         content=takeCommand()
#         to=mishra.prakhar309@gmail.com
#         sendEmail(to,content) 
#         speak("Email has been sent successfully")
#     except Exception as e:
#         print(e)       
main()


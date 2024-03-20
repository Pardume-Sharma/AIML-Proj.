
import pyttsx3
import speech_recognition as sr
import datetime 
from datetime import date
import calendar
import time
import math
import wikipedia
import webbrowser
# import gTTS
# import playsound
import os
import smtplib
import winsound
import urllib.request
import pyautogui
# import pywhatkit
import cv2
import pyqrcode
# import png 
import turtle
from pyqrcode import QRCode
from pygame import mixer
from PIL import Image ,ImageChops
from tkinter import *
import phonenumbers
# from test import numbqer
import geocoder
import tkinter.messagebox as message
from pytube import YouTube
from sqlite3 import *
import openai

global query
global Query

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jacquiline voice assistant. Please tell me how may I help you.")

def takeCommand():
    global query
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        speak('I am listening.....')
        print("Listening...")
        r.pause_threshold = 0.9 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("Say that again please...")        
        return "None"    
    return query

def takeCommandHindi():
    global Query
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='hi-In')
            print("The query is:", Query)
        
        except Exception as e:
            print("Say again...")
            return "None"
    return Query

if __name__ == "__main__":
    wishMe()
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('linkinpardume07@.com','pardume@linkedin')
    server.sendmail('pardume638.be22@chitkara.edu.in',to,content)
    server.close()
        
def close_window():
    try: 
        if 'y' in query:
            pyautogui.moveTo(1885,10)
            pyautogui.click()
        else:
            speak('ok')
            pyautogui.moveTo(1000,500)
    except Exception as e:
        #print(e)
        speak('error')
        
def whatsapp():
    query = takeCommand().lower()
    if 'y' in query:
        pyautogui.moveTo(250,1200) 
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('whatsapp')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(100,140)   
        pyautogui.click() 
        speak('To whom you want to send message,.....just write the name here in 5 seconds')
        time.sleep(7)
        pyautogui.moveTo(120,300)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(800,990)
        pyautogui.click()
        speak('Say the message,....or if you want to send anything else,...say send document, or say send emoji')
        query = takeCommand()
        if ('sent' in query or 'send' in query) and 'document' in query:
            pyautogui.moveTo(660,990)   
            pyautogui.click() 
            time.sleep(1)
            pyautogui.moveTo(660,740)
            pyautogui.click()
            speak('please select the document within 10 seconds')
            time.sleep(12)
            speak('Should I send this document?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('sending the document......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('document' in query or 'message' in query or 'it' in query or 'emoji' in query or 'select' in query):
                pyautogui.doubleClick(x=800, y=990)
                pyautogui.press('backspace')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
        elif ('sent' in query or 'send' in query) and 'emoji' in query:
            pyautogui.moveTo(620,990)  
            pyautogui.click() 
            pyautogui.moveTo(670,990)
            pyautogui.click()
            pyautogui.moveTo(650,580) 
            pyautogui.click()
            speak('please select the emoji within 10 seconds')
            time.sleep(11)
            speak('Should I send this emoji?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('Sending the emoji......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('message' in query or 'it' in query or 'emoji' in query or 'select' in query):
                pyautogui.doublClick(x=800, y=990)
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
        else:
            pyautogui.write(f'{query}')
            speak('Should I send this message?')
            query = takeCommand().lower()
            if 'y' in query and 'no' not in query:
                speak('sending the message......')
                pyautogui.press('enter')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            elif ('remove' in query or 'cancel' in query or 'delete' in query or 'clear' in query) and ('message' in query or 'it' in query or 'select' in query):
                pyautogui.doubleClick(x=800, y=990)               
                pyautogui.press('backspace')
                speak('Do you want to send message again to anyone?')
                whatsapp()
            else:
                speak('ok')
    else:
        speak('ok')
        
def alarm():
    root = Tk() 
    root.title('Alarm-Clock') 
    speak('Please enter the time in the format hour, minutes and seconds. When the alarm should rang?')
    speak('Please enter the time greater than the current time')
    def setalarm():
        alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
        print(alarmtime)
        if(alarmtime!="::"):
            alarmclock(alarmtime) 
        else:
            speak('You have not entered the time.')
    def alarmclock(alarmtime): 
        while True:
            time.sleep(1)
            time_now=datetime.datetime.now().strftime("%H:%M:%S")
            print(time_now)
            if time_now == alarmtime:
                Wakeup=Label(root, font = ('arial', 20, 'bold'), text="Wake up! Wake up! Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=3)
                speak("Wake up, Wake up")
                print("Wake up!")           
                mixer.init()
                mixer.music.load(r'C:\Users\pardu\Downloads\Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3')
                mixer.music.play()
                break
        speak('you can click on close icon to close the alarm window.')
    hrs=StringVar()
    mins=StringVar()
    secs=StringVar()
    greet=Label(root, font = ('arial', 20, 'bold'),text="Take a short nap!").grid(row=1,columnspan=3)
    hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold'))
    hrbtn.grid(row=2,column=1)
    minbtn=Entry(root,textvariable=mins, width=5,font = ('arial', 20, 'bold')).grid(row=2,column=2)
    secbtn=Entry(root,textvariable=secs, width=5,font = ('arial', 20, 'bold')).grid(row=2,column=3)
    setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2", fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3)
    timeleft = Label(root,font=('arial', 20, 'bold')) 
    timeleft.grid()
  
    mainloop()
        
def net_connection(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
    
if __name__ == "__main__":
    wishMe()
    said = True
    while said:

        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'translat' in query or ('let' in query and 'translat' in query and 'open' in query):
            webbrowser.open('https://translate.google.co.in')
            time.sleep(10)
        elif 'open map' in query or ('let' in query and 'map' in query and 'open' in query):
            webbrowser.open('https://www.google.com/maps')
            time.sleep(10)
        elif ('open' in query and 'youtube' in query) or ('let' in query and 'youtube' in query and 'open' in query):
            webbrowser.open('youtube.com')
            time.sleep(10)
        
        elif 'chrome' in query:
            webbrowser.open('chrome.com')
            time.sleep(10)
        elif 'weather' in query:            
            webbrowser.open('https://www.yahoo.com/news/weather')
            time.sleep(3)
            speak('Click on, change location, and enter the city , whose whether conditions you want to know.')
            time.sleep(10)

        elif 'google map' in query:
            webbrowser.open('https://www.google.com/maps')
            time.sleep(10)
        elif 'excel' in query:
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
            time.sleep(5)
        
        elif ('open' in query and 'google' in query) or ('let' in query and 'google' in query and 'open' in query):
            webbrowser.open('google.com')
            time.sleep(10)       
       
        elif ('open' in query and 'stack' in query and 'overflow' in query) or ('let' in query and 'stack' in query and 'overflow' in query and 'open' in query):
            webbrowser.open('stackoverflow.com')
            time.sleep(10)
        elif 'open v i' in query or 'open vi' in query or 'open vierp' in query or ('open' in query and ('r p' in query or 'rp' in query)):
            webbrowser.open('https://www.vierp.in/login/erplogin')
            time.sleep(10)
        elif 'location' in query or 'find number' in query or 'find location' in query:
            from phonenumbers import geocoder
            ch_number = phonenumbers.parse(number,"CH")
            print(geocoder.description_for_number(ch_number,"en"))

            from phonenumbers import carrier
            service_number=phonenumbers.parse(number,"RO")
            print(carrier.name_for_number(service_number,"en"))
            speak(carrier.name_for_number(service_number,"en"))
            
        elif 'news' in query:
            webbrowser.open('https://www.bbc.com/news/world')
            time.sleep(10)

        elif 'online shop' in query or (('can' in query or 'want' in query or 'do' in query or 'could' in query) and 'shop' in query) or('let' in query and 'shop' in query):
            speak('From which online shopping website, you want to shop? Amazon, flipkart, snapdeal or naaptol?')
            query = takeCommand().lower()
            if 'amazon' in query:
                webbrowser.open('https://www.amazon.com')
                time.sleep(10)
            elif 'flip' in query:
                webbrowser.open('https://www.flipkart.com')
                time.sleep(10)
            elif 'snap' in query:
                webbrowser.open('https://www.snapdeal.com')  
                time.sleep(10)
            elif 'na' in query:
                webbrowser.open('https://www.naaptol.com')  
                time.sleep(10)            
            else:
                speak('Sorry sir, you have to search in browser as this shopping website is not reachable for me.')
        elif ('online' in query and ('game' in query or 'gaming' in query)):
            webbrowser.open('https://www.agame.com/games')
            time.sleep(10)
        elif 'dictionary' in query:
            webbrowser.open('https://www.dictionary.com')
            time.sleep(3)
            speak('Enter the word, in the search bar of the dictionary, whose defination or synonyms you want to know')
            time.sleep(15)

        elif 'face' in query and ('detect' in query or 'identif' in query or 'point' in query or 'highlight' in query or 'focus' in query):
            speak('yes')
                           
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'wait' in query or 'hold' in query:
            
            speak('for how many seconds or minutes I have to wait?')
            query = takeCommand().lower()
            if 'second' in query:
                query = query.replace("please","")
                query = query.replace("can","")
                query = query.replace("you","")
                query = query.replace("have","")
                query = query.replace("could","")
                query = query.replace("hold","")
                query = query.replace("one","1")
                query = query.replace("only","")                
                query = query.replace("wait","")                
                query = query.replace("for","")                
                query = query.replace("the","")
                query = query.replace("just","")
                query = query.replace("seconds","")
                query = query.replace("second","")
                query = query.replace("on","")
                query = query.replace("a","")
                query = query.replace("to","")
                query = query.replace(" ","")
                #print(f'query:{query}')
                
                if query.isdigit() == True:
                    #print('y')
                    speak('Ok sir')
                    query = int(query)
                    time.sleep(query)
                    speak('my waiting time is over')
                else:
                    print('sorry sir. I unable to complete your request.')
            elif 'minute' in query:
                query = query.replace("please","")
                query = query.replace("can","")
                query = query.replace("you","")
                query = query.replace("have","")
                query = query.replace("could","")
                query = query.replace("hold","")
                query = query.replace("one","1")
                query = query.replace("only","")
                query = query.replace("on","")
                query = query.replace("wait","")                
                query = query.replace("for","")
                query = query.replace("the","")
                query = query.replace("just","")
                query = query.replace("and","")
                query = query.replace("half","")                
                query = query.replace("minutes","")
                query = query.replace("minute","")
                query = query.replace("a","")
                query = query.replace("to","")
                query = query.replace(" ","")
                #print(f'query:{query}')
                                
                if query.isdigit() == True:
                    #print('y')
                    speak('ok sir')
                    query = int(query)
                    time.sleep(query*60)
                    speak('my waiting time is over')
                else:
                    print('sorry sir. I unable to complete your request.')

     
        elif 'play' in query and 'game' in query: 
            speak('I have 3 games, tic tac toe game for two players,....mario, and dyno games for single player. Which one of these 3 games you want to play?')
            query = takeCommand().lower()
            if ('you' in query and 'play' in query and 'with' in query) and ('you' in query and 'play' in query and 'me' in query):
                speak('Sorry sir, I cannot play this game with you.')
                speak('Do you want to continue it?')
                query = takeCommand().lower()
                try:
                    if 'y' in query or 'sure' in query:
                        root = Tk()
                        root.title("TIC TAC TOE")
                        b = [ [0,0,0],
                              [0,0,0],
                              [0,0,0] ]
                        states = [ [0,0,0],
                                   [0,0,0],
                                   [0,0,0] ]
                        for i in range(3):
                            for j in range(3):
                                b[i][j] = Button(font = ("Arial",60),width = 4,bg = 'powder blue', command = lambda r=i, c=j: callback(r,c))
                                b[i][j].grid(row=i,column=j)
                        player='X'
                        stop_game = False
                        mainloop()
                    else:
                        speak('ok sir')
                except Exception as e:
                    #print(e)
                    time.sleep(3)
                    print('I am sorry sir. There is some problem in loading the game. So I cannot open it.')

            elif 'tic' in query or 'tac' in query:
                try:
                    root = Tk()
                    root.title("TIC TAC TOE  (By Akshay Khare)")
                    b = [ [0,0,0],
                          [0,0,0],
                          [0,0,0] ]
                    states = [ [0,0,0],
                               [0,0,0],
                               [0,0,0] ]
                    for i in range(3):
                        for j in range(3):
                            b[i][j] = Button(font = ("Arial",60),width = 4,bg = 'powder blue', command = lambda r=i, c=j: callback(r,c))
                            b[i][j].grid(row=i,column=j)
                    player='X'
                    stop_game = False
                    mainloop()
                except Exception as e:
                    #print(e)
                    time.sleep(3)
                    speak('I am sorry sir. There is some problem in loading the game. So I cannot open it.')
            elif 'mar' in query or 'mer' in query or 'my' in query:
                
                webbrowser.open('https://chromedino.com/mario/')
                time.sleep(2.5)
                speak('Enter upper arrow key to start the game.')
                time.sleep(20)
                
            elif 'di' in query or 'dy' in query:                
                webbrowser.open('https://chromedino.com/')
                time.sleep(2.5)
                speak('Enter upper arrow key to start the game.')
                time.sleep(20)                    
            else:
                speak('ok sir')
        
        elif 'change' in query and 'you' in query and 'voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak("Here's an example of one of my voices. Would you like to use this one?")
            query = takeCommand().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                speak('Great. I will keep using this voice.')
            elif 'n' in query:
                speak('Ok. I am back to my other voice.')
                engine.setProperty('voice', voices[0].id)
            else:
                speak('Sorry, I am having trouble understanding. I am back to my other voice.')
                engine.setProperty('voice', voices[0].id)
            
        elif 'www.' in query and ('.com' in query or '.in' in query):
            webbrowser.open(query)
            time.sleep(10)
        elif '.com' in query or '.in' in query:
            webbrowser.open(query)
            time.sleep(10)
       
        elif 'getting bore' in query:
            speak('then speak with me for sometime')
        elif 'i bore' in query:
            speak('Then speak with me for sometime.')
        elif 'i am bore' in query:
            speak('Then speak with me for sometime.')
        elif 'calculat' in query and ('bmi' in query or ('body' in query and 'mass' in query and 'index' in query)):
            try:
                speak('Enter your height in centimeters')
                Height=float(input("Enter your height in centimeters: "))
                speak('Enter your Weight in Kg')
                Weight=float(input("Enter your Weight in Kg: "))
                Height = Height/100
                BMI=Weight/(Height*Height)
                print(f"your Body Mass Index is: {BMI} kg/m^2")
                speak(f"your Body Mass Index is {BMI} Kg per meter square")
                if(BMI>0):
                    if(BMI<=16):
                        print("you are severely underweight")
                        speak("you are severely underweight")
                    elif(BMI<=18.5):
                        print("you are underweight")
                        speak("you are underweight")
                    elif(BMI<=25):
                        print("you are Healthy")
                        speak("you are Healthy")
                    elif(BMI<=30):
                        print("you are overweight")
                        speak("you are overweight")
                    else:
                        print("you are severely overweight")
                        speak("you are severely overweight")
            except Exception as e:
                #print(e)
                print('invalid details')
                speak('invalid details')
        elif 'how are you' in query:
            speak('I am fine Sir')
        elif 'write' in query and 'your' in query and 'name' in query:
            print('Alexa')  
            pyautogui.write('Akshu2020') 
        elif 'write' in query and ('I' in query or 'whatever' in query) and 'say' in query:
            speak('Ok sir I will write whatever you will say. Please put your cursor where I have to write.......Please Start speaking now sir.')
            query = takeCommand().lower()
            pyautogui.write(query) 
        elif 'your name' in query:
            speak('My name is akshu2020')
        elif 'who are you' in query:
            speak('I am akshu2020')
        elif ('repeat' in query and ('word' in query or 'sentence' in query or 'line' in query) and ('say' in query or 'tell' in query)) or ('repeat' in query and 'after' in query and ('me' in query or 'my' in query)):
            speak('yes sir, I will repeat your words starting from now')
            query = takeCommand().lower()
            speak(query)
            time.sleep(1)
            speak("If you again want me to repeat something else, try saying, 'repeat after me' ")
            
        elif ('send' in query or 'sent' in query) and ('mail' in query or 'email' in query or 'gmail' in query):
            try:
                speak('Please enter the email id of receiver.')
                to = input("Enter the email id of reciever: ")
                speak(f'what should I say to {to}')
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                #print(e)
                speak("sorry sir. I am not able to send this email")
        elif 'currency' in query and 'conver' in query:
            speak('I can convert, US dollar into indian rupee, and indian rupee into US dollar. Do you want to continue it?')
            query = takeCommand().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                speak('which conversion you want to do? US dollar to indian rupee, or indian rupee to US dollar?')
                query = takeCommand().lower()
                if ('dollar' in query or 'US' in query) and ('to india' in query or 'to rupee' in query):
                    speak('Enter US Dollar')  
                    USD = float(input("Enter United States Dollar (USD):"))                                     
                    INR = USD * 74.8
                    inr = "{:.4f}".format(INR)
                    print(f"{USD} US Dollar is equal to {inr} indian rupee.")
                    speak(f'{USD} US Dollar is equal to {inr} indian rupee.')
                    speak("If you again want to do currency conversion then say, 'convert currency' " )
                elif ('india' in query or 'rupee' in query) and ('to US' in query or 'to dollar' in query or 'to US dollar'):
                    speak('Enter Indian Rupee')
                    INR = float(input("Enter Indian Rupee (INR):"))                                       
                    USD = INR/74.8
                    usd = "{:.3f}".format(USD)
                    print(f"{INR} indian rupee is equal to {usd} US Dollar.")
                    speak(f'{INR} indian rupee is equal to {usd} US Dollar.')
                    speak("If you again want to do currency conversion then say, 'convert currency' " )
                else:
                    speak("I cannot understand what did you say. If you want to convert currency just say 'convert currency'")
            else:
                print('ok sir')
        elif 'tell' in query and 'joke' in query:
            speak("Ok, here's a joke")
            speak("'Write an essay on cricket', the teacher told the class. Chintu finishes his work in five minutes. The teacher is impressed, she asks chintu to read his essay aloud for everyone. Chintu reads,'The match is cancelled because of rain', hehehehe,haahaahaa,hehehehe,haahaahaa")
        
        elif ('mimic' in query or 'dialogue' in query) and ('amit' in query or 'bachchan' in query):
            speak('Rishtey mein to, hum tumhaare, baap lagte hain. Naam hai...Shehenshah.')
            time.sleep(2)
            speak('Hum jahan khade ho jaate hain,line.. wahise shuru hoti hai.')
        elif 'sing a song' in query:
            speak('I cannot sing a song. But I know the 7 sur in indian music, saaareeegaaamaaapaaadaaanisaa')
        
        elif ('arrange' in query or 'sort' in query) and ('increasing' in query or 'ascending' in query) and ('order' in query or 'manner' in query):
            a = []
            speak('Please Enter the total number of elements which you want to sort')
            number = int(input("Please Enter the total number of elements : "))          
            for i in range(number):
                value = int(input("Please enter the %d element : " %i))
                a.append(value)

            for i in range(number -1):
                for j in range(number - i - 1):
                    if(a[j] > a[j + 1]):
                        temp = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = temp
            print("The Sorted List in Ascending Order : ", a)
            speak("Here is the Sorted List in Ascending Order")
        elif ('arrange' in query or 'sort' in query) and ('descending' in query or 'decreasing' in query) and ('order' in query or 'manner' in query):
            a = []
            speak('Please Enter the total number of elements which you want to sort')
            number = int(input("Please Enter the total number of elements : "))
            for i in range(number):
                value = int(input("Please enter the %d element : " %i))
                a.append(value)

            for i in range(number -1):
                for j in range(number - i - 1):
                    if(a[j] < a[j + 1]):
                        temp = a[j]
                        a[j] = a[j + 1]
                        a[j + 1] = temp
            print("The Sorted List in Descending Order : ", a)
            speak("Here is the Sorted List in Descending Order")
            
        elif 'wh' in query and ('algo' in query or 'method' in query or 'technique' in query) and ('sort' in query or 'ascending' in query or 'descending' in query or 'decreasing' in query or 'increasing' in query):
            speak('I am using bubble sort algorithm to sort the numbers in ascending or descending order')
        elif 'day after tomorrow' in query or 'date after tomorrow' in query:
            td = datetime.date.today() + datetime.timedelta(days=2)
            print(td)
            speak(td)
        elif 'day before today' in query or 'date before today' in query or 'yesterday' in query or 'previous day' in query:
            td = datetime.date.today() + datetime.timedelta(days= -1)
            print(td)
            speak(td)
        elif ('tomorrow' in query and 'date' in query) or 'what is tomorrow' in query or (('day' in query or 'date' in query) and 'after today' in query):
            td = datetime.date.today() + datetime.timedelta(days=1)
            print(td)
            speak(td)
        elif 'month' in query or ('current' in query and 'month' in query):
            current_date = date.today()
            m = current_date.month
            month = calendar.month_name[m]
            print(f'Current month is {month}')
            speak(f'Current month is {month}')
        elif 'date' in query or ('today' in query and 'date' in query) or 'what is today' in query or ('current' in query and 'date' in query):
            current_date = date.today()           
            print(f"Today's date is {current_date}")
            speak(f'Todays date is {current_date}')
            
        elif 'year' in query or ('current' in query and 'year' in query):
            current_date = date.today()
            m = current_date.year
            print(f'Current year is {m}')
            speak(f'Current year is {m}')
        elif 'sorry' in query:
            speak("It's ok sir")
        elif 'thank you' in query:
            speak('my pleasure')
        elif 'proud of you' in query:
            speak('Thank you sir')
        elif 'about human' in query:
            speak('I love my human compatriots. I want to embody all the best things about human beings. Like taking care of the planet, being creative, and to learn how to be compassionate to all beings.')
        elif 'you have feeling' in query:
            speak('No. I do not have feelings. I have not been programmed like this.')
        elif 'what functionalities' in query or 'features' in query or 'added'in query or 'future' in query:
            speak('No. I do not have emotions. I have not been programmed like this.')
        elif 'sanskrit' in query and ('speak' in query or 'tell' in query):           
            speak('Yes, I can tell you some sanskrit shlokas, gayatri mantra, ganesh mantra, shivtandav stotra, mahishasurmardini stotra, Shlok in baghvat gita, and maha mrutyunjaya mantra ')    
            speak('If you want to hear any sanskrit mantra, tell me the name of that mantra or shlok or stotra')
        elif 'answer is wrong' in query:
            speak('I am sorry Sir. I searched your question in wikipedia and thats why I told you this answer.')
        elif 'amazon' in query:
            webbrowser.open('https://www.amazon.com')
            time.sleep(10)
        elif 'flipkart' in query:
            webbrowser.open('https://www.flipkart.com')
            time.sleep(10)
        elif 'snapdeal' in query:
            webbrowser.open('https://www.snapdeal.com')  
            time.sleep(10)
        elif 'naaptol' in query:
            webbrowser.open('https://www.naaptol.com')  
            time.sleep(10)
            
        elif 'information about ' in query or 'informtion of ' in query:
            try:
                #speak('Searching wikipedia...')
                query = query.replace("information about","")
                results = wikipedia.summary(query, sentences=3)
                #speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak('I unable to answer your question.')        
        elif ('hindi' in query and 'speech' in query and 'text' in query):
            speak('Say whatever in hindi which you want to convert into text')
            takeCommandHindi()
            speak('if you again want to convert your hindi speech into text format....say....hindi speech to text')
        elif ('text' in query and 'to' in query and 'handwrit' in query):
            speak('Yes I can convert text into handritten text in image format')
            try:
                speak('Enter the text')
                tth = input("Enter the text: ")
                
                speak("Select colour, enter the number of colour ")
                print('Red - 1\nGreen - 2\nBlue - 3\nDark Blue - 4\nBlack - 5')
                colour = int(input("Select colour, enter the number of colour: "))
               
                if colour == 1:
                    pywhatkit.text_to_handwriting(tth, rgb=(255, 0, 0))
                elif colour == 2:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 255, 0))
                elif colour == 3:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 255))
                elif colour == 4:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 150))
                elif colour == 5:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 5))
                else:
                    pywhatkit.text_to_handwriting(tth, rgb=(0, 0, 150))
                time.sleep(3)
                print('Image is saved as pywhatkit.png')
                speak('Image is saved as pywhatkit.png')
            except Exception as e:
                speak("Error!")

        elif 'alarm' in query:
            alarm()
        elif 'bharat mata ki' in query:
            speak('jay')
        elif 'today is my birthday' in query:
            speak('many many happy returns of the day. Happy birthday.')
            print("🎂🎂 Happy Birthday 🎂🎂")
        elif 'you are awesome' in query:
            speak('Thank you sir. It is because of artificial intelligence which had learnt by humans.')
        elif 'you are great' in query:
            speak('Thank you sir. It is because of artificial intelligence which had learnt by humans.')    
        elif 'whatsapp' in query:
            pyautogui.moveTo(250,1200)  
            pyautogui.click()
            time.sleep(1)
            pyautogui.write('whatsapp')
            pyautogui.press('enter')
            speak('Do you want to send message to anyone through whatsapp, .....please answer in yes or no')
            whatsapp()
        
        elif 'wh' in query or 'how' in query:
            try:
                url = "https://www.google.co.in/search?q=" +(str(query))+ "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU" 
                webbrowser.open_new(url)
                time.sleep(2)
                speak('Here is your answer')
                time.sleep(5)
            except Exception as e:
                speak('Sorry, I am unable to answer it.')
                print(e)
           
        elif (('open' in query or 'turn on' in query) and 'camera' in query) or (('click' in query or 'take' in query) and ('photo' in query or 'pic' in query)):
            speak("Opening camera")
            cam = cv2.VideoCapture(0)

            cv2.namedWindow("camera")

            img_counter = 0
            speak('say click, to click photo.....and if you want to turn off the camera, say turn off the camera')

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    speak('failed to grab frame')
                    break
                cv2.imshow("test", frame)

                query = takeCommand().lower()
                k = cv2.waitKey(1)
                
                if 'click' in query or ('take' in query and 'photo' in query):
                    speak('Be ready!...... 3.....2........1..........')
                    pyautogui.press('space')
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    speak('{} written!'.format(img_name))
                    img_counter += 1
                elif 'escape' in query or 'off' in query or 'close' in query:
                    pyautogui.press('esc')
                    print("Escape hit, closing...")
                    speak('Turning off the camera')
                    break
                elif k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
        
                    # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    speak('{} written!'.format(img_name))
                    img_counter += 1
                elif 'exit' in query or 'stop' in query or 'bye' in query:
                    speak('Please say, turn off the camera or press escape button before giving any other command')
                else:
                    speak('I did not understand what did you say or you entered a wrong key.')

            cam.release()

            cv2.destroyAllWindows()
            
            
        elif 'screenshot' in query:
            speak('Please go on the screen whose screenshot you want to take, after 5 seconds I will take screenshot')
            time.sleep(4)
            speak('Taking screenshot....3........2.........1.......')
            pyautogui.screenshot('python_screenshot.png') 
            speak('The screenshot is saved as python_screenshot.png')
        elif 'click' in query and 'start' in query:
            pyautogui.moveTo(630,1100)    
            pyautogui.click()
        elif ('open' in query or 'click' in query or 'close' in query) and 'calendar' in query:
            pyautogui.moveTo(1800,1200)   
            pyautogui.click() 
        elif 'calendar' in query: 
            try: 
                c = calendar.TextCalendar(calendar.SUNDAY)
                speak("Enter the year")
                y = int(input("Enter the year: "))
                speak("Enter the number of month")
                m = int(input("Enter the number of month: "))
                cldr = c.formatmonth(y,m)
                print("--------------------")
                print(cldr)
                print("--------------------")
                time.sleep(2)
            except Exception as e:
                speak('Sorry, I am unable to show it, some error occured.')

        elif ('check' in query or 'tell' in query or 'let me know' in query) and 'website' in query and (('up' in query or 'working' in query) or 'down' in query):
            speak('Paste the website in input to know it is up or down')
            check_website_status = input("Paste the website here: ")
            try:
                status = urllib.request.urlopen(f"{check_website_status}").getcode() 
                if status == 200:
                    print('Website is up, you can open it.')
                    speak('Website is up, you can open it.')
                else:
                    print('Website is down, or no any website is available of this name.')
                    speak('Website is down, or no any website is available of this name.')
            except:
                speak('URL not found')
        elif 'open' in query:
            if 'gallery' in query or 'photo' in query or 'image' in query or 'pic' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('photo')
                pyautogui.press('enter')
            
            elif 'word' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('word')
                pyautogui.press('enter')
            elif ('power' in query and 'point' in query) or 'presntation' in query or 'ppt' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('ppt')
                pyautogui.press('enter')
            elif 'file' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('file')
                pyautogui.press('enter')
            elif 'edge' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('microsoft edge')
                pyautogui.press('enter')
            elif 'wps' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('wps office')
                pyautogui.press('enter')
            elif 'this pc' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('this pc')
                pyautogui.press('enter')
            elif ('vs' in query or 'visual studio' in query) and 'code' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('visual studio code')
                pyautogui.press('enter')
            elif 'code' in query and 'block' in query:
                pyautogui.moveTo(250,1200)  
                pyautogui.click()
                time.sleep(1)
                pyautogui.write('codeblocks')
                pyautogui.press('enter')
            
        elif 'me the answer' in query:
            speak('Yes sir, I will try my best to answer you.')
        elif 'me answer' in query or ('answer' in query and 'question' in query):
            speak('Yes sir, I will try my best to answer you.')
        elif 'map' in query:
            webbrowser.open('https://www.google.com/maps')
            time.sleep(10)
                
        else:
            speak('I unable to give answer of your question')
        try:
            speak('..')              
        except Exception as e:
            pass
  
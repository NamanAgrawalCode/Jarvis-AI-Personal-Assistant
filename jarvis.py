#This is my trail at buiding a Jarvis Assistant in python
#Copyright imposed. DO NOT COPY
#Do not steal the code
#Credit me everywhere you use this.

import pyttsx3   #pip install pyttsx
'''
if that does not work, try

pip install -U pyttsx3==2.71

pip install -U setuptools

pip install pyaudio

google it
'''
import webbrowser #pip install pycopy-webbrowser
import smtplib #pip install secure-smtplib
import random
import speech_recognition as sr   #pip install speechRecognition
import wikipedia    #pip install wikipedia
import datetime
import wolframalpha   #pip install wolframalpha
import os
import sys

#Your Path may be different
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


#the pyttsx3 module
#pyttsx3 is a tts python module.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

#it should greet me, as I am it's- I mean, His, boss
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!, sir')

    if currentH >= 12 and currentH < 15:
        speak('Good Afternoon!, sir')

    if currentH >= 15 and currentH !=0:
        speak('Good Evening!, sir')

greetMe()

#The assistant will say this everytime it is loaded.
speak('Hello Sir, I am your digital assistant JARVIS')
speak('How may I help you?')


#To make microphone input possible.

def takeCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:   #microphone                                                                   
        print("Listening...")
        
        audio = r.listen(source)
    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')  #it will use google recognize
        print('Boss: ' + query + '\n')
        
#If the J.A.R.V.I.S cannot recognize what the user said, the user can type the command.
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

   
    return query

#A function to send mail
#to make it work, you need to go to your gmail account and turn on access of less secure apps settings
#then replace thee following things with your own email and Password
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Your_Gmail_Account_Email", "Your_Account_Password") #'''Do not worry, your password is safe!'''
    server.sendmail("namanryp@gmail.com", to, content)
    server.close
        

if __name__ == '__main__':

    while True:
    
        query = takeCommand()
        query = query.lower()
        
        
# If what the user says contains "open YouTube", it will open YouTube in chrome
	
        if 'open youtube' in query:
            speak('okay')
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            speak('okay')
            webbrowser.get(chrome_path).open("google.com")

        elif 'open gmail' in query:
            speak("ok")
            webbrowser.get(chrome_path).open("gmail.com")

        elif 'open reddit' in query.lower():
            red = ['Sure, Boss.', 'Sure Thing, Sir.', 'There you go, Master.']
            speak(random.choice(red)) #To keep things interesting, J.A.R.V.I.S, will say either of these things, randomly.
            webbrowser.get(chrome_path).open("reddit.com")

        elif 'open instagram' in query.lower():
            insta = ['Ok, Enjoy.', 'There you go! Sir!', 'Sure. Do not forget to follow! @namanagrawalmememaster', 'as you order, Boss!']
            speak(random.choice(insta))
            webbrowser.get(chrome_path).open("instagram.com")
            
        elif 'open github' in query.lower():
            github = ['Remember, its NamanAgrawalCode', 'become a great coder and create my brothers and sister!' ]
            speak(random.choice(github))
            webbrowser.get(chrome_path).open("github.com")
            
        elif 'open instructables' in query.lower():
            instruct = ['Sure!', 'As you command, my lord', 'not really my thing, but ok.']
            speak(random.choice(instruct))
            webbrowser.get(chrome_path).open("instructables.com")
            
         elif 'open free code camp' in query.lower():
            freecodecamp = ['Sure!', 'Learn Coding Free!', 'The world is in as shocking need of coders! I hope you become one!']
            speak(random.choice(freecodecamp))
            webbrowser.get(chrome_path).open("freecodecamp.org")
                      
         elif 'open wikipedia' in query.lower():
            ww = ['Sure!', 'Ok, Boss.', 'Learn and perish!']
            speak(random.choice(ww))
            webbrowser.get(chrome_path).open("wikipedia.org")
					  
		 elif 'open wolframalpha' in query or 'open w o l f r a m a l p h a' in query.lower():
            wolfram = ['Sure.', 'As you command, My lord.', 'Apka hukum salokho par.']
            speak(random.choice(wolfram))
            webbrowser.get(chrome_path).open("wolframalpha.com")
					  
		elif 'open your code' in query.lower():
            codecode = ['Sorry, but thats a gaurded secret', 'Sorry, but i WONT']
            speak(random.choice(codecode))
            webbrowser.get(chrome_path).open("sorrybutthatsasecretsogetout.com")

	#search wikipedia!
        elif 'search wikipedia' in query.lower():
            speak("Searching wikipedia...")
            query = query.replace("wikipedia search", "")
            speak("How many sentences do you want to know?")
            x = input("")
            results = wikipedia.summary(query, sentences = x)
            speak(results)
            print(results)


        elif "what's up" in query or 'how are you' in query:
            whatsup = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy', "Perfect and ready for use, Boss.", 'Ready to help you!']
            speak(random.choice(whatsup))

		#sending emails!
        elif 'email' in query.lower() :
            try:
                speak("What should I send?")
                content = takeCommand()
                speak("to whom should I send it to?")
                to = input("")
                sendEmail(to, content)
                speak("Email has been send successfully")

            except Exception as e:
                print(e)

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query or 'hi' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query.lower():
            songs_dir = "Your_Songs_Directory"
            songs = os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir, songs[0]))

		#game! (give the directory)
        elif 'game' in query.lower():
            game = "A_Game_Directory"
            
            os.system(game)

        elif 'who created you' in query.lower() :
            speak("Boss, I was created by Naman Agrawal")

        elif 'cure for coronavirus' in query.lower() :
            speak("THERE IS CURRENTLY A CORONAVIRUS OUTBREAK. No cure has been devloped yet, and it is advised to stay at home, always wear a mask and stay safe. You can get more information on the web.")
        elif 'what can you do' in query.lower():
            speak("I can send emails, tell you the time, open sites, search the net.")

        elif 'time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(" Sir, the time is " + strTime)
					  
				elif 'google search' in query:
						query = query.replace(" ", "+")
						speak("Boss, as I can't read it out yet, I am opening it for you.")
						webbrowser.open('www.google.com/search?q=' + query)
			

        elif 'to whom does the credit of making you goes to' in query.lower():
            speak("The Credit of making me goes to many people. Topmost of them being free CodeCamp (and their forum), My creator's family and friends, Python, Wikipedia, pyttsx3, speech_recognition, Google, WolframAlpha, GitHub, the  creator of the game, CodeWithHarry, My creator, etc.,  ")
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    

                    # App id of Wolframalpha
                    '''
                    go to wolframalpha.com, sign up. Then click on your account symbol, and ask for an app id
                    You can always google it up
                    '''
                    app_id = ''

                    # Instance of wolf ram alpha 
                    # client class 
                    client = wolframalpha.Client(app_id) 

                    # Stores the response from 
                    # wolframalpha 
                    res = client.query(query) 

                    # Includes only text from the response 
                    answer = next(res.results).text

                    speak(answer)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com/search?q=' + query)
        
        askingfornextcommand = ['Next Comand, Sir', 'What more do want to do, Sir', 'Next Command, Boss!', 'I am ready for your next wish, Boss.', "What do'ya wanna do, Boss? ", "Ready for ya'next wish, boss.", "Boss, I want to do more!", "At your service, My lord", "Your Wish, My Command.", "Whatever you need! I owe you! Boss!" ]

        speak(random.choice(askingfornextcommand))

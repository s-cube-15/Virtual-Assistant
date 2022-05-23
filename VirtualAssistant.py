import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia 
import webbrowser
import os
import smtplib # Used to send email through gmail

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your virtual assistant. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\nTry Saying 'Sachin Tendulkar Wikipedia'")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Not so clear, say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('amtalreja02@gmail.com', 'aayush@02')
    server.sendmail('amtalreja02@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
       
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open brave' in query:
            webbrowser.open("brave.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir = ''
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me the current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The current time is {strTime}")
            speak(f"The current time is {strTime}")
            

        elif 'open code' in query:
            codePath = "D:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "2020.sudhanshu.sabale@ves.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Success! Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email due to some error")

        if 'exit' in query:
            speak("Goodbye!")
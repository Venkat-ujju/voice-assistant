import speech_recognition as sr
import pyttsx3
import webbrowser
import smtplib
import random
import ssl

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print(" Recognizing....")
        command = recognizer.recognize_google(audio, language="en-in")
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you say it again?")
        return ""
    except Exception as e:
        speak("Something went wrong.")
        print(e)
        return ""
def open_website(command):
    sites = {
        "amazon": "https://www.amazon.in",
        "linkedin": "https://www.linkedin.com",
        "instagram": "https://www.instagram.com",
        "github": "https://www.github.com",
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "my portal": "https://www.codegnan.com",
    }

    for key in sites:
        if key in command:
            speak(f"Opening {key}")
            webbrowser.open(sites[key])
            return
    speak("Sorry, I don't know that site.")

def send_otp_via_email(receiver_email):
    otp = str(random.randint(100000, 999999))
    subject = "Your OTP Code"
    body = f"Your OTP is: {otp}"

    sender_email = "venkatujji.01@gmail.com"  
    sender_password = "tdvj ecda rjvh kyqt"
          
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{body}")
        speak(f"OTP has been sent to {receiver_email}")
    except Exception as e:
        print("Email error:", e)
        speak("Failed to send the OTP.")
def main():
    speak("Hey! I'm your voice assistant. How can I help you today?")

    while True:
        command = take_command()
        if "open" in command:
            open_website(command)
        elif "send otp" in command:
            speak("Please tell me the email address to send OTP to.")
            receiver = input("Enter receiver email: ")
            send_otp_via_email(receiver)
        elif "shutdown" in command or "stop" in command:
            speak("Goodbye!")
            break
        elif command != "":
            speak("Sorry, I don't understand that yet.")
if __name__ == "__main__":
    main()

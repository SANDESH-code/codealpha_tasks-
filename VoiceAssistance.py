import speech_recognition as sr
import pyttsx3

# Create speech recognition and text-to-speech objects
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speaks the given text"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens for user command and returns text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            speak("There was an error with the speech service.")
            return ""

def main():
    """Runs the voice assistant"""
    speak("Hello! How can I assist you?")
    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there! How can I help?")
        elif "your name" in command:
            speak("I am your personal assistant.")
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("Sorry, I don't understand that command.")

# Run the assistant
if __name__ == "__main__":
    main()

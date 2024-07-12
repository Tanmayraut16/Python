import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Set properties before adding anything to speak
    engine.setProperty('rate', 120)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    
    # Use a different voice (optional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Changing index changes voices, 0 for male, 1 for female
    
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    print("Welcome to RoboSpeaker !!!!!")
    while True:
        x = input("Tell me what to Speak: ")
        if x.lower() == 'exit':
            print("GoodBye!!!")
            break
        speak(x)
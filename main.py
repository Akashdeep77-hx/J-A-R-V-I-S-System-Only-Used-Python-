import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
from googlesearch import search as web_search

def recognize_input():
    while True:
        print("Choose input option:")
        print("1. Speech")
        print("2. Text")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # Recognize speech
            recognized_text = recognize_speech()
            if recognized_text:
                return recognized_text
        elif choice == '2':
            # Recognize text input
            text_input = input("Please enter the text: ")
            if text_input:
                return text_input
        elif choice == '3':
            print("Exiting...")
            return None
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")

        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)

        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")
        return None

def search_web(query, num_results=1):
    # Perform a web search using Google
    search_results = web_search(query, num_results=num_results)

    # Create a list to store search results
    results_list = []
    
    # Iterate over the search results and append to the list
    count = 0
    for result in search_results:
        results_list.append(result)
        count += 1
        if count == num_results:
            break
    
    return results_list

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_music(song):
    speak(f"Playing {song} on YouTube.")
    pywhatkit.playonyt(song)

def search_the_web(query):
    search_results = search_web(query, num_results=1)
    if search_results:
        result = search_results[0]
        speak("Here is what I found on the web:")
        speak(result)
        webbrowser.open(result)
    else:
        speak("Sorry, I couldn't find anything related to your query.")

def jarvis():
    speak("Hello! I'm Jarvis. How can I assist you today?")
    while True:
        user_input = recognize_input()
        if user_input is None:
            break

        if "exit" in user_input.lower():
            speak("Goodbye!")
            break
        elif "play" in user_input.lower() and "song" in user_input.lower():
            song = user_input.lower().replace("play", "").replace("song", "").strip()
            play_music(song)
        else:
            search_the_web(user_input)

if __name__ == "__main__":
    jarvis()

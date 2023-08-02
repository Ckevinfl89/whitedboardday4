import pyttsx3
import pyttsx3
engine = pyttsx3.init()

import speech_recognition as sr
import wikipedia
import pyjokes

def ask_question():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Krystal Ask me a question")
        engine.runAndWait()
        audio = recognizer.listen(source)

    try:
        question = recognizer.recognize_google(audio)
        engine.say("You asked: " + question)
        engine.runAndWait()
    except:
        engine.say("I didn't understand your question")
        engine.runAndWait()
        return None
    return question

def tell_joke():
    joke = pyjokes.get_joke()
    engine.say(joke)
    engine.runAndWait()

def main():
    question = ask_question()
    if question is not None:
        if question.startswith("what is"):
            answer = wikipedia.summary(question, sentences=2)
            engine.say(answer)
        elif question.startswith("tell me a joke"):
            tell_joke()
    else:
        engine.say("Goodbye")
        engine.runAndWait()

if __name__ == "__main__":
    main()

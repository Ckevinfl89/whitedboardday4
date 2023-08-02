import pyttsx3
import speech_recognition as sr
import pyjokes
from googlesearch import search

engine = pyttsx3.init()

def ask_question():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("Kevin, ask me a question.")
        engine.runAndWait()
        audio = recognizer.listen(source)

    try:
        question = recognizer.recognize_google(audio)
        engine.say("You asked: " + question)
        engine.runAndWait()
        return question
    except sr.UnknownValueError:
        engine.say("Sorry, I couldn't understand your question.")
    except sr.RequestError:
        engine.say("Sorry, there was an issue connecting to Google Speech Recognition.")
    return None

def get_google_answer(question):
    try:
        search_results = search(question, num_results=1)
        first_result = next(search_results)
        return first_result
    except Exception as e:
        print(f"Error while getting the answer from Google: {e}")
        return None

def tell_joke():
    joke = pyjokes.get_joke()
    engine.say(joke)
    engine.runAndWait()

def main():
    question = ask_question()
    if question:
        if question.lower().startswith("tell me a joke"):
            tell_joke()
        else:
            answer = get_google_answer(question)
            if answer:
                engine.say("Here's what I found on the web: " + answer)
            else:
                engine.say("Sorry, I couldn't find an answer for your question.")
    else:
        engine.say("Goodbye")
    engine.runAndWait()

if __name__ == "__main__":
    main()


# import pyttsx3
# engine = pyttsx3.init()

# import speech_recognition as sr
# import wikipedia
# import pyjokes

# def ask_question():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         engine.say("Krystal Ask me a question")
#         engine.runAndWait()
#         audio = recognizer.listen(source)

#     try:
#         question = recognizer.recognize_google(audio)
#         engine.say("You asked: " + question)
#         engine.runAndWait()
#     except:
#         engine.say("I didn't understand your question")
#         engine.runAndWait()
#         return None
#     return question

# def tell_joke():
#     joke = pyjokes.get_joke()
#     engine.say(joke)
#     engine.runAndWait()

# def main():
#     question = ask_question()
#     if question is not None:
#         if question.startswith("what is"):
#             answer = wikipedia.summary(question, sentences=2)
#             engine.say(answer)
#         elif question.startswith("tell me a joke"):
#             tell_joke()
#     else:
#         engine.say("Goodbye")
#         engine.runAndWait()

# if __name__ == "__main__":
#     main()

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source, duration=0.2)  # Adjusting
    audio = r.listen(source)  # Listening

try:
    MyText = r.recognize_google(audio)  # Recognizing voice
    MyText = MyText.lower()
    print("Recognized Text:")
    print(MyText)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

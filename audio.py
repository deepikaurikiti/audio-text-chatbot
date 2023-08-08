import sys
import speech_recognition as sr
import pyttsx3

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python audio.py")
    sys.exit(1)

file_name = sys.argv[1]

r = sr.Recognizer()

# Audio into text
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source, duration=0.2)  # Adjusting
    audio = r.listen(source)  # Listening

    MyText = r.recognize_google(audio)  # Recognizing voice
    MyText = MyText.lower()

    print(MyText)

# Write the recognized text to the specified file
with open(file_name, 'w') as file:
    file.write(MyText)

print("File written successfully!")

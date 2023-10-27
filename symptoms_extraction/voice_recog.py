import speech_recognition as sr

def listen(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio, language = lang)
        print(f"You: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

    return command

for i in range(1):
    listen('en')
    
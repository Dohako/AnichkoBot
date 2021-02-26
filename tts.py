import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию

tts.setProperty('voice', 'eng') 

# Попробовать установить предпочтительный голос

for voice in voices:

    if voice.name == 'english':

        tts.setProperty('voice', voice.id)

tts.say('Hello there')

tts.runAndWait()
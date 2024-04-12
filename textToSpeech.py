from gtts import gTTS
import os

def generate_text_to_speech(text):
    tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)
    tts.save("output.mp3")
    os.startfile("output.mp3")

def main():
    text = input("Enter text to convert : ")
    generate_text_to_speech(text)

if __name__ == "__main__":
    main()
    
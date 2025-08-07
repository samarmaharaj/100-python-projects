import os
import resemble as resembleai
from gtts import gTTS
from pydub import AudioSegment

# Initialize ResembleAI with your API token
resembleai.api_key = 'nJyWy50A1l6kv1NuQsnDqQtt'

def clone_voice(sample_audio_path, voice_name):
    # Upload voice sample to ResembleAI
    with open(sample_audio_path, 'rb') as audio_file:
        audio_data = audio_file.read()
    
    # Create a new voice with the sample
    response = resembleai.v2.voices.create(name=voice_name, sample=audio_data)
    return response['item']['id']

def generate_speech(voice_id, text, output_path):
    # Generate speech from text using the cloned voice
    response = resembleai.v2.clips.create(voice_id=voice_id, body=text)
    clip_id = response['item']['id']
    
    # Retrieve the audio clip
    clip_response = resembleai.v2.clips.retrieve(voice_id, clip_id)
    audio_url = clip_response['item']['audio_url']
    
    # Download the audio
    audio_data = resembleai.v2.download(audio_url)
    
    # Save to a file
    with open(output_path, 'wb') as audio_file:
        audio_file.write(audio_data)

def main():
    # Clone the voice from a sample audio file
    sample_audio_path = r'C:\Users\samar kumar\Downloads\OSHO-Bharat_Ka_Bhavishya_01.mp3'
    voice_name = 'ClonedVoice'
    cloned_voice_id = clone_voice(sample_audio_path, voice_name)
    
    # Generate speech using the cloned voice
    text = 'Hello, this is a test of the cloned voice.'
    output_path = 'cloned_voice_output.wav'
    generate_speech(cloned_voice_id, text, output_path)
    
    print(f'Speech generated and saved to {output_path}')

if __name__ == '__main__':
    main()

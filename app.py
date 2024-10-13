import os
from google.cloud import speech
import io

# Set up the Google Cloud Credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_creds.json'

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    # Load the audio file
    with io.open(audio_file, 'rb') as audio:
        content = audio.read()

    # Configure the audio and request parameters
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )

    # Send request to the API
    response = client.recognize(config=config, audio=audio)

    # Parse and print the transcription
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

# Example usage
if __name__ == '__main__':
    transcribe_audio('your_audio_file.wav')

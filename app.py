from google.cloud import speech_v1p1beta1 as speech
import os

# Set the environment variable for credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_creds.json'

def transcribe_audio(audio_file):
    client = speech.SpeechClient()

    # Specify audio configuration
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,  # Set encoding to MP3
        sample_rate_hertz=16000,  # Set the correct sample rate of your file
        language_code="en-US",
    )

    # Load the audio file into memory
    with open(audio_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    # Make the request to the Google Speech-to-Text API
    response = client.recognize(config=config, audio=audio)

    # Print the transcription for each result
    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

# Call the function with the MP3 file
transcribe_audio('goodbye.mp3')

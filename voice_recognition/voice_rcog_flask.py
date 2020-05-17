'''
voice recognition module under Flask

reference: https://github.com/GoogleCloudPlatform/python-docs-samples/speech/microphone

'''
from __future__ import division

import re
import sys

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import pyaudio
from six.moves import queue

import microphone.transcribe_streaming_mic as mic

# Use flask for web app
from flask import Flask, render_template, Response
app = Flask(__name__)

def process_voice_recognition():
    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = 'en-US'  # a BCP-47 language tag

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=mic.RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with mic.MicrophoneStream(mic.RATE, mic.CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        #mic.listen_print_loop(responses)
        mic.listen_and_sample_words(responses)

# Initialize for web app
@app.route('/')
def index():
    return render_template('web_app_voice.html')

# Entry point for web app
@app.route('/audio_stream')
def audio_stream():
    return Response(process_voice_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    print("\n\nNote: Open browser and type http://127.0.0.1:5000/ or http://ip_address:5000/ \n\n")
    # Run flask for web app
    app.run(host='0.0.0.0', threaded=True, debug=True)
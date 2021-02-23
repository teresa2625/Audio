import speech_recognition
import time
import os
import pyaudio
import wave


def play_voice(AUDIO_FILE_NAME):
    CHUNK = 1024
    File = wave.open(AUDIO_FILE_NAME, "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(File.getsampwidth()),
                    channels=File.getnchannels(),
                    rate=File.getframerate(),
                    output=True)

    data = File.readframes(CHUNK)
    while data:
        stream.write(data)
        data = File.readframes(CHUNK)
        # stream.stop_stream()
        # stream.close()
        # p.terminate()


def audio_file_to_text(AUDIO_FILE_NAME):
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(AUDIO_FILE_NAME) as source:
        r.adjust_for_ambient_noise(source, duration=0)
        audio = r.record(source)
    text = r.recognize_google(audio, language='en-US')
    return text


def voice_to_text():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("speak")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        # text = r.recognize_google(audio, language='zh-TW')
        # return text
    try:
        text = r.recognize_google(audio, language='zh-TW')
    except r.UnknownValueError:
        text = "no"
    except r.RequestError as e:
        text = "no".format(e)
    return text


outfile = "/Users/teresahuang/Documents/learning/Python/voice.txt"
f1 = open(outfile, 'w', encoding='cp950')

print('a')
AUDIO_FILE_NAME = ("/Users/teresahuang/Documents/learning/Python/voice.wav")
play_voice(AUDIO_FILE_NAME)

print('b')
text = audio_file_to_text(AUDIO_FILE_NAME)
print(text)
f1.write(text)
print('word')
text = voice_to_text()
print(text)
f1.write(text + '\n')
print('\n\n' + outfile + 'ok')
f1.close()

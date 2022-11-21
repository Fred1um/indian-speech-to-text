import requests
from pydub import AudioSegment
import speech_recognition as sr
import pandas as pd
from ai4bharat.transliteration import XlitEngine

data = pd.read_csv('somefile.csv')
data_selected = data  # If you need to resume from some point, just specify start or end point, for ex. data[1000:2000]

lang_codes = {'Bengali': 'bn', 'Hindi': 'hi', 'Kannada': 'kn', 'Punjabi': 'pa', 'Gujarati': 'gu', 'Marathi': 'mr',
              'Tamil': 'ta', 'Oriya': 'or', 'Telugu': 'te', 'Urdu': 'ur', 'Malayalam': 'ml'}

engine = XlitEngine(src_script_type='indic', beam_width=20, rescore=False)


def recognize(audiofile, lang_code):
    global engine
    r = sr.Recognizer()
    with sr.AudioFile(audiofile) as source:
        audio = r.listen(source)
        try:
            # Here we need to specify the language of recognizing
            query = r.recognize_google(audio, language=f'{lang_code}-In')
        except Exception as e:
            print(e)
            return ''
    result = engine.translit_sentence(query, lang_code)
    return result

# Downloading m4a files from links in csv
for i, url in enumerate(range(len(data['file_url']))):  # Here you can also specify start or end point
    myfile = requests.get(url)
    file_name = url.split('/')[-1]
    file_location = f'somepath/{file_name}'
    open(file_location, 'wb').write(myfile.content)

    # Converting m4a to wav
    src = file_location
    dst = f"somepath/{file_name.split('.')[0]}.wav"  # ai4bharat recognition module works with wav and flac extensions
    sound = AudioSegment.from_file(src)
    sound.export(dst, format="wav")

    lang_code = lang_codes[data_selected['lang_name'][i]]
    text = recognize(dst, lang_code)
    data_selected['Recognized_Text'][i] = text

    data.to_csv('somepath', index=False)

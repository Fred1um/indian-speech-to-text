# Indian language recognition and transliterating script

##  Key target
The creation of this project was facilitated by the need to obtain transliterated text from 10,000 audio files of Indian speech in 11 dialects.
Links were stored in a csv file. They had to be downloaded, converted, then speech recognized, and only then received romanized text.

### Packages to install
```bash
pip install SpeechRecognition
pip install ai4bharat-transliteration
```

### Usage
Load the csv file to "data"
```bash
data = pd.read_csv('somefile.csv')
```
Notice, that SpeechRecognition module supports the following file formats:

>WAV

>AIFF/AIFF-C

>FLAC

So if you have files in this format, just comment the converting part 
```bash
src = file_location
dst = f"somepath/{file_name.split('.')[0]}.wav"  # ai4bharat recognition module works with wav and flac extensions
sound = AudioSegment.from_file(src)
sound.export(dst, format="wav")
```
and put the path to your files in "dst" variable.
    

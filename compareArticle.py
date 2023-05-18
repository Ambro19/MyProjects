import requests
import csv
import pyperclip
import nltk
nltk.download('punkt')
from translation import translate, translate_back
from nltk.tokenize import sent_tokenize
#import nltk
#from nltk.download('punkt')
from bleu_score import compare as bleu_compare
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
import PySimpleGUI as sg
import random

# constants and variables
display_trans = {
    "English": ["es", "fr", "de", "it", "ja", "ko", "pt", "ru", "zh-CN"],
    "Spanish": ["en", "fr", "de", "it", "ja", "ko", "pt", "ru", "zh-CN"],
    "French": ["en", "es", "de", "it", "ja", "ko", "pt", "ru", "zh-CN"],
    "German": ["en", "es", "fr", "it", "ja", "ko", "pt", "ru", "zh-CN"],
    "Italian": ["en", "es", "fr", "de", "ja", "ko", "pt", "ru", "zh-CN"],
    "Japanese": ["en", "es", "fr", "de", "it", "ko", "pt", "ru", "zh-CN"],
    "Korean": ["en", "es", "fr", "de", "it", "ja", "pt", "ru", "zh-CN"],
    "Portuguese": ["en", "es", "fr", "de", "it", "ja", "ko", "ru", "zh-CN"],
    "Russian": ["en", "es", "fr", "de", "it", "ja", "ko", "pt", "zh-CN"],
    "Chinese": ["en", "es", "fr", "de", "it", "ja", "ko", "pt", "ru"]
}
lang_eng = ["English", "Spanish", "French", "German", "Italian", "Japanese", "Korean", "Portuguese", "Russian", "Chinese"]
INPUT_BOX_SIZE = (50, 10)
lang = "English"
display = "Wikipedia Article Comparison Tool"

def colors():
    return "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

# GUI layout
lang_selection = [
    [sg.Text("Select Language:"), sg.Combo(lang_eng, default_value=lang, key="-LANG SELECT-", readonly=True, enable_events=True), sg.Button("Select", key="-SELECT LANG-")]
]

welcome = [
    [sg.Text(display, font=("Helvetica", 20), justification='center')]
]

text_entry = [[sg.Text("Comparison Tool"), sg.Radio("BLEU Score", "comparison", default=True, key="-BLEU-"), sg.Radio("Sentence Bert", "comparison", key="-BERT-"), sg.Slider(range=(1,100), default_value=50, size=(20,15), orientation="horizontal", key="-SIMILARITY SLIDER-")],
    [sg.Text("Link to Article"), sg.InputText(default_text="Enter link here", size=INPUT_BOX_SIZE, key="-LINK-"), sg.Text("Language"), sg.Combo(lang_eng, default_value="English", key="-TARGET LANG-", readonly=True)],
    [sg.Text("Source"), sg.Multiline(default_text="", size=INPUT_BOX_SIZE, key="-TEXT 1-"), sg.Text("Target"), sg.Multiline(default_text="", size=INPUT_BOX_SIZE, key="-TEXT 2-")],
]

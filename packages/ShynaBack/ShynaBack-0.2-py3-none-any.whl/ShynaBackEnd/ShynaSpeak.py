from google_speech import Speech
from nltk.tokenize import sent_tokenize
import random

"""
Google speech and NLTK data is the dependency.

Two function as follows:
1) shyna_speaks: require message to speak. Random choice enable.
2) test_shyna_speaks : call to just test if everything is working fine or not.
"""

def shyna_speaks(msg: object) -> object:
    try:
        msgs=random.choice(msg.split("|"))
        for i in sent_tokenize(msgs):
            lang = "en"
            speech = Speech(i, lang)
            sox_effects = ("speed", "1.1999999", )
            speech.play(sox_effects)
    except Exception as e:
        print(e)

def test_shyna_speaks():
    text = "Hey! Shivam?  Test! Test! Are you able to listen me.| can you hear me| hello. test complete?. Not able to listen, is it? I hope speaker volume is up"
    shyna_speaks(text)


import sys
import os
#from aqt.utils import showInfo

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))

from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai
from dotenv import load_dotenv

# words is a string containing the three words to be used in format "'word1', 'word2', 'word3'"
# reserve_list is a string list containing all young and mature words 
def get_sentence(words, reserve_list):

    f = open(os.path.join(os.path.dirname(__file__), ".env"), "r")
    genai.configure(api_key=f.read())

    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    reserve_list2 = str(reserve_list)
    #showInfo(words)
    
    
    response = model.generate_content(
        "Create a sentence that must include the words " + str(words) + ". These words may be anywhere in the sentence an in any order, but must be present. IT MUST BE IN THE LANGUAGE THAT THE GIVEN WORDS ARE IN. Only if you lack the words necessary will you use the wors in the list: " + reserve_list2 + " to create a grammatically correct and easy-to-understand sentence up to 20 words. Avoid unusual or nonsensical combinations of words, and create realistic scenarios that use the required words in a way that make sense. The sentence should be basic and suitable for a beginner. IT MUST BE IN THE LANGUAGE THAT THE GIVEN WORDS ARE IN",          
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }
    )
    return str(response.text) # return ai generated sentence as string

# Translate an input string into English
def translate(sentence):
    
    f = open(os.path.join(os.path.dirname(__file__), ".env"), "r")
    genai.configure(api_key=f.read())

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(
        "Provide the translation of this sentence in English. Only reply with the best translated sentence using your context, no other additional sentences or formatting: " + sentence,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }                                                                  
    )
    return str(response.text) # return translated sentence as string
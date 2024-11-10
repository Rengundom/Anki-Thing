import sys
import os

sys.path.insert(0, "C:/Users/Hot Chocfee/AppData/Roaming/Anki2/addons21/Anki-Thing/lib")

import google.generativeai as genai
from dotenv import load_dotenv

#load env for api key
load_dotenv()

# words is a string containing the three words to be used in format "'word1', 'word2', 'word3'"
# reserve_list is a string list containing all young and mature words 
def get_sentence(words, reserve_list):
    genai.configure(api_key=os.environ.get("api_key"))

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    reserve_list = ", ".join(reserve_list)
    response = model.generate_content(
    "Create a sentence that must include the words " + words + ". These words may be anywhere in the sentence an in any order, but must me present. If possible, construct a Subject-Verb-Object sentence. If a clear SVO sentence cannot be formed, try a Subject-Verb-Adjective sentence. Only if neither of these basic structures works should you add words from this list [" + reserve_list + "] to create a grammatically correct and easy-to-understand sentence up to 20 words. Avoid unusual or nonsensical combinations of words, and create realistic scenarios that use the required words in a way that would make sense even to a person unfamiliar with the English language. The sentence should be basic and suitable for a beginner English learner."               
                                      )
    return str(response.text) # return ai generated sentence as string

# Translate an input string into English
def translate(sentence):
    genai.configure(api_key=os.environ.get("api_key"))

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content("Provide the translation of this sentence in English. Only reply with the best translated sentence using your context, no other additional sentences: " + sentence)
    return str(response.text) # return translated sentence as string
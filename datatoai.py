#import anki
#import json

#global currentWords
#global fillerWords

def fillTheArray(arrayName, idTag):
    try:
        ids = mw.col.find_cards(idTag)
        for id in ids:
            if id not in arrayName:
                arrayName += id
    except:
        pass

def unfillTheArray(arrayName, idTag):
    try:
        unfillCounter=0
        arrayLength = len(arrayName)
        for arrayLength in arrayName:
            if mw.col.get_card_id(arrayName[unfillCounter]) == idTag:
                arrayName.pop(unfillCounter)
                unfillCounter-=1
            unfillCounter+=1
    except:
        pass


def tooMuchStudy():
    global currentWords
    currentWords = []
    global fillerWords
    fillerWords = []
    fillTheArray(currentWords, "tag:learning")
    fillTheArray(currentWords, "tag:relearning")
    fillTheArray(currentWords, "tag:done")
    fillTheArray(currentWords, "tag:mature")
    fillTheArray(fillerWords, "tag:young")
    fillTheArray(fillerWords, "tag:mature")
    unfillTheArray(fillerWords, "is:due")

def senddata(card1, card2, card3):
    sentvalue = str(card1) + ", " + str(card2) + ", " + str(card3)
    return sentvalue

    #card1 = json.loads(card1)
    #card2 = json.loads(card2)
    #card3 = json.loads(card3)
    #return card1, card2, card3
    #return json of everything


# Array is set as global in init? Worried, but idk.
if len(currentWords) == 0:
    tooMuchStudy()
word1 = currentWords[0]
currentWords.pop(0)
if len(currentWords) == 0:
    tooMuchStudy()
word2 = currentWords[0]
currentWords.pop(0)
if len(currentWords) == 0:
    tooMuchStudy()
word3 = currentWords[0]
currentWords.pop(0)



senddata(word1, word2, word3)

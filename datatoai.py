#import anki
#import json


def fillTheArray(idTag):
    temp = []
    try:
        ids = mw.col.find_cards(idTag)
        for id in ids:
            if id not in temp:
                temp.append(id.fields[0])
    except:
        pass
    return temp

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


def tooMuchStudyCurrent():
    toomp = []
    toomp.append(fillTheArray("learning"))
    toomp.append(fillTheArray("relearning"))
    toomp.append(fillTheArray("done"))
    toomp.append(fillTheArray("mature"))
    return toomp

def tooMuchStudyFiller():
    femp = []
    femp += fillTheArray("young")
    femp += fillTheArray("mature")
    unfillTheArray(femp, "is:due")
    return femp


def senddata():
    currentWords = []
    currentWords += tooMuchStudyCurrent()
    word1 = currentWords[0]
    currentWords.pop(0)
    word2 = currentWords[0]
    currentWords.pop(0)
    word3 = currentWords[0]
    currentWords.pop(0)
    return str(f"{word1}, {word2}, {word3}")


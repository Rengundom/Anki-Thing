#import anki
#import json
from aqt.utils import showInfo
from aqt import mw

def fillTheArray(idTag):
    temp = []

    ids = mw.col.find_cards(idTag)
    if len(ids) == 0:
        return ""
    ids.sort(key=lambda card_id: mw.col.get_card(card_id).due)
    #showInfo(f'fillArray find ids of {idTag} {str(ids)}')
    for id in ids:
        card = mw.col.get_card(id)
        temp.append(card.question())
    #showInfo(f'fillArray: {idTag}, {str(temp)}')
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
    toomp += (fillTheArray("is:learn"))
    toomp += (fillTheArray("is:review"))
    #toomp += (fillTheArray("is:new"))
    
    return toomp

def tooMuchStudyFiller():
    femp = []
    femp += fillTheArray("rated:1") #Words already studied that day
    femp += fillTheArray("is:buried") #Words already well known
    unfillTheArray(femp, "prop:due=0") #Function has no return
    
    return femp

current_position = 0

def senddata():
    global current_position
    currentWords = tooMuchStudyCurrent()

    # Check if there are enough cards to proceed
    if len(currentWords) < 3:
        showInfo("Not enough cards to display.")
        return []

    # Get the next three words starting from current_position
    word1 = currentWords[current_position % len(currentWords)]
    word2 = currentWords[(current_position + 1) % len(currentWords)]
    word3 = currentWords[(current_position + 2) % len(currentWords)]
    current_position+=3
    return [word1,word2,word3]


from .GUI_Panels import displaySentence
from .highlight import highlight
from aqt import mw, gui_hooks
from aqt.utils import showInfo, qconnect, QDialog, Qt, QMessageBox, QDesktopServices, QUrl,QPushButton, QLineEdit, QVBoxLayout
from aqt.qt import *
import os


SentenceLearnerEnabled=True

def toggleLearner():
    global SentenceLearnerEnabled
    if(SentenceLearnerEnabled):
        SentenceLearnerEnabled=False
        showInfo(f"The sentence learner is disabled!")
    else:
        SentenceLearnerEnabled=True
        showInfo(f"The sentence learner is enabled!")

def getAPIKey():
    if os.path.exists(os.path.join(os.path.dirname(__file__), ".env")):
       f = open(os.path.join(os.path.dirname(__file__), ".env"), "r")
       showInfo(f.read())
       pass
    else:
        popUp=QDialog()
        popUp.setWindowTitle("You need to enter a Gemini API key:")

        apiKey=QLineEdit()
        apiKey.setPlaceholderText("Enter your Gemini API key here")

        enterButton=QPushButton("Enter")
        enterButton.clicked.connect(popUp.accept)

        layout = QVBoxLayout()
        layout.addWidget(apiKey)
        layout.addWidget(enterButton)
        popUp.setLayout(layout)

        if popUp.exec() == QDialog.DialogCode.Accepted:
            f = open(os.path.join(os.path.dirname(__file__), ".env"), "x")
            f.write(f"api_key={apiKey.text()}")
            
        else:
            getAPIKey()
    

def testFunction(reviewer) -> None:
    if(SentenceLearnerEnabled):
        card = mw.reviewer.card
        note = card.note()
        field_text = note.fields[0]
        QTimer.singleShot(100, lambda:displaySentence(highlight("すごい！あなたはとてもカッコいいだよ！でも、あなたの犬が大嫌いだよ！", ["犬","大嫌い", "カッコいい"])))


# This just makes the typing easier and number of lines nicer.
def fillTheArray(arrayName, idTag):
    try:
        ids = mw.col.find_cards(str(idTag))
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

        
# Rebecca's addition. I'm making a global array so that it can be accessed by a file later.
# That file is going to look at the contents of the array, take three words, and provide them,
# in proper format, to the AI. I'm going to fill the array up here so that it actually only
# gets filled once rather than every single time that the AI pull request requests some words.


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



action = QAction("Toggle the sentence learner", mw)

qconnect(action.triggered, toggleLearner)

mw.form.menuTools.addAction(action)

gui_hooks.main_window_did_init.append(getAPIKey)

gui_hooks.reviewer_did_show_question.append(testFunction)
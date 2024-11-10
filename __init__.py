from .GUI_Panels import displaySentence
from .highlight import highlight
from .llm_calls import get_sentence
from .datatoai import fillTheArray, unfillTheArray, senddata, tooMuchStudyFiller
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
            f.write(apiKey.text())
            
        else:
            getAPIKey()
counter = 0
def testFunction(reviewer) -> None:
    if(SentenceLearnerEnabled):
        global counter
        counter+=1
        theData = senddata()
        if(counter==1):
            QTimer.singleShot(100, lambda:displaySentence(highlight(get_sentence(theData, tooMuchStudyFiller()), theData)))
        elif(counter==3):
            counter=0


# This just makes the typing easier and number of lines nicer.


        
# Rebecca's addition. I'm making a global array so that it can be accessed by a file later.
# That file is going to look at the contents of the array, take three words, and provide them,
# in proper format, to the AI. I'm going to fill the array up here so that it actually only
# gets filled once rather than every single time that the AI pull request requests some words.





action = QAction("Toggle the sentence learner", mw)

qconnect(action.triggered, toggleLearner)

mw.form.menuTools.addAction(action)

gui_hooks.main_window_did_init.append(getAPIKey)

gui_hooks.reviewer_did_show_question.append(testFunction)
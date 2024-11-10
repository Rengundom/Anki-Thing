from aqt import mw, gui_hooks
from aqt.utils import showInfo, qconnect, QDialog, Qt, QMessageBox, QDesktopServices, QUrl, QTextBrowser, QVBoxLayout, QPushButton
from aqt.qt import *
from .llm_calls import translate

def displayTranslate(giventext, popUp, msg_box, reveal_button):
     popUp.setWindowTitle("Translated Sentence:        ")
     msg_box.setHtml(f'<div style="font-size:30px;">{giventext}</div>')
     reveal_button.setText("Continue")
     reveal_button.clicked.disconnect()
     reveal_button.clicked.connect(popUp.accept)

def displaySentence(giventext):
     popUp=QDialog()
     popUp.setWindowTitle("Translate the Sentence:        ")
     msg_box=QTextBrowser()
     msg_box.setHtml(f'<div style="font-size:30px;">{giventext}</div>')

     reveal_button = QPushButton("Reveal", popUp)
     
     layout = QVBoxLayout()
     layout.addWidget(msg_box)
     layout.addWidget(reveal_button)
     popUp.setLayout(layout)
     qconnect(reveal_button.clicked, lambda: displayTranslate(translate(giventext), popUp, msg_box, reveal_button))

     return popUp.exec()
from main import *
from math import floor
import random
import json


QUIZ_QUESTIONS = {
 "French": {
     "Set1": {
         "question": "Translate 'Je suis un garcon.'",
         "options": ["How are you?", "I am boy", "I am a boy"],
         "correctOption": "I am a boy",
     },
     "Set2": {
         "question": "Translate 'Merci'",
         "options": ["Hello", "Thank you", "You're weclome"],
         "correctOption": "Thank you"
     },
    "Set3": {
         "question": "Translate 'Bonne nuit'",
         "options": ["Good evening", "Good night", "Good evening"],
         "correctOption": "Good night"
     },
    "Set4": {
         "question": "Translate 'Le chat et un homme.'",
         "options": ["A man and a cat.", "A cat and a dog.", "A cat and a man."],
         "correctOption": "A cat and a man."
     },
    "Set5": {
         "question": "Translate 'Ceci est un vache.'",
         "options": ["This is a cow.", "This is a yatch.", "This is a ship."],
         "correctOption": "This is a cow."
     },
 },



 "Italian": {
     "Set1": {
         "question": "Translate 'Io sono ragazza.'",
         "options": ["I am girl.", "I am boy.", "I am cat."],
         "correctOption": "I am boy.",
     },
     "Set2": {
         "question": "Translate 'Grazie'",
         "options": ["Grass", "Hello", "Thank you"],
         "correctOption": "Thank you"
     },
    "Set3": {
         "question": "Translate 'Prego'",
         "options": ["Why", "You're welcome.", "Good evening"],
         "correctOption": "You're welcome."
     },
    "Set4": {
         "question": "Translate 'Si, addio'",
         "options": ["No, thank you.", "Yes, hello.", "Yes, goodbye."],
         "correctOption": "A cat and a man."
     },
    "Set5": {
         "question": "Translate 'Questo e un gatto'",
         "options": ["This is a dog.", "This is a cat.", "This is a ship."],
         "correctOption": "This is a cat."
     },
 },


 "Spanish": {
    "Set1": {
         "question": "Translate 'Hola, yo soy espanol.'",
         "options": ["Hello, I know spanish.", "Hello, you are spanish.", "Hello, I am spanish."],
         "correctOption": "Hello, I am spanish.",
     },
     "Set2": {
         "question": "Translate 'Hombre y mujer'",
         "options": ["Man and woman.", "Woman and man.", "Boy and girl."],
         "correctOption": "Man and woman."
     },
    "Set3": {
         "question": "Translate 'Pero'",
         "options": ["Dog", "Cat", "Rat"],
         "correctOption": "Dog"
     },
    "Set4": {
         "question": "Translate 'No, garcias'",
         "options": ["No, hello.", "Yes, hello.", "No, thank you."],
         "correctOption": "No, thank you."
     },
    "Set5": {
         "question": "Translate 'Eso es un perro.'",
         "options": ["This is a dog.", "This is a cow.", "This is a rat."],
         "correctOption": "This is a dog."
     },
 }
}


class QuizHandle(MainWindow):
    
    def setupEvents(self):
        ### Quiz Form Connections
        #########
        ## French
        
        self.ui.QuizButton_French.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, "French"))
        #Submit
        self.ui.FrenchQuizButton_Submit.clicked.connect(lambda: QuizHandle.getCheckedRadioButton(self, "French"))
        #Skip
        ##########

        ##########
        ## Spanish 
        
        self.ui.QuizButton_Spanish.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, "Spanish"))
        #Submit
        self.ui.SpanishQuizButton_Submit.clicked.connect(lambda: QuizHandle.getCheckedRadioButton(self, "Spanish"))
        #Skip
        ##########

        ##########
        ## Italian
        
        self.ui.QuizButton_Italian.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, "Italian"))
        #Submit
        self.ui.ItalianQuizButton_Submit.clicked.connect(lambda: QuizHandle.getCheckedRadioButton(self, "Italian"))
        #Skip
        ##########

        ## NEXT_BTN ##
        self.ui.QuizOutputPage_NextButton.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, self.currentQuizCourse))
        ## SKIP_BTN's ##
        self.ui.FrenchQuizButton_Skip.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, "French"))
        self.ui.SpanishQuizButton_Skip.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, "Spanish"))
        self.ui.ItalianQuizButton_Skip.clicked.connect(lambda: QuizHandle.generateQuestionaire(self, "Italian"))


    
    def generateQuestionaire(self, courseName):
        currentCourse = QUIZ_QUESTIONS[courseName]
        randomKey = random.choice(list(currentCourse))
        randomSet = currentCourse[randomKey]
        questionText = randomSet["question"]
        optionList = randomSet["options"]
        correctOption = randomSet["correctOption"]

        # radioButtons = [self.ui[f"{courseName}QuizRadioButton_1"], self.ui[f"{courseName}QuizRadioButton_2"], self.ui[f"{courseName}QuizRadioButton_3"]]
        radioButtons =  {
            "French": [self.ui.FrenchQuizRadioButton_1, self.ui.FrenchQuizRadioButton_2, self.ui.FrenchQuizRadioButton_3],
            "Spanish": [self.ui.SpanishQuizRadioButton_1, self.ui.SpanishQuizRadioButton_2, self.ui.SpanishQuizRadioButton_3],
            "Italian": [self.ui.ItalianQuizRadioButton_1, self.ui.ItalianQuizRadioButton_2, self.ui.ItalianQuizRadioButton_3],
        }
        self.currentQuizCourse = courseName
        self.currentQuizAnswer = correctOption     

        if courseName == "French":
            # self.ui[f"{courseName}Quiz_QuestionText"].setText(str(questionText))
            self.ui.stackedWidget.setCurrentWidget(self.ui.SubjectFrench_QuizPage)
            self.ui.FrenchQuiz_QuestionText.setText(str(questionText))
            radioButtons["French"][0].setText(str(optionList[0]))
            radioButtons["French"][1].setText(str(optionList[1]))
            radioButtons["French"][2].setText(str(optionList[2]))

        elif courseName == "Spanish":
            self.ui.stackedWidget.setCurrentWidget(self.ui.SubjectSpanish_QuizPage)
            self.ui.SpanishQuiz_QuestionText.setText(str(questionText))
            radioButtons["Spanish"][0].setText(str(optionList[0]))
            radioButtons["Spanish"][1].setText(str(optionList[1]))
            radioButtons["Spanish"][2].setText(str(optionList[2]))

        elif courseName == "Italian":
            self.ui.stackedWidget.setCurrentWidget(self.ui.SubjectItalian_QuizPage)
            self.ui.ItalianQuiz_QuestionText.setText(str(questionText))
            radioButtons["Italian"][0].setText(str(optionList[0]))
            radioButtons["Italian"][1].setText(str(optionList[1]))
            radioButtons["Italian"][2].setText(str(optionList[2]))
          
        print(self.currentQuizAnswer, self.currentQuizCourse)
        
        
    def showOutputPage(self, courseName, status):
        self.ui.stackedWidget.setCurrentWidget(self.ui.QuizOutput_Page)
        if status == "pass":
            self.ui.QuizOutputPage_OutputLabel.setText("<strong>Correct Answer!</strong>")
            self.ui.QuizOutputPage_CorrectAnswer.setText(f"<strong>Answer: </strong> {self.currentQuizAnswer}")

        elif status == "fail":
            self.ui.QuizOutputPage_OutputLabel.setText("<strong>Wrong Answer!</strong>")
            self.ui.QuizOutputPage_CorrectAnswer.setText(f"<strong>Answer: </strong> {self.currentQuizAnswer}")

        QuizHandle.incrementData(status)


    def getCheckedRadioButton(self, courseName):   
        buttons =  {
            "French": [self.ui.FrenchQuizRadioButton_1, self.ui.FrenchQuizRadioButton_2, self.ui.FrenchQuizRadioButton_3],
            "Spanish": [self.ui.SpanishQuizRadioButton_1, self.ui.SpanishQuizRadioButton_2, self.ui.SpanishQuizRadioButton_3],
            "Italian": [self.ui.ItalianQuizRadioButton_1, self.ui.ItalianQuizRadioButton_2, self.ui.ItalianQuizRadioButton_3],
            }
        #buttons = [self.ui[f"{courseName}QuizRadioButton_1"], self.ui[f"{courseName}QuizRadioButton_2"], self.ui[f"{courseName}QuizRadioButton_3"]]
        checkedButton = None
        for button in buttons[courseName]:
            
            if button.isChecked() and button.text() == self.currentQuizAnswer:
                checkedButton = button
                QuizHandle.showOutputPage(self, courseName, "pass")

        if checkedButton == None:
            QuizHandle.showOutputPage(self, courseName, "fail")

    def incrementData(status):
        
        quizStats = open("storage/saves/QuizStats.json", "r")
        jsonToDict = json.load(quizStats)
        print("Json To Dict", jsonToDict)
        print(type(jsonToDict))
        
        if status == "pass":
            jsonToDict["TotalGames"] += 1
            jsonToDict["Wins"] += 1
            

        elif status == "fail":
            jsonToDict["TotalGames"] += 1
            jsonToDict["Loses"] += 1
        
        print(jsonToDict, "after math")
        # dictToJson = json.dumps(jsonToDict)
        print("Dict to Json",  jsonToDict)
        quizStats.close()
        with open('storage/saves/QuizStats.json', 'w') as json_file:
            json.dump(jsonToDict, json_file)
           

    def setQuizData(self):
        quizStats = open("storage/saves/QuizStats.json", "r")
        jsonToDict = json.load(quizStats)
        wins = jsonToDict["Wins"]
        loses = jsonToDict["Loses"]
        self.ui.QuizesDone_Text.setText(str(jsonToDict["TotalGames"]))
        self.ui.QuizesPassed_Txt.setText(str(jsonToDict["Wins"]))
        self.ui.QuizesFails_Txt.setText(str(jsonToDict["Loses"]))
        
        quizStats.close()
        
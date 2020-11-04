from main import *
from math import floor

mainTemplate = {
    "Enrolled"    : [],
    "GamesPlayed" : 0,
    "Wins"        : 1,
    "Loses"       : 1, 
    "Accuracy"    : 0,
}


class courseHandle(MainWindow):
    
    def setupEvents(self):
        ### French:
        ## V Page Event
        self.ui.SubjectButton_French.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.FrenchCoursePage))
        self.ui.SubjectButton_French.clicked.connect(lambda: courseHandle.incrementEnrolledCourses("french")) 
        
        ## V Sub Course Handle: French 
        # Basic 1
        self.ui.Level_Basic1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Basic1_French))
        # Basic 2
        self.ui.Level_Basic2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Basic2_French))

        ## V Sub Course Nav Handle: French
        # Basic 1
        self.ui.Basic1FrenchNavButtonLeft.clicked.connect(lambda: self.ui.Basic1French_StackedWidget.setCurrentIndex(self.ui.Basic1French_StackedWidget.currentIndex() - 1))
        self.ui.Basic1FrenchNavButtonRight.clicked.connect(lambda: self.ui.Basic1French_StackedWidget.setCurrentIndex(self.ui.Basic1French_StackedWidget.currentIndex() + 1))

        # Basic 2
        self.ui.Basic2FrenchNavButtonLeft.clicked.connect(lambda: self.ui.Basic2French_StackedWidget.setCurrentIndex(self.ui.Basic2French_StackedWidget.currentIndex() - 1))
        self.ui.Basic2FrenchNavButtonRight.clicked.connect(lambda: self.ui.Basic2French_StackedWidget.setCurrentIndex(self.ui.Basic2French_StackedWidget.currentIndex() + 1))



        ### Spanish
        ## V Page Event
        self.ui.SubjectButton_Spanish.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SpanishCoursePage))
        self.ui.SubjectButton_Spanish.clicked.connect(lambda: courseHandle.incrementEnrolledCourses("spanish"))
        ## V Sub Course Handle: Spanish
        # Basic 1
        self.ui.Level_Basic1_Spanish.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Basic1_Spanish))
        # Basic 2
        self.ui.Level_Basic2_Spanish.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Basic2_Spanish))

        ## V Sub Course Nav Handle: Spanish
        # Basic 1
        self.ui.Basic1SpanishNavButtonLeft.clicked.connect(lambda: self.ui.Basic1Spanish_StackedWidget.setCurrentIndex(self.ui.Basic1Spanish_StackedWidget.currentIndex() - 1))
        self.ui.Basic1SpanishNavButtonRight.clicked.connect(lambda: self.ui.Basic1Spanish_StackedWidget.setCurrentIndex(self.ui.Basic1Spanish_StackedWidget.currentIndex() + 1))

        # Basic 2
        self.ui.Basic2SpanishNavButtonLeft.clicked.connect(lambda: self.ui.Basic2Spanish_StackedWidget.setCurrentIndex(self.ui.Basic2Spanish_StackedWidget.currentIndex() - 1))
        self.ui.Basic2SpanishNavButtonRight.clicked.connect(lambda: self.ui.Basic2Spanish_StackedWidget.setCurrentIndex(self.ui.Basic2Spanish_StackedWidget.currentIndex() + 1))


        ### Italian 
        self.ui.SubjectButton_Italian.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.ItalianCoursePage))
        self.ui.SubjectButton_Italian.clicked.connect(lambda: courseHandle.incrementEnrolledCourses("italian"))
        ## V Sub Course Handle: Italian
        # Basic 1
        self.ui.Level_Basic1_Italian.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Basic1_Italian))
        # Basic 2
        self.ui.Level_Basic2_Italian.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Basic2_Italian))

        ## V Sub Course Nav Handle: Italian
        # Basic 1
        self.ui.Basic1ItalianNavButtonLeft.clicked.connect(lambda: self.ui.Basic1Italian_StackedWidget.setCurrentIndex(self.ui.Basic1Italian_StackedWidget.currentIndex() - 1))
        self.ui.Basic1ItalianNavButtonRight.clicked.connect(lambda: self.ui.Basic1Italian_StackedWidget.setCurrentIndex(self.ui.Basic1Italian_StackedWidget.currentIndex() + 1))

        # Basic 2
        self.ui.Basic2ItalianNavButtonLeft.clicked.connect(lambda: self.ui.Basic2Italian_StackedWidget.setCurrentIndex(self.ui.Basic2Italian_StackedWidget.currentIndex() - 1))
        self.ui.Basic2ItalianNavButtonRight.clicked.connect(lambda: self.ui.Basic2Italian_StackedWidget.setCurrentIndex(self.ui.Basic2Italian_StackedWidget.currentIndex() + 1))

        

    def getKeyFromDict(key, mode):
        with open(f'storage/saves/{key}.txt', mode) as handle:
            return handle

    def incrementEnrolledCourses(courseName):
        readHandle = open("storage/saves/Enrolled.txt", "r").read().split(";")

        print(readHandle)
        if courseName in readHandle:
            print("no")
            print(courseHandle.getNoOfCourses())
        else: 
            print("yes add")
            courseHandle.appendCourseInFile(courseName)
        # readHandle.close()

    
    def appendCourseInFile(courseName):
        writeHandle = open("storage/saves/Enrolled.txt", "a")
        readHandle  = open("storage/saves/Enrolled.txt", "r")
        writeHandle.write(f";{courseName}")
        writeHandle.close()
        readHandle.close()
                
    
    def getNoOfCourses():
        with open(f'storage/saves/Enrolled.txt', "r+") as handle:
            enrolled = handle.read().split(";")
            count = 0
            for v in enrolled:
                if not v == "":
                    count+=1

            return count







# with open('storage/saves/data.pickle', 'rb') as handle:
#     b = pk.load(handle)
#     print(b["Enrolled"])
#     wins = b["Wins"]
#     loses = b["Loses"]


# print(f"{(floor((wins/loses)*100))}%")




# import pickle as pk
# mainTemplate = {
#     "Enrolled"    : [],
#     "GamesPlayed" : 0,
#     "Wins"        : 1,
#     "Loses"       : 1, 
#     "Accuracy"    : 0,
# }
# with open('storage/saves/data.pickle', 'wb') as handle:
#     pk.dump(mainTemplate, handle)

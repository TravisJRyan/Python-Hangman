"""Program 3 Programmed by Travis Ryan
CS 170 Section 2
Finished on April 24, 2016 at 11:46 AM
Program allows the user to play hangman from an inputted file containing
a list of words."""

from graphics import * #zelle graphics library
from time import * #time necessary for sleep 

def DisplayWindow(window): #main game window
    #aesthetics: greeting texts
    GreetingText = Text( (Point(500, 200)), "Welcome to Hangman! Enter a file name.")
    GreetingText.setSize(30)
    E1 = Entry( (Point(500,500)), 10) 
    E1.setSize(30)
    E1.draw(window)
    GreetingText.draw(window)
    
    #conditions necessary for looping
    condition = False
    othercondition = False
    
    #waiting for a file from user
    while condition == False:
        try:
            window.getMouse()
            filename = E1.getText()
            file = open(filename)
            stringofwords = file.read()
            if stringofwords == "":
                raise FileNotFoundError
            GreetingText.undraw()
            condition = True
            if othercondition == True:
                WrongText.undraw()
        except FileNotFoundError: #file not found exception
            GreetingText.undraw()
            WrongText = Text( (Point(500, 200)), "The file does not exist. Enter another file name.")
            WrongText.setSize(30)
            WrongText.draw(window)
            othercondition = True
    #Initializing necessary variables for game
    wrongCharacters = 0
    rightCharacters = 0
    wrongWords = 0
    rightWords = 0
    timeshung = 0
    listofwords = ExtractData(stringofwords)
    E1.undraw()
    #initialize letters
    #oh god i did these individually
    #this is a monstrosity
    for i in range(len(listofwords)):
        thirdcondition = False
        if thirdcondition == True:
            WrongText.undraw()
        alreadyguessed = []
        #Getting the current word 
        CurrentWord = listofwords[i]
        #Creating 26 Text items.
        blackrectangle = Rectangle( (Point(50,450)), (Point(450,760)) )
        blackrectangle.setFill("black")
        blackrectangle.draw(window)
        letterA = Text( (Point(100, 500)), "A") 
        letterA.setSize(35)
        letterA.setFill("white")
        letterA.draw(window)
        letterB = Text( (Point(150, 500)), "B") 
        letterB.setSize(35)
        letterB.setFill("white")
        letterB.draw(window)
        letterC = Text( (Point(200, 500)), "C") 
        letterC.setSize(35)
        letterC.setFill("white")
        letterC.draw(window)
        letterD = Text( (Point(250, 500)), "D") 
        letterD.setSize(35)
        letterD.setFill("white")
        letterD.draw(window)
        letterE = Text( (Point(300, 500)), "E") 
        letterE.setSize(35)
        letterE.setFill("white")
        letterE.draw(window)
        letterF = Text( (Point(350, 500)), "F") 
        letterF.setSize(35)
        letterF.setFill("white")
        letterF.draw(window)
        letterG = Text( (Point(400, 500)), "G") 
        letterG.setSize(35)
        letterG.setFill("white")
        letterG.draw(window)
        letterH = Text( (Point(100, 570)), "H") 
        letterH.setSize(35)
        letterH.setFill("white")
        letterH.draw(window)
        letterI = Text( (Point(150, 570)), "I") 
        letterI.setSize(35)
        letterI.setFill("white")
        letterI.draw(window)
        letterJ = Text( (Point(200, 570)), "J") 
        letterJ.setSize(35)
        letterJ.setFill("white")
        letterJ.draw(window)
        letterK = Text( (Point(250, 570)), "K") 
        letterK.setSize(35)
        letterK.setFill("white")
        letterK.draw(window)
        letterL = Text( (Point(300, 570)), "L") 
        letterL.setSize(35)
        letterL.setFill("white")
        letterL.draw(window)
        letterM = Text( (Point(350, 570)), "M") 
        letterM.setSize(35)
        letterM.setFill("white")
        letterM.draw(window)
        letterN = Text( (Point(400, 570)), "N") 
        letterN.setSize(35)
        letterN.setFill("white")
        letterN.draw(window)
        letterO = Text( (Point(100, 640)), "O") 
        letterO.setSize(35)
        letterO.setFill("white")
        letterO.draw(window)
        letterP = Text( (Point(150, 640)), "P") 
        letterP.setSize(35)
        letterP.setFill("white")
        letterP.draw(window)
        letterQ = Text( (Point(200, 640)), "Q") 
        letterQ.setSize(35)
        letterQ.setFill("white")
        letterQ.draw(window)
        letterR = Text( (Point(250, 640)), "R") 
        letterR.setSize(35)
        letterR.setFill("white")
        letterR.draw(window)
        letterS = Text( (Point(300, 640)), "S") 
        letterS.setSize(35)
        letterS.setFill("white")
        letterS.draw(window)
        letterT = Text( (Point(350, 640)), "T") 
        letterT.setSize(35)
        letterT.setFill("white")
        letterT.draw(window)
        letterU = Text( (Point(400, 640)), "U") 
        letterU.setSize(35)
        letterU.setFill("white")
        letterU.draw(window)
        letterV = Text( (Point(150, 710)), "V") 
        letterV.setSize(35)
        letterV.setFill("white")
        letterV.draw(window)
        letterW = Text( (Point(200, 710)), "W") 
        letterW.setSize(35)
        letterW.setFill("white")
        letterW.draw(window)
        letterX = Text( (Point(250, 710)), "X") 
        letterX.setSize(35)
        letterX.setFill("white")
        letterX.draw(window)
        letterY = Text( (Point(300, 710)), "Y") 
        letterY.setSize(35)
        letterY.setFill("white")
        letterY.draw(window)
        letterZ = Text( (Point(350, 710)), "Z") 
        letterZ.setSize(35)
        letterZ.setFill("white")
        letterZ.draw(window)
        
        #Creating an entry box and question mark.
        questionmark = Text (Point(50, 250), "?")
        questionmark.setSize(35)
        questionmark.draw(window)
        E2 = Entry ( (Point(550, 250)), 40)
        E2.setSize(30)
        E2.setText("Enter a character or guess the word.")
        E2.draw(window)
        
        #Creating blank spaces the size of the current word.
        wordlength = len(CurrentWord)
        displayedtext = Text ( (Point (500, 100)), (" _" * wordlength) )
        displayedtext.setSize(30)
        displayedtext.draw(window)
        
        #Defining CurrentWrongWord
        CurrentWrongWord = 0
        
        #Defining CurrentWordTry
        CurrentWordTry = True
        
        #Defining HangmanStage
        HangmanStage = 0
        
        #loop through word tries
        while CurrentWordTry == True and CurrentWrongWord < 3 and HangmanStage <6:
            #7Letting the user input a character or word.
            window.getMouse()
            UserChoice = E2.getText()
            #Checking if UserChoice is a word and comparing it with CurrentWord
            if len(UserChoice) > 1:
                if UserChoice.upper() == CurrentWord.upper():
                    CurrentWordTry = False
                    rightWords += 1
                    if thirdcondition == True:
                        newtext.undraw()
                    else:
                        displayedtext.undraw()
                    newtext = Text ( (Point (500, 100)), CurrentWord.upper())
                    newtext.setSize(30)
                    newtext.draw(window)
                    yellowrectangle = Rectangle( (Point(1000,1000)), (Point(450,400)) )
                    yellowrectangle.setFill(color_rgb(249,255,82))
                    yellowrectangle.setWidth(0)
                    yellowrectangle.draw(window)
                    sleep(2)
                    newtext.undraw()
                else:
                    CurrentWrongWord += 1
                    wrongWords += 1
                    if CurrentWrongWord == 3:
                        errormessage = Text( Point(500, 350), "You have used all your word guesses.")
                        errormessage.setSize(30)
                        errormessage.draw(window)
                        sleep(2)
                        errormessage.undraw()
                        
            # Calling the Lookup function
            else:
                #wow this is a tragedy. i will fix this one day
                if Lookup(CurrentWord, UserChoice) == False:
                    HangmanStage += 1
                    wrongCharacters += 1
                    DisplayHangmanStage(HangmanStage, window)
                    if HangmanStage == 6:
                        timeshung += 1
                    if UserChoice == "A" or UserChoice == "a":
                        letterA.setFill("red")
                        letterA.undraw()
                        letterA.draw(window)
                    elif UserChoice == "B" or UserChoice == "b":
                        letterB.setFill("red")
                        letterB.undraw()
                        letterB.draw(window)
                    elif UserChoice == "C" or UserChoice == "c":
                        letterC.setFill("red")
                        letterC.undraw()
                        letterC.draw(window)
                    elif UserChoice == "D" or UserChoice == "d":
                        letterD.setFill("red")
                        letterD.undraw()
                        letterD.draw(window)
                    elif UserChoice == "E" or UserChoice == "e":
                        letterE.setFill("red")
                        letterE.undraw()
                        letterE.draw(window)
                    elif UserChoice == "F" or UserChoice == "f":
                        letterF.setFill("red")
                        letterF.undraw()
                        letterF.draw(window)
                    elif UserChoice == "G" or UserChoice == "g":
                        letterG.setFill("red")
                        letterG.undraw()
                        letterG.draw(window)
                    elif UserChoice == "H" or UserChoice == "h":
                        letterH.setFill("red")
                        letterH.undraw()
                        letterH.draw(window)
                    elif UserChoice == "I" or UserChoice == "i":
                        letterI.setFill("red")
                        letterI.undraw()
                        letterI.draw(window)
                    elif UserChoice == "J" or UserChoice == "j":
                        letterJ.setFill("red")
                        letterJ.undraw()
                        letterJ.draw(window)
                    elif UserChoice == "K" or UserChoice == "k":
                        letterK.setFill("red")
                        letterK.undraw()
                        letterK.draw(window)
                    elif UserChoice == "L" or UserChoice == "l":
                        letterL.setFill("red")
                        letterL.undraw()
                        letterL.draw(window)
                    elif UserChoice == "M" or UserChoice == "m":
                        letterM.setFill("red")
                        letterM.undraw()
                        letterM.draw(window)
                    elif UserChoice == "N" or UserChoice == "n":
                        letterN.setFill("red")
                        letterN.undraw()
                        letterN.draw(window)
                    elif UserChoice == "O" or UserChoice == "o":
                        letterO.setFill("red")
                        letterO.undraw()
                        letterO.draw(window)
                    elif UserChoice == "P" or UserChoice == "p":
                        letterP.setFill("red")
                        letterP.undraw()
                        letterP.draw(window)
                    elif UserChoice == "Q" or UserChoice == "q":
                        letterQ.setFill("red")
                        letterQ.undraw()
                        letterQ.draw(window)
                    elif UserChoice == "R" or UserChoice == "r":
                        letterR.setFill("red")
                        letterR.undraw()
                        letterR.draw(window)
                    elif UserChoice == "S" or UserChoice == "s":
                        letterS.setFill("red")
                        letterS.undraw()
                        letterS.draw(window)
                    elif UserChoice == "T" or UserChoice == "t":
                        letterT.setFill("red")
                        letterT.undraw()
                        letterT.draw(window)
                    elif UserChoice == "U" or UserChoice == "u":
                        letterU.setFill("red")
                        letterU.undraw()
                        letterU.draw(window)
                    elif UserChoice == "V" or UserChoice == "v":
                        letterV.setFill("red")
                        letterV.undraw()
                        letterV.draw(window)
                    elif UserChoice == "W" or UserChoice == "w":
                        letterW.setFill("red")
                        letterW.undraw()
                        letterW.draw(window)
                    elif UserChoice == "X" or UserChoice == "x":
                        letterX.setFill("red")
                        letterX.undraw()
                        letterX.draw(window)
                    elif UserChoice == "Y" or UserChoice == "y":
                        letterY.setFill("red")
                        letterY.undraw()
                        letterY.draw(window)
                    elif UserChoice == "Z" or UserChoice == "z":
                        letterZ.setFill("red")
                        letterZ.undraw()
                        letterZ.draw(window)
                else:
                    rightCharacters += 1
                    if thirdcondition == True:
                        newtext.undraw()
                    else:
                        displayedtext.undraw()
                    alreadyguessed.append(UserChoice.upper())
                    newstring = MakeNewString(CurrentWord, alreadyguessed)
                    newtext = Text ( (Point (500, 100)), newstring )
                    newtext.setSize(30)
                    newtext.draw(window)
                    if "_" not in newstring:
                        CurrentWordTry = False
                        yellowrectangle = Rectangle( (Point(1000,1000)), (Point(450,400)) )
                        yellowrectangle.setFill(color_rgb(249,255,82))
                        yellowrectangle.setWidth(0)
                        yellowrectangle.draw(window)
                        sleep(2)
                    thirdcondition = True #i knew nothing of OOP when i wrote this i swear
                    if UserChoice == "A" or UserChoice == "a":
                        letterA.setFill("green")
                        letterA.undraw()
                        letterA.draw(window)
                    elif UserChoice == "B" or UserChoice == "b":
                        letterB.setFill("green")
                        letterB.undraw()
                        letterB.draw(window)
                    elif UserChoice == "C" or UserChoice == "c":
                        letterC.setFill("green")
                        letterC.undraw()
                        letterC.draw(window)
                    elif UserChoice == "D" or UserChoice == "d":
                        letterD.setFill("green")
                        letterD.undraw()
                        letterD.draw(window)
                    elif UserChoice == "E" or UserChoice == "e":
                        letterE.setFill("green")
                        letterE.undraw()
                        letterE.draw(window)
                    elif UserChoice == "F" or UserChoice == "f":
                        letterF.setFill("green")
                        letterF.undraw()
                        letterF.draw(window)
                    elif UserChoice == "G" or UserChoice == "g":
                        letterG.setFill("green")
                        letterG.undraw()
                        letterG.draw(window)
                    elif UserChoice == "H" or UserChoice == "h":
                        letterH.setFill("green")
                        letterH.undraw()
                        letterH.draw(window)
                    elif UserChoice == "I" or UserChoice == "i":
                        letterI.setFill("green")
                        letterI.undraw()
                        letterI.draw(window)
                    elif UserChoice == "J" or UserChoice == "j":
                        letterJ.setFill("green")
                        letterJ.undraw()
                        letterJ.draw(window)
                    elif UserChoice == "K" or UserChoice == "k":
                        letterK.setFill("green")
                        letterK.undraw()
                        letterK.draw(window)
                    elif UserChoice == "L" or UserChoice == "l":
                        letterL.setFill("green")
                        letterL.undraw()
                        letterL.draw(window)
                    elif UserChoice == "M" or UserChoice == "m":
                        letterM.setFill("green")
                        letterM.undraw()
                        letterM.draw(window)
                    elif UserChoice == "O" or UserChoice == "o":
                        letterO.setFill("green")
                        letterO.undraw()
                        letterO.draw(window)
                    elif UserChoice == "P" or UserChoice == "p":
                        letterP.setFill("green")
                        letterP.undraw()
                        letterP.draw(window)
                    elif UserChoice == "Q" or UserChoice == "q":
                        letterQ.setFill("green")
                        letterQ.undraw()
                        letterQ.draw(window)
                    elif UserChoice == "R" or UserChoice == "r":
                        letterR.setFill("green")
                        letterR.undraw()
                        letterR.draw(window)
                    elif UserChoice == "S" or UserChoice == "s":
                        letterS.setFill("green")
                        letterS.undraw()
                        letterS.draw(window)
                    elif UserChoice == "T" or UserChoice == "t":
                        letterT.setFill("green")
                        letterT.undraw()
                        letterT.draw(window)
                    elif UserChoice == "U" or UserChoice == "u":
                        letterU.setFill("green")
                        letterU.undraw()
                        letterU.draw(window)
                    elif UserChoice == "V" or UserChoice == "v":
                        letterV.setFill("green")
                        letterV.undraw()
                        letterV.draw(window)
                    elif UserChoice == "W" or UserChoice == "w":
                        letterW.setFill("green")
                        letterW.undraw()
                        letterW.draw(window)
                    elif UserChoice == "X" or UserChoice == "x":
                        letterX.setFill("green")
                        letterX.undraw()
                        letterX.draw(window)
                    elif UserChoice == "Y" or UserChoice == "y":
                        letterY.setFill("green")
                        letterY.undraw()
                        letterY.draw(window)
                    elif UserChoice == "Z" or UserChoice == "z":
                        letterZ.setFill("green")
                        letterZ.undraw()
                        letterZ.draw(window)
            E2.setText("")
        if thirdcondition == True:
            newtext.undraw()
        else:
            displayedtext.undraw()
        E2.undraw()
    #Clearing the screen and displaying statistics
    closingyellowrectangle = Rectangle( (Point(0,0)), (Point(1000,1000)))
    closingyellowrectangle.setFill(color_rgb(249,255,82))
    closingyellowrectangle.setWidth(0)
    closingyellowrectangle.draw(window)
    E2.undraw()
    rightstring1 = ("Right Character Guesses: "+str(rightCharacters))
    wrongstring1 = ("Wrong Character Guesses: "+str(wrongCharacters))
    rightstring2 = ("Right Word Guesses: "+str(rightWords))
    wrongstring2 = ("Wrong Word Guesses: "+str(wrongWords))
    hungstring = ("Times Hung: "+str(timeshung))
    rightText1 = Text( (Point(500, 300)), rightstring1)
    rightText1.setSize(30)
    rightText1.draw(window)
    wrongText1 = Text( (Point(500, 450)), wrongstring1)
    wrongText1.setSize(30)
    wrongText1.draw(window)
    rightText2 = Text( (Point(500, 600)), rightstring2)
    rightText2.setSize(30)
    rightText2.draw(window)
    wrongText2 = Text( (Point(500, 750)), wrongstring2)
    wrongText2.setSize(30)
    wrongText2.draw(window)
    hungText = Text ( (Point(500, 900)), hungstring)
    hungText.setSize(30)
    hungText.draw(window)
    resultsText = Text(Point(500, 150), "Results")
    resultsText.setSize(30)
    resultsText.draw(window)
    #9. Getting a mouse click to end the game.
    window.getMouse()
    window.close()

    #return list of strings
def ExtractData(stringofwords):
    #Splitting the string of words into a list
    mylist = stringofwords.split()
    return mylist

    #lookup function checks if character is in word
def Lookup(word, character):
    mylist = []
    wordupper = word.upper()
    characterupper = character.upper()
    if characterupper not in wordupper:
        return False

    #makes a new string for display on screen based on guessed letters
def MakeNewString(word, alreadyguessed):
    newstring = ""
    for i in range(len(word)):
        if word[i].upper() in alreadyguessed:
            newstring+=(" "+word[i].upper())
        else:
            newstring+=(" _")
    return newstring

    #update hangman image on screen
def DisplayHangmanStage(stage, window):
    if stage == 1:
        stage1 = Image( (Point(725, 715)), "Stage1.gif" )
        stage1.draw(window)
    elif stage == 2:
        stage2 = Image( (Point(725, 715)), "Stage2.gif" )
        stage2.draw(window)
    elif stage == 3:
        stage3 = Image( (Point(725, 715)), "Stage3.gif" )
        stage3.draw(window)
    elif stage == 4:
        stage4 = Image( (Point(725, 715)), "Stage4.gif" )
        stage4.draw(window)
    elif stage == 5:
        stage5 = Image( (Point(725, 715)), "Stage5.gif" )
        stage5.draw(window)
    elif stage == 6:
        stage6 = Image( (Point(725, 715)), "Stage6.gif" )
        stage6.draw(window)
        sleep(2)
        yellowrectangle = Rectangle( (Point(1000,1000)), (Point(450,400)) )
        yellowrectangle.setFill(color_rgb(249,255,82))
        yellowrectangle.setWidth(0)
        yellowrectangle.draw(window)
    
    #main function calls game window
def main():
    #Creating the graphics window.
    window = GraphWin("Hangman Program",1000,1000)
    window.setBackground(color_rgb(249,255,82))
    #Displaying the window via the DisplayWindow function.
    DisplayWindow(window)
    
main()

#I sincerely apologize for this code. It was my first project and I will fix it one day.

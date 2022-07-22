'''
test_triword.py

This is an early prototype of the triword gameplay.
Testing: checking user input and displaying result
Limitations: only implementing user view of incorrect and
correct letters in alphabetical order

'''
# NOTE:
# order of the words in the array is very important
# left side of triangle: 1st word
# right side of triangle: 2nd word
# base of triangle: 3rd word

class test_triword:
    # test triword set of words
    words = ["farm", "fake", "mice"]

    # initialize instance of test_triword
    def __init__():
        this.incorrectLetters = [] # incorrect letters guessed
        this.correctLetters = [] # correct letters guessed
        printState()

    '''
    Function: checkWord()
    Params: None
    Returns: Boolean
    Scope: Checks user input if it matches any of words in the set.
    '''
    def checkWord(input):
        pass

    '''
    Function: updateCorrectLetters()
    Params: None
    Returns: None
    Scope:
    '''
    def updateCorrectLetters():
        pass

    '''
    Function: updateCorrectLetters()
    Params: None
    Returns: None
    Scope:
    '''
    def updateIncorrectLetters():
        pass

    '''
    Function: printState()
    Params: None
    Returns: None
    Scope: Shows user the state of the game, including
    incorrectly and correctly guessed letters. Is called after each guess.
    '''
    def printState():
        print("C _ _ E \nC _ _ Y \nE _ _ Y\n"
        pass

    '''
    Function: getUserGuess()
    Params: None
    Returns: None
    Scope: Gets user input, validates it and updates appropriate arrays.
    '''
    def getUserGuess():
        printState()
        pass

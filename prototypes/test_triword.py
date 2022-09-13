'''
test_triword.py

This is an early prototype of the triword gameplay.
Testing: checking user input and displaying result.
Limitations: only implementing user view of incorrect and
correct letters in alphabetical order.
Next steps: add limited number of tries.

Notes: use a dictionary to keep track of all letters found in words
search time would only be in O(n) at the very worst


'''
# NOTE:
# order of the words in the array is very important
# left side of triangle: 1st word
# right side of triangle: 2nd word
# base of triangle: 3rd word
# 1st and last letters of each word are given

class test_triword:
    # test triword set of words
    answer = ["farm", "fake", "mice"]

    # state of guesses by user
    state = []

    # state of the game; will be true when game is complete
    gameOver = false
    # initialize instance of test_triword
    def __init__():
        this.incorrectLetters = [] # incorrect letters guessed
        this.correctLetters = [] # correct letters guessed

        # game gives the 1st and last letter of each word
        # update the state
        for i in range(len(answer)):
            splitWord = answer[i].split()
            # zeroes are used to denote empty spots
            state.append("{} 0 0 {}".format(answer[0], answer[3]))

        printState()

    '''
    Function: updateState()
    Params: None
    Updates the state of the game.
    '''
    def updateState():
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
    Converts the state array to a string for easy printing.
    Returns result as a string.
    '''
    def convertStateArrayToString() -> str:

    '''
    Function: printState()
    Params: None
    Returns: None
    Scope: Shows user the state of the game, including
    incorrectly and correctly guessed letters. Is called after each guess.
    '''
    def printState():
        k = 0
        rows = 4 # need 4 rows for 4-letter words

        for i in range (1, rows + 1):
            for space in range (1, (rows - i) + 1):
                print(end = "  ")

        while k != (2*i - 1):
            print("* ", end = "")
            k += 1

        print()

        print("C _ _ E \nC _ _ Y \nE _ _ Y\n")
        pass
    '''
    Function: validateUserInput()
    Params: (str) input
    Returns: boolean
    Scope: checks if user input is valid, based on 2 conditions:
    (1) Must only contain letters
    (2) Must be 4 letters long
    '''
    def validateUserInput(input) -> bool:
        if (input.isalpha() == True and len(input) == 4):
            return True
        return False

    '''
    Function: getUserGuess()
    Params: None
    Returns: None
    Scope: Gets user input, validates it and updates appropriate arrays.
    '''
    def getUserGuess():
        # game is ongoing until the gameOver == True (i.e. user has
        # correctly guessed all the words)
        while (gameOver == False):
            # get user input and validate it
            valid = False
            while (valid != True):
                guess = input("Type in your guess: ").upper().strip()
                valid = validateUserInput(guess)

            # check if user input is correct
            updateIncorrectLetters()
            # print state for user
            printState()
            pass

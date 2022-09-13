def validateUserInput(input) -> bool:
    if (input.isalpha() == True and len(input) == 4):
        return True
    return False

def getUserGuess():
    valid = False
    while (valid != True):
        guess = input("Type in your guess: ").upper().strip()
        valid = validateUserInput(guess)
    return

getUserGuess()

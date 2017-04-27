def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    total = 0.0
    k = start
    while(k<stop):
        total += step * f(k)
        k = k + step


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result = result + letter
        else:
            result = result + '_'
    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lettersLeft = string.ascii_lowercase
    for letter in lettersGuessed:
        lettersLeft = lettersLeft.replace(letter,'')
    return lettersLeft


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-----------"

    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessesLeft = 8
    while guessesLeft > 0:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print "-----------"
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            availableLetters = availableLetters.replace(letter,"")
            print "-----------"
            if isWordGuessed(secretWord, lettersGuessed) == True:
             print "Congratulations, you won!"
             break
        else:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guessesLeft = guessesLeft - 1
            lettersGuessed.append(letter)
            availableLetters = availableLetters.replace(letter,"")
            print "-----------"
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-----------"

    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessesLeft = 8
    while guessesLeft > 0:
        print "You have " + str(guessesLeft) + " guesses left."
        print "Available letters: " + availableLetters
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        if letter in lettersGuessed:
            print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            print "-----------"
        elif letter in secretWord:
            lettersGuessed.append(letter)
            print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
            availableLetters = availableLetters.replace(letter,"")
            print "-----------"
            if isWordGuessed(secretWord, lettersGuessed) == True:
             print "Congratulations, you won!"
             break
        else:
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
            guessesLeft = guessesLeft - 1
            lettersGuessed.append(letter)
            availableLetters = availableLetters.replace(letter,"")
            print "-----------"
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."




















def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    import string
    assert type(shift) is int and 0 <= shift < 26
    dict = {}
    for i in range(len(string.ascii_lowercase)):
        cypher = (i + shift)%26
        plain = i%26
        cyphertext = string.ascii_lowercase[cypher]
        plaintext = string.ascii_lowercase[plain]
        dict[plaintext] = cyphertext
        dict[plaintext.upper()] = cyphertext.upper()     
    return dict


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    import string
    assert type(text) == str
    cyphertext = ''
    for char in text:
        if char in string.punctuation or char == ' ' or char.isdigit():
            cyphertext += char
        else:
            cyphertext += coder[char]
    return cyphertext 


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    coder = buildCoder(shift)
    return applyCoder(text, coder)


def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    realWords = 0
    bestShift = 0
    for i in range(26):
        shiftedText = applyShift(text, i)
        separated = shiftedText.split(' ')
        validWords = 0
        for word in separated:
            if isWord(wordList, word):
                validWords += 1
        if validWords > realWords:
            realWords = validWords
            bestShift = i
    return bestShift 


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    text = getStoryString()
    wordList = loadWords()
    shift = findBestShift(wordList, text)
    return applyShift(text, shift)











































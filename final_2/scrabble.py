def canMakeWord(letters,word):
    letters = list(letters)
    for x in word:
        if x in letters:
            letters.remove(x)
        else:
            return False
    return True


def withWild(letters,word):
    letters = list(letters)
    for x in word:
        if x in letters:
            letters.remove(x)
        elif '?' in letters:
            letters.remove('?')
        else:
            return False
    return True


def countPlurals(words):
    return len([x for x in words.split() if x[-1].lower() == 's'])


def notPossessive(words):
    return len([w for w in words.split() if w[-1].upper() == 'S' 
                and w[-2] != "'"])



print(countPlurals("These AppleS are Great so are Blueberries"))
print(notPossessive("bananas oranges apple's grapes kiwi's"))
print(countPlurals("computers science tests ares hards"))
print(notPossessive("hows hunter's sceince's finals"))
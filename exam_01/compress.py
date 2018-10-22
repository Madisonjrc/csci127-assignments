import random
list=["Halloween", "special","apple"]
def compress_word(w):
    l = ''
    for i in w.lower():
        if i not in 'aeiou': #or "AEIOU":
            l += i.lower()
    return l

print(compress_word("Halloween"))
print(compress_word("Apple"))
print(compress_word("special"))


def sentence(line):
    nl = []
    for x in line.split():
        nl.append(compress_word(x))
    return ' '.join(nl)

print(sentence("I like to eat apple pie"))
print(sentence("who is there"))
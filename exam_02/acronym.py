def makeacronym(w):
    return ''.join([x[0] for x in w.split()])
print(makeacronym('laughing out loud'))
print(makeacronym('be right back'))
print(makeacronym('cOMPuter SCience'))
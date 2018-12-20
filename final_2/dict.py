def addline(d,line):
    line = line.lower()
    x = line[0]
    if x in d.keys():
        d[x].append(line)
    else:
        d[x] = [line]
    return d


def spellcheck(d, word):
    word = word.lower()
    x = word[0]
    
    if x in d.keys():
        if word in d[x]:
            return True
    return False

d = {}
inputs = ['science','test','computer','final','friend']
for i in inputs:
    d = addline(d,i)
    
print('Dictionary:\n',d)
print(spellcheck(d,"word"))
print(spellcheck(d,"computers"))
print(spellcheck(d,"science"))
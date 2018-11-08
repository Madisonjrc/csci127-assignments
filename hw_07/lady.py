def happy_ladybugs(b):
    if '_' in b:
        b=b.replace('_',"")
        count={}
        for i in b:
            count.setdefault(i,0)
            count[i] += 1
        for i in count.values():
            if i < 2:
                return 'no'
        
        return 'yes'
    elif is_full(b):
        return 'yes'
    else:
        return 'no'

    
    
def is_full(b):
    if len(b) == 1:
        return False
    prev = b[0]
    streak = 1  
    for i in range(1,len(b)):
        if b[i] == prev:
            streak += 1
        elif streak > 1:
            if i == len(b) -1:
                return False
            prev = b[i]
            streak = 1
        else:
            return False
    return True


def distinct_values(l):
    distinct = []
    for c in l: 
        if c not in distinct:
            distinct.append(c)
    return distinct

test = ['AABBCC','AABBC_C','A','__','A__ADD__FQ_QQF']

for g in test:
    print(g,':Ladybug Happy=',happy_ladybugs(g))        
        
    
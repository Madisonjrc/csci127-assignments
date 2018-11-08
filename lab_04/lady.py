def happy_ladybugs(b):
    values = distinct_values(b)
    if '_' in values:
        values.remove('_')
        for v in values:
            count = 0
            for c in b:
                if v == c:
                    count += 1
            if count <= 1:
                return 'NO'
        return 'YES'
    
    elif is_full(b):
        return 'YES'
    
    else:
        return 'NO'
    
    
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

test = ['AABBCC','AABCBC','A','__','A__A','B__BG','RADA_D_R',
         'CC_DDD_FGFGC_C']

for g in test:
    print(g,'Ladybug Happy=',happy_ladybugs(g))        
        
    
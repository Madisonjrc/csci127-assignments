#Madison Chen and Rachel Tieu
import random
l=[]
for i in range (0,100):
    l.append(random.randrange(0,11))
print(l)
def max(l):
    x=0
    large=l[x]
    while x<len(l):
        if l[x]>large:
            large=l[x]
        x= x+1
    return large
print(max(l))
def freq(l,val):
    x=0
    freq=0
    while x<len(l):
        if l[x]==val:
            freq= freq+1
        x+=1
    return freq

print (freq(l, 4))
def mode(l):
    mmode=0
    u=[]
    num=0
    for i in l:
        if i not in u:
            mode=freq(l,i)
            if mode>mmode:
                mmode=mode
                num=i
            u.append(i)
    return num,mmode
print (mode(l))
    
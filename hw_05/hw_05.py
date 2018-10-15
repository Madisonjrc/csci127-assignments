def filterodd(l):
    list=[]
    for i in l:
        if i%2!=0:
            list+=[i]
    return list
print(filterodd([1,4,6,5,7,8,9]))
def mapsquare(l):
    list=[]
    for i in l:
        list+=[i*i]
    return list
print(mapsquare([1,4,6,5,7,8,9]))
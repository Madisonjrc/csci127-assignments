def countApplesAndOranges(s,t,a,b,apples,oranges):
    applecount = 0
    orangecount = 0
    
    for i in apples:
        pos =  a + i
        if pos >= s and pos <= t:
            applecount += 1
    
    for i in oranges:
        pos = b + i
        if pos >= s and pos <= t:
            orangecount += 1
    return applecount,orangecount

print('House position: [3,11], Apple tree: 5,Orange tree: 7, Apples: [-2,4,1], Oranges: [5,-6]\n')
print(countApplesAndOranges(3,11,5,7,[-2,4,1],[5,-6]))
print('House: [-9,-5], Apple tree: -12,\nOrange tree: -3, Apples: [4,3,-5,10], Oranges: [-3,2,-1]\n')
print(countApplesAndOranges(-9,-5,-12,-3,[4,3,-5,10],[-3,2,1]))
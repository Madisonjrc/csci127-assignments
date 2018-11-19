letters = ['AEIOULNRST','DG','BCMP','FHVWY','K','JX','QZ']
values = [1,2,3,4,5,8,10]
scores = {}
for x,y in zip(letters,values):
    for z in x:
        scores[z] = y
def score(w):
    answer = 0
    for x in w:
        answer += scores[x.upper()]
    return answer
print(score("testing"))
print(score("Zamansky"))
print(score("apple"))
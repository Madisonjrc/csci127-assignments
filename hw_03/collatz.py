#collatz.py
#t(n) n if
#in the loop print out sequence return and print out the # of steps
#go until n is one
def seq(n):
    count=0
    while (n != 1):
        if (n % 2 ==0):
            n=n // 2
        else:
            n=n * 3 + 1
        count+=1
        print(n)
    return "This while loop ran "+str(count)+" times"
print(seq(5))
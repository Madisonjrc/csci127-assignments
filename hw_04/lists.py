#Madison Chen
import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the lsit
      max_value : the max random value to put in the list
    """
    l = [] # start with an empty list

    # make a loop that counts up to size
    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        # we could have written this instead of the above line:
        # l = l + [random.randrange(0,max_value)]
        i = i + 1
    return l
print(build_random_list(10,100))

def locate(l, value):
    print(l)
    i = 0
    while i < len(l):
        if l[i] == value:
            return i
        else:
            i+=1
    return -1
print(locate(build_random_list(10, 35), 7))


def count(l, value):
    count = 0
    #print(l)
    for i in l:
        if i == value:
            count = count + 1
    return count
print(count(build_random_list(10,30),20))

def reverse(l):
    i = len(l)-1
    while i >=0:
        print(l[i])
        i -= 1
print(reverse(build_random_list(10,30)))

    
def isIncreasing(l):
    print(l)
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True
print(isIncreasing(build_random_list(10,30)))

def palindrome(l):
    print(l)
    if l[::-1] == l:
        return True
    return False
print(palindrome(build_random_list(10,30)))
#fizzbuzz
#if number divisible by 3 print fizz
#if number divisible by 5 print buzz
#if both print both
#Madison Chen and Narsima Donuk

def fizzbuzz(max_value):
    count=0
    while count <= max_value:
        if count % 15 == 0 :
            print ("FizzBuzz")
        elif count % 3 == 0:
            print ("Fizz")
        elif count % 5 == 0:
            print ("Buzz")
        else:
            print (count)
        count = count + 1
    return "there are "+ str(max_value // 15) + " FizzBuzz"
print(fizzbuzz(100))
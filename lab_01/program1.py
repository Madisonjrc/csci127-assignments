def greeter(name):
        return "hello"+name+"!"
print(greeter("stan"))
print(greeter("ollie"))
def make_abba(a, b):
  return a+b+b+a
def hello_name(name):
  return "Hello "+ name+"!"

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

def missing_char(str, n):
    front= str[:n]
    back=str[n+1:]
    return front+back
def monkey_trouble(a_smile, b_smile):
  if a_smile==True and b_smile==True:
    return True
  if a_smile==False and b_smile==False:
    return True
  if a_smile==True and b_smile==False:
    return False
  if a_smile==False and b_smile==True:
    return False
def parrot_trouble(talking, hour):
  if talking==True and hour!=[7,8,9,10,11,12,13,14,15,16,17,18,19]:
    return True
  else:
    return False

print(monkey_trouble(True,False))
print(near_hundred(10))    
print(hello_name("dolly"))
print(make_abba("hi","bye"))
print(missing_char("hello",2))

#vowel -> just add "ay" to end otherwise do first to end and add "ay"
def part_pig_latin(name):

    if name[0]!= ("a" or "e" or "i" or "o" or "u"):
        return name[1:] + name[0] + "ay"
    else:
        return name+"ay"
    
print(part_pig_latin("madison"))
print(part_pig_latin("apple"))                                        

def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    return name.title()

print (capitalize("madison chen"))

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    
    """
    name_list=


    
def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    return name[1:] + name[0] + "ay"
def make_out_word(out, word):
    return out[:2] + word + out[2:]
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags("i", "yay"))

print(make_out_word("[[]]","find"))

print(part_pig_latin("Madison"))

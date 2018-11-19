def encode(s):
    if len(s) == 0:
        return []
    counter = 0
    i = 0
    out = []
    prev = s[0]
    while i < len(s):
        if s[i] == prev:
            counter += 1
        else:
            out.append([prev,count])
            prev = s[i]
            counter = 1
    
print(encode('lllllllllaaaaaammmmmmmbbbbb'))


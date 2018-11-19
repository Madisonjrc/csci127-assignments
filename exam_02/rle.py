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
            out.append([prev,counter])
            prev = s[i]
            counter = 1
        i += 1
    out.append([prev,counter])
    return out
def decode(s):
    out = ''
    for l in s:
        out += l[0]*l[1]
    return out
print(encode('lllllllllaaaaaammmmmmmbbbbb'))
print(decode(encode('llllllaaaaammmmmmmbbbbb')))

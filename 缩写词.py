def acronym(phrase):
    s = ''
    phrase = phrase.upper()
    p = phrase.split()
    for i in range(0,len(p)):
        s = s + p[i][0]
    return s
phrase=input()
print(acronym(phrase))    
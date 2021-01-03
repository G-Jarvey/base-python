stuid = {}
stuscore = {}
course = set()

while true:
    line = input()
    if line == 'END':
        break
    s = line.split(',')
    if len(s) == 2:
        stuid[s[0]] = s[1]
    elif len(s) == 3:
        #s = ['id','course','score']
        d = stuscore.get(s[0],{})
        d[s[1]] = int(s[2])
        course.add(s[1])

d = stuscore[id]
for k in score:
    if k in d:
        pass
        
    

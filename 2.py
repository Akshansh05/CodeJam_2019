def calcPath():
    grids = int(input())
    herpath = list(input())
    mypath = []
    for c in herpath:
        if c == 'S':
            mypath.append('E')
        elif c == 'E':
            mypath.append('S')

    return ''.join(mypath)


tests = int(input())
answers = []
for test in range(tests):
    answers.append(calcPath())
index = 1
for answ in answers:
    print('Case #%d: %s' % (index, answ))
    index = index + 1

result = 0

inputline = input('Enter the roman numerals  you want to convert:')

def add(x):
    result += x

def sub(x):
    result += x

def split(input):
    return [char for char in input]

inputlist = split(inputline)
numlist = []

mnum = 1000
dnum = 500
cnum = 100
lnum = 50
xnum = 10
vnum = 5
inum = 1

i = 0

while i < len(inputlist):
    if inputlist[i] == 'M' : numlist.append(mnum)
    elif inputlist[i] == 'D': numlist.append(dnum)
    elif inputlist[i] == 'C': numlist.append(cnum)
    elif inputlist[i] == 'L': numlist.append(lnum)
    elif inputlist[i] == 'X': numlist.append(xnum)
    elif inputlist[i] == 'V': numlist.append(vnum)
    elif inputlist[i] == 'I': numlist.append(inum)
    i+=1

i = 0
while i < len(numlist):
    if numlist[i] < numlist[i+1] and i != len(numlist):
        sub(numlist[i])
    else:
        add(numlist[i])
    i+=1

print(result)

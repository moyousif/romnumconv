result = 0

inputline = input('Enter the roman numerals you want to convert: ')

def add(x,result):
    result += x
    return result

def sub(x,result):
    result -= x
    return result

def split(input):
    return [char for char in input]

inputlist = split(inputline)
numlist1 = []

mnum = 1000
dnum = 500
cnum = 100
lnum = 50
xnum = 10
vnum = 5
inum = 1

i = 0

while i < len(inputlist):
    if inputlist[i] == 'M' : numlist1.append(mnum)
    elif inputlist[i] == 'D': numlist1.append(dnum)
    elif inputlist[i] == 'C': numlist1.append(cnum)
    elif inputlist[i] == 'L': numlist1.append(lnum)
    elif inputlist[i] == 'X': numlist1.append(xnum)
    elif inputlist[i] == 'V': numlist1.append(vnum)
    elif inputlist[i] == 'I': numlist1.append(inum)
    i+=1

i = 0
numlist2 = numlist1

for i in range(0, len(numlist1)-1):
    if numlist1[i] < numlist2[i+1]:
        result = sub(numlist1[i], result)
    else:
        result = add(numlist1[i], result)

result = add(numlist1[-1], result)


print(result)

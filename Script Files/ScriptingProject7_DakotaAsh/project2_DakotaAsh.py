file = input("Enter the file name: ")
opn = open(file, "r")
lyst = list()

for line in opn:
    line = line.strip('\n')
    lyst.append(line)

loop = True
while loop:
    print('The file has', len(lyst), 'lines.')
    lineNum = int(input('Enter a line number, or 0 to quit: '))
    if lineNum == 0:
        loop = False
    else:
        print(str(lineNum)+': '+lyst[lineNum-1]+'\n')
opn.close()

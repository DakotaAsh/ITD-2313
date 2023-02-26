file = input("Enter the file name: ")
try:
    a = open(file, 'r')
except:
    print("Error, could not open file: ", file)
print('{:<12s} {:>10s} {:>10s}'.format('Name', 'Hours', 'Total Comp'))
for line in a.readlines():
    name, hours, comp = line.split()
    hours = int(hours)
    comp = float(comp)
    total = hours * comp
    print('{:<12s} {:>10d} {:>10.2f}'.format(name, hours, comp))
a.close()

afile = input("Enter a filename and its extension: ")
bfile = input("Enter another filename and its extension: ")
a = open(afile, "r")
b = open(bfile, "w+")
content = a.read()
b.write(content)
a.close()
b.close()
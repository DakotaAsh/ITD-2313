codedText = input("Enter the coded text: ")
distance = int(input("Enter the distance: "))
plainText = ""
for x in codedText:
    order = ord(x)
    a = order - distance
    plainText += chr(a)
print(plainText)

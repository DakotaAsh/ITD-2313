text = input("Enter some text: ")
a = int(input("Enter distance value: "))
result = ""
for x in text:
    result += chr(ord(x)+a)
print(""+result)

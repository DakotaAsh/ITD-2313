height = float(input("Enter the height: "))
index = float(input("Enter the bounce index  of the ball: "))
bounce = int(input("Enter the number of times the ball is allowed to bounce: "))

distance = height

for bounce in range(bounce-1):
    height *= index
    distance += height*2

distance += height*index

print("The distance traveled is: " +str(distance) + "feet")

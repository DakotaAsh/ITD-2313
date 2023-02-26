x = 1
iteration = int(input("Enter the number of iterations: "))

y = 0

for z in range(iteration):
        if z % 2 == 0:
            y+=4/x
        else:
            y-=4/x
            x += 2

print("Here is your value, given " +str(iteration),"iterations: \n", y)

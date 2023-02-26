salary = float(input("Enter a starting salary: "))
percent = float(input("Enter an annual percent increase: "))
year = int(input("Enter the tenure: "))
print("\n""Year       Salary""\n""-----------------")
for a in range(1, year+1):
    print(a,"\t",end="")
    print("%.2f"%salary)
    salary = salary * (1+percent/100)

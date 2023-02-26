#Significant constants
tax = 0.20
deduct_s = 10000.0
deduct_d = 3000.0

#The inputs are
g_income = float(input("Enter the gross income: "))
d_count = int(input("Enter the number of dependents: "))

#Maths
taxableIncome = g_income - deduct_s - deduct_d * d_count

incomeTax = round(taxableIncome * tax, 2)

#The outputs are
print("The income tax is $" + str(incomeTax))

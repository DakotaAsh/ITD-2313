hourlyWage = input("Please tell me your hourly wage: ")
hoursWorked = input("Please tell me how many hours you've worked: ")
overtime = input("If any, how many hours of overtime have you worked: ")
weekly = float(hourlyWage)*float(hoursWorked)+float(overtime)*1.5
pay = print("Your weekly gross income is: $", weekly)

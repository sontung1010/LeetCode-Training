portion_down_payment = 0.25
current_savings = 0
r = 0.04
month = 0
raise_month = 0

annual_salary = int(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

down_payment = portion_down_payment*total_cost
monthly_salary = annual_salary/12
while current_savings < down_payment:
    current_savings = monthly_salary*portion_saved + current_savings*(1 + r/12)
    print(current_savings)
    month += 1
    raise_month += 1
    a = raise_month % 6
    if a == 0:
        monthly_salary = monthly_salary*(1 + semi_annual_raise)


print("Number of months: " + str(month))


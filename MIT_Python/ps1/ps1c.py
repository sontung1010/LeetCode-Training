month_total = 36
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000
down_payment = total_cost * portion_down_payment


current_savings = 0
epsilon = 100
raise_month = 0
steps = 0
low = 0
high = 10000

annual_salary = int(input("Enter your starting salary: "))
if annual_salary <= 68476:
    print("It is not possible to pay the down payment in three years.")
else:
    monthly_salary = annual_salary/12
    guess = (high + low)/2
    savings_rate = guess/10000

    while raise_month < month_total:
        current_savings = monthly_salary*savings_rate + current_savings*(1 + r/12)
        raise_month += 1
        a = raise_month % 6
        #print("current_savings = " + str(current_savings))
        if a == 0:
            monthly_salary = monthly_salary*(1 + semi_annual_raise)

    while abs(current_savings - down_payment) >= epsilon:
        if current_savings < down_payment:
            #print("current_savings < down_payment")
            low = guess
            #print("low = " + str(low))
        else:
            #print("current_savings > down_payment")
            high = guess
            #print("high = " + str(high))
        guess = (high + low)/2
        steps += 1
        #print("steps = " + str(steps))
        #if steps > 2:
        #   break
        current_savings = 0
        monthly_salary= annual_salary/12
        raise_month = 0
        savings_rate = guess/10000
        #print("saving_rate of step " + str(steps) + ": " + str(savings_rate))

        while raise_month < month_total - 1:
            current_savings = monthly_salary*savings_rate + current_savings*(1 + r/12)
            #print("current_savings of step " + str(steps) + ": " + str(current_savings))
            raise_month += 1
            #print("raise_month of step " + str(steps) + ": " + str(raise_month))
            a = raise_month % 6
            if a == 0:
                monthly_salary = monthly_salary*(1 + semi_annual_raise)
                #print("monthly_salary of step " + str(steps) + " now is " + str(monthly_salary))


    print("Best savings rate: " + str(savings_rate))
    print("Steps in bisection search: " + str(steps))


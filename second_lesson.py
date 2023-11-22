symbol = "~" * 40  # For example, I can write it in the form: print("~" * 40)

print(symbol)

name = input("Enter your name: ")
name = name.strip().title()

age = int(input("Enter your age: "))

average_salary = float(input("Enter your average salary: "))
average_salary = round(average_salary, 2)

years_until_retirement = 65 - age

all_money_earned = years_until_retirement * average_salary * 12

salary_in_dollars = all_money_earned / 37.3
salary_in_dollars = round(salary_in_dollars, 2)

count_of_toyota = int(salary_in_dollars / 31500)

print(
    f"I,{name} can only earn __{salary_in_dollars}__ dollars, this is enough for only __{count_of_toyota}__ cars, "
    f"I am not satisfied with this, so I will change my life and study programming hard!"
)

import requests

url = "https://script.google.com/macros/s/AKfycbzoMCJqHKEHx4CkmQZ4uCByYGrhYZUKBGtNtf9eVIi3pmNdMFqsHDJIZnUx-wTr98zjFQ/exec"

response = requests.get(url=url)
data_from_net = response.json()
family = data_from_net["family"]

monthly_income = 0
count_of_large_families = 0
count_loan_more_than_income = 0
count_women_with_housing = 0

for person in family:
    large_family = person["large_family"]
    if large_family == True and person["age"] > 35:
        monthly_income_of_person = person["monthly_income"]
        monthly_income += monthly_income_of_person
    if large_family == True:
        large_families = large_family
        count_of_large_families += large_families
    if person["loan_per_month"] > person["monthly_income"]:
        loan_more_than_income = 1
        count_loan_more_than_income += loan_more_than_income
    if person["gender"] == "female" and person["own_home"] == True:
        women_with_housing = 1
        count_women_with_housing += women_with_housing

# For me
print(
    f"Місячний дохід людей, сімя яких є багатодітною і вік яких більше 35 років: {monthly_income} грн \n"
    f"Кількість багатодітних сімей: {count_of_large_families}\n"
    f"Сумарна кількість сімей, в яких витрати за кредитами більші за доходи: {count_loan_more_than_income}\n"
    f"Скільки жінок забезпечені власним житлом: {count_women_with_housing}"
)

import constants


def is_string_from_digits(my_string: str) -> bool:
    has_string_only_digits = my_string.isdigit()
    return has_string_only_digits


# Convert centimeters to inches
def get_centimeters() -> str:
    while True:
        user_input = input(constants.MSG_USER_INPUT)
        if is_string_from_digits(user_input):
            return user_input
        print(constants.MSG_NOT_NUMERIC_INPUT)


def convert_str_into_float(number_string: str) -> float:
    is_convertable = is_string_from_digits(number_string.replace(".", ""))
    if not is_convertable:
        raise ValueError(
            f"Damn, cannot process {number_string} into number <from convert_str_into_int>"
        )
    converted_value = float(number_string)
    return converted_value


def get_inches_from_centimeters(*, centimeters: float, inch: float = 0.39) -> float:
    inches = float(centimeters * inch)
    inches = round(inches, 2)
    return inches


# Return a list of even numbers
def get_list_of_numbers() -> list[str]:
    while True:
        list_data = input(constants.MSG_USER_INPUT_NUMBERS).split()
        for element in list_data:
            if is_string_from_digits(element):
                return list_data
            else:
                print(constants.MSG_NOT_NUMERIC_INPUT)


def get_paired_numbers(numbers: list[str]) -> list[int]:
    paired_numbers_list = []
    for num in numbers:
        int_num = int(num)
        if int_num % 2 == 0:
            paired_numbers_list.append(int_num)
    return paired_numbers_list


# Response to a mortgage inquiry
def get_mortgage_amount() -> str:
    while True:
        mortgage_amount = input(constants.MSG_USER_INPUT_MORTGAGE)
        if is_string_from_digits(mortgage_amount):
            return mortgage_amount
        print(constants.MSG_NOT_NUMERIC_INPUT)


def get_monthly_income() -> str:
    while True:
        monthly_income = input(constants.MSG_USER_INPUT_INCOME)
        if is_string_from_digits(monthly_income):
            return monthly_income
        print(constants.MSG_NOT_NUMERIC_INPUT)


def get_loan_response(*, mortgage: float, income: float) -> str:
    per_for_month = mortgage / 25 / 12
    percent = (income / 100) * 35
    if per_for_month > percent:
        return "No"
    else:
        return "Yes"

import ninth_lesson_library_function


def main():
    # Convert centimeters to inches
    raw_centimeters: str = ninth_lesson_library_function.get_centimeters()
    centimeters: float = ninth_lesson_library_function.convert_str_into_float(
        raw_centimeters
    )
    inches: float = ninth_lesson_library_function.get_inches_from_centimeters(
        centimeters=centimeters,
    )
    print(f"You get {inches} inches in {centimeters} centimeters")

    # Return a list of even numbers
    numbers: list[str] = ninth_lesson_library_function.get_list_of_numbers()
    list_paired: list[int] = ninth_lesson_library_function.get_paired_numbers(numbers)
    print(f"List of even numbers: {list_paired}")

    # Response to a mortgage inquiry
    raw_mortgage: str = ninth_lesson_library_function.get_mortgage_amount()
    raw_income: str = ninth_lesson_library_function.get_monthly_income()
    mortgage: float = ninth_lesson_library_function.convert_str_into_float(raw_mortgage)
    income: float = ninth_lesson_library_function.convert_str_into_float(raw_income)
    answer: str = ninth_lesson_library_function.get_loan_response(
        mortgage=mortgage,
        income=income,
    )
    print(f"Answer to your request: {answer}")


if __name__ == "__main__":
    main()

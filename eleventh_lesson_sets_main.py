import eleventh_lesson_sets_functions


def main():
    city: list[str] = eleventh_lesson_sets_functions.get_cities_you_have_been()
    city_in_future: list[str] = eleventh_lesson_sets_functions.get_cities_in_future()
    result: str = eleventh_lesson_sets_functions.get_answer_about_cities(
        city=city,
        city_in_future=city_in_future,
    )
    print(result)


if __name__ == "__main__":
    main()

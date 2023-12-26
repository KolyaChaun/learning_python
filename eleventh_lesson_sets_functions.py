def tuple_in_str(cities):
    my_str = ", ".join(cities)
    return my_str


def get_cities_you_have_been() -> list[str]:
    city = (
        input("Введіть через пробіл міста, в яких ви були за минулі 10 років: ")
        .title()
        .split()
    )
    return city


def get_cities_in_future() -> list[str]:
    city_in_future = (
        input(
            "Введіть через пробіл міста, куди ви хотіли би поїхати в наступні 10 років: "
        )
        .title()
        .split()
    )
    return city_in_future


def get_answer_about_cities(*, city: list[str], city_in_future: list[str]) -> str:
    common = set(city) & set(city_in_future)
    common_str = tuple_in_str(common)
    if common:
        result = f"Вам мабуть, дуже сподобалося в цих містах: {common_str}"
        return result
    else:
        result = "Я бачу, що ви відкриті до чогось нового"
        return result

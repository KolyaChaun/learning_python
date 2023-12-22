def distance_traveled_the_vehicle(*, time: int, speed: int, weight: int | float) -> str:
    if time <= 0 or speed <= 0 or weight <= 0:
        raise ValueError(
            "Enter correct data (for example speed = 20, time = 60, weight = 1000)"
        )
    distance = time * speed
    result = (
        f"Транспортний засіб вагою {weight} кг рухався {time} секунд зі швидкістю {speed}м/сек, "
        f"і подолав відстань {distance} метрів"
    )
    return result

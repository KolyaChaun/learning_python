import tenth_lesson_function


def main():
    result: str = tenth_lesson_function.distance_traveled_the_vehicle(
        time=3600,
        speed=22,
        weight=1300,
    )
    print(result)


if __name__ == "__main__":
    main()

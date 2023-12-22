import tenth_lesson_function
import pytest


def test_distance_traveled_vehicle_valid_data():
    expected = (
        "Транспортний засіб вагою 1300 кг рухався 3600 секунд зі швидкістю 20м/сек,"
        " і подолав відстань 72000 метрів"
    )
    actual_result = tenth_lesson_function.distance_traveled_the_vehicle(
        speed=20, time=3600, weight=1300
    )
    assert expected == actual_result


def test_distance_traveled_vehicle_25speed():
    expected = (
        "Транспортний засіб вагою 1300 кг рухався 3600 секунд зі швидкістю 25м/сек,"
        " і подолав відстань 90000 метрів"
    )
    actual_result = tenth_lesson_function.distance_traveled_the_vehicle(
        speed=25, time=3600, weight=1300
    )
    assert expected == actual_result


def test_distance_traveled_vehicle_900weight():
    expected = (
        "Транспортний засіб вагою 900 кг рухався 3600 секунд зі швидкістю 25м/сек,"
        " і подолав відстань 90000 метрів"
    )
    actual_result = tenth_lesson_function.distance_traveled_the_vehicle(
        speed=25, time=3600, weight=900
    )
    assert expected == actual_result


def test_distance_traveled_vehicle_10time():
    expected = (
        "Транспортний засіб вагою 900 кг рухався 10 секунд зі швидкістю 25м/сек,"
        " і подолав відстань 250 метрів"
    )
    actual_result = tenth_lesson_function.distance_traveled_the_vehicle(
        speed=25, time=10, weight=900
    )
    assert expected == actual_result


def test_distance_traveled_vehicle_0time():
    with pytest.raises(ValueError):
        tenth_lesson_function.distance_traveled_the_vehicle(
            speed=25, time=0, weight=1300
        )


def test_distance_traveled_vehicle_0speed():
    with pytest.raises(ValueError):
        tenth_lesson_function.distance_traveled_the_vehicle(
            speed=0, time=10, weight=1300
        )


def test_distance_traveled_vehicle_minus_weight():
    with pytest.raises(ValueError):
        tenth_lesson_function.distance_traveled_the_vehicle(
            speed=25, time=10, weight=-1300
        )

from abc import ABC, abstractmethod
from typing import Self


class Vehicle(ABC):
    def __init__(
        self,
        brand: str,
        volume_of_tank: int,
        remainder_in_tank: int | float,
        speed: int | float,
        mileage: int | float,
    ):
        self.brand = brand.upper()
        self.volume_of_tank = volume_of_tank
        self.remainder_in_tank = remainder_in_tank
        self.speed = speed
        self.mileage = mileage

    def refuel_the_car(self, add_fuel: int | float):
        if self.remainder_in_tank + add_fuel < self.volume_of_tank:
            self.remainder_in_tank += add_fuel
            print(
                f"===========================================\n"
                f"В {self.brand} було заправлено {add_fuel}л\n"
                f"==========================================="
            )
        else:
            print(
                f"===========================================\n"
                f"В транспортний засіб {self.brand}, ви не зможете заправити больще ніж максимальний обьем баку:"
                f" {self.volume_of_tank}л\n"
                f"==========================================="
            )

    def transfer_fuel(self, other: Self, amount_of_fuel: int | float):
        if self.remainder_in_tank < amount_of_fuel:
            print(
                f"===========================================\n"
                f"Недостатньо палива в топливному баку: {self.brand}\n"
                f"==========================================="
            )

        elif other.remainder_in_tank + amount_of_fuel > other.volume_of_tank:
            print(
                f"===========================================\n"
                f"Недостатньо вільного місця в топливному баку: {other.brand}\n"
                f"==========================================="
            )
        else:
            self.remainder_in_tank -= amount_of_fuel
            other.remainder_in_tank += amount_of_fuel
            print(
                f"===========================================\n"
                f"Було здійснено перелив пального з {self.brand} в {other.brand} у кількості {amount_of_fuel}л\n"
                f"==========================================="
            )

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplemented


class Car(Vehicle):
    def __init__(
        self,
        brand: str,
        volume_of_tank: int,
        remainder_in_tank: int | float,
        speed: int | float,
        mileage: int | float,
        passengers: int,
        airbags: bool = None,
    ):
        super().__init__(brand, volume_of_tank, remainder_in_tank, speed, mileage)
        self.passengers = passengers
        self.airbags = airbags

    def __str__(self):
        return (
            f"Марка: {self.brand}, \n"
            f"Обєм баку: {self.volume_of_tank}л, \n"
            f"Залишок пального в баку: {self.remainder_in_tank}л,\n"
            f"Пробег: {self.mileage} км, \n"
            f"Максимальна швидкість: {self.speed} км/год\n"
            f"Пробіг: {self.mileage} км\n"
            f"Кількість пасажирів: {self.passengers},\n"
            f"Наявність подушок безпеки : {self.airbags}"
        )


class Motorbike(Vehicle):
    def __init__(
        self,
        brand: str,
        volume_of_tank: int,
        remainder_in_tank: int | float,
        speed: int | float,
        mileage: int | float,
        sidecar: bool = None,
    ):
        super().__init__(brand, volume_of_tank, remainder_in_tank, speed, mileage)
        self.sidecar = sidecar

    def __str__(self):
        return (
            f"Марка: {self.brand}, \n"
            f"Обєм баку: {self.volume_of_tank}л, \n"
            f"Залишок пального в баку: {self.remainder_in_tank}л,\n"
            f"Пробег: {self.mileage} км, \n"
            f"Максимальна швидкість: {self.speed} км/год\n"
            f"Пробіг: {self.mileage} км\n"
            f"Люлька: {self.sidecar}"
        )


bmw = Car("bmw", 55, 30, 220, 100000, 5, True)
yamaha = Motorbike("yamaha", 15, 8, 180, 5000, False)

yamaha.refuel_the_car(5)
yamaha.transfer_fuel(bmw, 8.5)
print(bmw)
print(yamaha)

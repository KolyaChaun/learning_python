class Car:
    mileage: int = 0

    def __init__(self, brand: str, manufacturer: str, year: int = 2020, fuel_consumption: float = 0.0):
        self.brand = brand.upper()
        self.manufacturer = manufacturer.title()
        self.year = year
        self.fuel_consumption = fuel_consumption

    def __str__(self) -> str:
        return (
            f"Марка авто: {self.brand},\n"
            f"Виробник: {self.manufacturer},\n"
            f"Рік випуску: {self.year} року,\n"
            f"Пробіг: {self.mileage} км,\n"
            f"Витрата палива: {self.fuel_consumption}л/100км\n"
            f"----------------------------"
        )

    def signal(self):
        return "Beeeee! Beeeee! Beeeee!"


vw = Car("volkswagen", "germany", 2010)
toyota = Car("tyOta", "Jpan", 2005, 8)
bmw = Car("bmw", "germany")
vw.mileage = 100_050
vw.fuel_consumption = 8.5
toyota.mileage = 9000
bmw.fuel_consumption = 12.1

print(vw)
print(toyota)
print(bmw)

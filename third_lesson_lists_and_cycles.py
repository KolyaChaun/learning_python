cities = "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$".strip(
    "6..5874$:?$"
).split()

for citi in cities:
    print(f"Я\U00002764_{citi.title()}_")

with open("airport-codes_csv.csv", mode="r", encoding='utf-8') as file:
    for line in file:
        if line.split(";")[5] == "UA":
            print(line.split(';')[2])

import requests
import json

url = "https://dummyjson.com/quotes?limit=100"

response = requests.get(url)

data_from_net = response.json()

with open("eight_lesson_data.json", mode="w", encoding='utf-8') as file:
    json.dump(data_from_net, file, indent=4)

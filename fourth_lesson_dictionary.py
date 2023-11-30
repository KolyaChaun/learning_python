students = {
    "Іван Петров": {
        "Пошта": "Ivan@gmail.com",
        "Вік": 14,
        "Номер телефону": "+380987771221",
        "Середній бал": 95.8,
    },
    "Женя Курич": {
        "Пошта": "Geka@gmail.com",
        "Вік": 16,
        "Номер телефону": None,
        "Середній бал": 64.5,
    },
    "Маша Кера": {
        "Пошта": "Masha@gmail.com",
        "Вік": 18,
        "Номер телефону": "+380986671221",
        "Середній бал": 80,
    },
}

students["Микола Чаюн"] = {
    "Пошта": "kolia.kolia@gmail.com",
    "Вік": 25,
    "Номер телефону": "+380961271221",
    "Середній бал": 99,
}

average_score_by_group = (
    students["Іван Петров"]["Середній бал"]
    + students["Женя Курич"]["Середній бал"]
    + students["Маша Кера"]["Середній бал"]
    + students["Микола Чаюн"]["Середній бал"]
) / len(students)
# average_score_by_group_difficult = sum(student["Середній бал"] for student in students.values()) / len(students)

students["Іван Петров"]["bank_account_number"] = None

salary_data_person_two = students["Женя Курич"].get("Заробітня плата") or 0.0

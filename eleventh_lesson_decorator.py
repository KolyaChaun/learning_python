import time


def decorator_create_file_with_logs(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        function_loading_speed = time.time() - start_time
        with open("eleventh_lesson_logs.txt", mode="a", encoding="utf-8") as file:
            file.write(
                f"Назва функції: {func.__name__},\n"
                f"Результат виконання функції: {result},\n"
                f"Швидкість виконання функції: {function_loading_speed}\n"
                f"---------------------------\n"
            )
            return result
    return wrapper


@decorator_create_file_with_logs
def get_message() -> str:
    return "Hi Python!"


@decorator_create_file_with_logs
def multiplication(num1: int, num2: int) -> int:
    return num1 * num2


@decorator_create_file_with_logs
def number_to_power(num1: int, num2: int) -> int:
    return num1**num2


get_message()
multiplication(2, 5)
number_to_power(2, 10)
multiplication(3, 3)
number_to_power(2, 5)


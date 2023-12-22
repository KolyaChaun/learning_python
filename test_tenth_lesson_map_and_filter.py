import tenth_lesson_map_and_filter


def test_list_str():
    expected = [
        "Kolya",
        "10",
        "True",
        "25",
        "False",
        "30.5",
        "Python",
        "5",
        "True",
        "3.2",
        "False",
        "100",
        "33.3",
    ]
    actual_result = tenth_lesson_map_and_filter.my_list_str
    assert expected == actual_result


def test_list_int():
    expected = [10, 25, 5, 100]
    actual_result = tenth_lesson_map_and_filter.my_list_int
    assert expected == actual_result

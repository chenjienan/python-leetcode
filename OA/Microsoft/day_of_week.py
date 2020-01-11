def dayOfWeek(S, K):
    day_to_num = {
        "Mon": 0,
        "Tue": 1,
        "Wed": 2,
        "Thu": 3,
        "Fri": 4,
        "Sat": 5,
        "Sun": 6
    }

    num_to_day = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
    }

    return num_to_day[(day_to_num[S] + K) % 7]

print(dayOfWeek("Wed", 2))
print(dayOfWeek("Sat", 23))
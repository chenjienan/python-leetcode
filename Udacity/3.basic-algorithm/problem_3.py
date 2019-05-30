def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_ls = sorted(input_list)

    num_1 = ""
    num_2 = ""
    for i, d in enumerate(sorted_ls[::-1]):
        if i % 2 == 0: num_1 += str(d)
        else: num_2 += str(d)
    return int(num_1), int(num_2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
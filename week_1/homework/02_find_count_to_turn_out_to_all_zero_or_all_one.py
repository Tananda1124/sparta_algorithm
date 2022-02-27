input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    space = 1
    for i in string:
        input_scan_array = list(string)

    compare_array = input_scan_array

    input_scan_array = list(map(int, input_scan_array))
    compare_array = list(map(int, compare_array))
    del compare_array[0]

    for i in compare_array:
        if input_scan_array[i] != compare_array[i]:
            space += 1
    if space % 2 == 0:
        return round(space / 2)
    elif space == 1:
        return 0


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
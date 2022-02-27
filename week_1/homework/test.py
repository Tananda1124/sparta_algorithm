input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # space 나누기 -> space 세기 -> 최소 뒤집기 return
    space = 1
    for i in string:
        input_scan_array = list(string)
    print(input_scan_array)

    input_scan_array = list(map(int, input_scan_array))
    compare_array = [0] * len(input_scan_array - 1)
    for i in input_scan_array:
        input_scan_array[i + 1] = compare_array[i]

    for i in compare_array:
        if input_scan_array[i] != compare_array[i]:
            space += 1
    # 1,1
    # 2,1
    # 3,1
    # 4,2
    # 5,2
    # 6,3
    if space % 2 == 0:
        return round(space / 2)
    else:
        return 0


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

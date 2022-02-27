input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    max_num = 0
    for i in array:
        if max_num == 0:
            max_num = max_num + i
        else:
            if i <= 1:
                max_num = max_num + i
            else:
                max_num = max_num * i

    return max_num


result = find_max_plus_or_multiply(input)
print(result)
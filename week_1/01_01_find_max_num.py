input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 이 부분을 채워보세요!
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num
        # Tip. for - else 문은 break가 실행되지 않았을 경우에 실행된다.


result = find_max_num(input)
print(result)

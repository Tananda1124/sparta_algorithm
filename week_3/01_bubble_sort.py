input = [4, 6, 2, 9, 1]
# a, b = b, a -> 서로의 값을 바꿔준다. 참고하여 풀어보자


def bubble_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
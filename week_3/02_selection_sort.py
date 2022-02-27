input = [4, 6, 2, 9, 1]
a = [3, 99, 39, 30, 50]


def selection_sort(array):
    # 이 부분을 채워보세요!
    num = 0
    for i in range(len(array)):
        for j in range(len(array) - 1 - num):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
        num += num
        if num == len(array):
            return array


selection_sort(input)
selection_sort(a)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
print(a)

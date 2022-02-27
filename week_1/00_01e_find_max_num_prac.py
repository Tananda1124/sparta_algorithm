# --method 1 이중반복 이용하기 --
# array = [1, 2, 3, 4, 5, 100, 6]
#
# def find_max_num(array):
#     for num in array:
#         for compare_num in array:
#             if num < compare_num:
#                 break
#         else:
#             return num
#
#
# a = find_max_num(array)
# print(a)

#--method 2 하나씩 비교하기--
# array = [1, 3, 5, 7, 1024, 9]
#
# def find_max_num(arr):
#     max_num = arr[0]
#     for i in arr:
#         if max_num < i:
#             max_num = i
#     return max_num

#i를 넣을때 arr[i]로 넣어 계속 오류가 났음. python에서는 C99와 for문이 다름을 숙지하자!
#
# print(find_max_num(array))


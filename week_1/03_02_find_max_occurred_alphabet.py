input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            # bool값이 들어가는 조건문에서는 함수 앞에 not을 주로 쓰는 듯하다. --> char의 값이 string이면 계속해서 실행하라는 뜻
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(ord("a") + max_alphabet_index)



result = find_max_occurred_alphabet(input)
print(result)
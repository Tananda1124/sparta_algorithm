def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            # bool값이 들어가는 조건문에서는 함수 앞에 not을 주로 쓰는 듯하다. --> char의 값이 string이면 계속해서 실행하라는 뜻
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
    return alphabet_occurrence_array



print(find_alphabet_occurrence_array("bbbb"))
print(find_alphabet_occurrence_array("hello my name is sparta"))

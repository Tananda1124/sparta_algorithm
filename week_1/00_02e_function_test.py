# 입력값이 문자인지 판단해주는 str.isalpha()함수는 True, False 등의 bool값을 반환해준다.
# a = str.isalpha('a')
# print(a)
#
# b = [0]*2
# c = str.isalpha(b[0])
# print(b)
# print(c)
# # --> str.isalpha() 함수에는 배열값이 들어가면 오류가 발생한다.

# ord() --> 문자를 아스키 코드 값으로 반환해준다. 숫자를 문자로 변환하려면 chr()
# a = ['a']*3
# b = ord('a')
# c = ord(a[0])
#
# print(b)
# print(c)
# print(ord(a[0]))
#
# for i in a:
#    print(ord(b))
# ord()에 배열형식이 들어가면 실패한다.

print(str.isalpha())
#■■■ input() ■■■#

# 사용자의 입력을 받는 방법. (간단한 키보드 이런종류)
a=input()
    # input()함수를 사용해서 변수에 값을 저장하는 것이다.
    # 이때 값은 변수에 문자열로 저장이 된다.


# 프롬프트를 띄워서 사용자로부터 입력 받기 (즉, 입력에 대한 설명을 하고 싶을때)
a=input("숫자를 입력해주세요:")





#■■■ print() ■■■#

# print() 심화 과정
# 1. 큰따옴표(")로 둘러싸인 문자열은 +연산과 동일하다.
print("123""456""789")

# 2. 문자열 띄어쓰기는 콤마로 한다.
print("My","name","is","dahan")

# 3. 한 줄에 결과값을 계속 출력하고 싶을 때
for i in range(5):
    print(i, end=" ")
    # 즉, print 파라미터 중 end속성에 값을 " " 즉, 한칸 띄어쓰기나 공백을 줘서 원래 default로 들어가 있는 \n(개행)을 취소시킨 것임
print("세 정수를 입력하세요. ")

A = int(input("정수 A 값을 입력하시오"))
B = int(input("정수 B 값을 입력하시오"))
C = int(input("정수 C 값을 입력하시오"))

maximum = A
if B > maximum:
    maximum = B
if C > maximum:
    maximum = C

print(f'최대값은 {maximum}')
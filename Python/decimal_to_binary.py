n = float(input("변환하고 싶은 숫자를 입력해주세요 : ")) # 10진수 입력받기
binary = int(input("변환할 진법을 입력해주세요 : ")) # 변환할 진수

integer = int(n) # 10진수의 정숫값
decimal = n - int(n) # 입력받은 10진수의 소숫값
result = "" # 결과값을 받을 문자열
count = 0 # 한계

if binary > 16:
    print("2 ~ 16진수 사이로 입력해주세요!")
    exit()


while integer != 0 and count < 30: # 정수가 0이 될 때까지, count(한계)가 30이 될 때까지 반복
    print(f"몫 = {integer // binary}, 나머지 = {integer % binary}")
    if binary > 10:
        result += str(hex(integer % binary)[2])
    else:
        result += str(integer % binary)
    integer = integer // binary
    count += 1

result = result[::-1]

if decimal != 0:
    count = 0
    result += "."
    while decimal != 0 and count < 30: # 소수가 0이 될 때까지, count(한계)가 30이 될 때까지 반복
        decimal = float(f"{decimal * binary:.10f}")
        if decimal >= 1:
            print(decimal)
            result += str(hex(int(decimal)))[2]
            decimal -= int(decimal)
        elif decimal < 1:
            print(decimal)
            result += str(int(decimal))
        print("X 2\n——————————")
        count += 1

if count == 30: # count(한계)가 30이 되었을 경우
    result += "..." # 결과값 뒤에 "..."붙이기

print(result.upper()) # 결과값 출력
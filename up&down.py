import random
ran = random.randint(1, 100)

cnt = 0
while True:
    input_data = int(input("1에서 100중에서 원하는 숫자를 입력하세요"))
    if ran > input_data:
        print("up")
        cnt += 1
    elif ran < input_data:
        print("down")
        cnt += 1
    else:
        print("정답입니다")
        print(cnt + 1, "번만에 정답을 맞히셨습니다")
        break

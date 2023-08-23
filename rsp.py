import random

ran = ['가위', '바위', '보']

computer = random.choice(ran)
player = input('무엇을 내시겠습니까? ')

print('컴퓨터 :', computer, '플레이어 :', player)
if player == computer:
    print('비겼습니다')
elif (player == '가위' and computer == '보' or
      player == '바위' and computer == '가위' or
      player == '보' and computer == '바위'):
    print('이겼습니다')
else:
    print('졌습니다')

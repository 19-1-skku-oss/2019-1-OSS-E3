"""pong.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Pong, classic arcade game.                                   # Pong, 클래식 아케이드 게임

Excercises                                                      # 연습문제들

1. Change the colors.                                           # 1. pong에서 색깔을 어떻게 수정하느냐
2. What is the frame rate? Make it faster or slower.            # 2. 프레임의 속도는 어떤가? 이를 수정해보라
3. Change the speed of the ball.                                # 3. 공의 속도를 수정해보라
4. Change the size of the paddles.                              # 4. 페달의 사이즈를 수정해보라
5. Change how the ball bounces off walls.                       # 5. 공이 벽을 넘어갔을 때 어떻게 되는지를 수정하라
6. How would you add a computer player?                         # 6. 컴퓨터 플레이어를 어떻게 추가할까?
6. Add a second ball.                                           # 7. 두번째 공을 추가해보라

"""

from random import choice, random                               # 랜덤 모듈에서 choice와 random을 불러온다.
from turtle import *                                            # 터틀 모듈을 불러온다.
from freegames import vector                                    # freegames util.py에서 선언된 vector를 불러온다.

global round
round = 0

def value():                                                    # value() 함수
    "Randomly generate value between (-5, -3) or (3, 5)."       # 위 함수는 (-5,-3) 또는 (3,5) 중의 값을 랜덤으로 불러온다.
    return ((2+round) + random() * 3) * choice([1, -1]) 

ball = vector(0, 0)                                             # 처음 공의 벡터를 0으로 설정한다.
aim = vector(value(), value())                                  # 공의 진행방향을 vector(value(),value())로 초기화한다.
state = {1: 0, 2: 0}                                            # 1과 2의 상태를 0으로 초기화한다.

def move(player, change):                                       # move(player, change) 함수
    "Move player position by change."                           # 각 플레이어의 페달의 포지션을 move함수를 통해 바꿔준다.
                                                                # player = 1일때 : 왼쪽 페달, player = 2일때 : 오른쪽 페달
    state[player] += change                                     # change만큼 state[player]를 증가시킨다. (페달의 y좌표)

def rectangle(x, y, width, height):                             # rectangle(x, y, width, height) 함수
    "Draw rectangle at (x, y) with given width and height."     # 이 함수는 게임판을 초기화하는 함수이다.
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    "Draw game and move pong ball."
    clear()
    rectangle(-200, state[1], 10, 50)                           # 위의 rectangle을 이용해 함수를 초기화한다. (-200,-200) ~ (200,200) 까지 활성화
    rectangle(190, state[2], 10, 50)

    ball.move(aim)                                              # ball의 aim을 초기화 시켜주고
    x = ball.x                                                  # 그에 따라 ball의 x, y 벡터가 설정된다.
    y = ball.y

    up()                                                        # 구현하기 위한 환경설정
    goto(x, y)
    dot(10)
    update()

    if y < -200 or y > 200:                                     # ball의 y좌표가 200 초과 또는 -200 미만이 되면 aim.y를 -aim.y로 바꾼다.
        aim.y = -aim.y

    if x < -185:                                                # x가 -185 미만이 되면 일때는 되면 high는 state[1] 이고 low는 state[1] + 50이다 (즉 판의 길이가 50임)
        low = state[1]                                          
        high = state[1] + 50

        if low <= y <= high:                                    # 만약 y좌표가 low와 high 사이에 있으면, 공의 방향을 오른쪽으로 바꾼다. (즉 튕겨나감)
            aim.x = -aim.x
        else:
            return                                              # 아니면 게임 종료

    if x > 185:
        low = state[2]                                          # x가 185 초과일 때, 위의 경우와 같은 케이스로 처리
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    ontimer(draw, 50)                                           # draw함수를 0.05초 뒤에 실행한다. 즉 draw함수는 0.05초마다 계속 갱신되는 재귀함수임.

setup(420, 420, 370, 0)                                         # setuptool에서 제공하는 setup()함수임.
hideturtle()                                                    # 거북이를 화면에서 숨긴다.
tracer(False)
listen()
onkey(lambda: move(1, 20), 'w')                                 # w - 왼쪽 페달을 20 올림, s - 왼쪽 페달을 20 내림, i - 오른쪽 페달을 20 올림, k - 오른쪽 페달을 20 내림
onkey(lambda: move(1, -20), 's')
onkey(lambda: move(2, 20), 'i')
onkey(lambda: move(2, -20), 'k')
draw()                                                          # draw() 시작해줌
done()                                                          # draw()가 종료되면 done() 해줌.


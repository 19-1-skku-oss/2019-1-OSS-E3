"""bounce.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Bounce, a simple animation demo.                             # Bounce, 간단한 애니메이션 데모

Exercises                                                       # 연습문제들

1. Make the ball speed up and down.                             # 1. 공의 속도를 빠르거나 느리게 만들자
2. Change how the ball bounces when it hits a wall.             # 2. 공이 벽이랑 부딪힐때 튀기는 방법을 바꿔보자
3. Make the ball leave a trail.                                 # 3. 공이 이동하면서 자취를 남기도록 해보자
4. Change the ball color based on position.                     # 4. 위치에 따른 공의 색깔을 바꿔보자
   Hint: colormode(255); color(0, 100, 200)                     

"""

from random import *                                            # random 모듈을 불러온다    
from turtle import *                                            # turtle 모듈을 불러온다
from freegames import vector                                    # freegames utils.py에서 선언된 vector를 불러온다

def value():                                                    # (-5, -3) 그리고 (3, 5) 사이에만 있는 랜덤한 수를 생성하는 함수
    "Randomly generate value between (-5, -3) or (3, 5)."
    return (3 + random() * 2) * choice([1, -1])

ball = vector(0, 0)                                             # 공의 초기 좌표를 (0, 0)으로 설정해준다
aim = vector(value(), value())                                  # aim의 초기 좌표는 value 함수에서 구한 랜덤 값을 각각 x좌표와 y좌표에 넣어준다

def draw():                                                     # 공을 움직여주고 그 화면을 나타내주는 함수
    "Move ball and draw game."
    ball.move(aim)                                              # 공을 aim에 설정되있는 좌표만큼 움직여준다

    x = ball.x                                                  # x와 y를 ball.x와 ball.y 값으로 설정해준다    
    y = ball.y

    if x < -200 or x > 200:                                     # 만약 x가 -200보다 작거나 200보다 크면 aim의 x좌표의 부호를 바꿔준다        
        aim.x = -aim.x

    if y < -200 or y > 200:
        aim.y = -aim.y

    clear()
    goto(x, y)
    dot(10)

    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
up()
draw()
done()

"""Maze.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Maze, move from one side to another.                         # Maze, 한쪽으로 부터 다른쪽으로 이동한다


Excercises                                                      # 연습문제들

1. Keep score by counting taps.                                 # 1. tap들을 세면서 점수를 계속 매기자
2. Make the maze harder.                                        # 2. maze를 좀 더 어렵게 만들자
3. Generate the same maze twice.                                # 3. 똑같은 maze를 두배 키워서 생성하자

"""

from turtle import *                                            # 터틀 모듈을 불러온다
from random import random                                       # random 모듈에서 random 함수를 불러온다
from freegames import line                                      # freegames utils.py에서 선언된 line을 불러온다

def draw():                                                     # maze를 그리는 함수
    "Draw maze."                                                # 너비는 5로 하고 색깔은 검은색으로 해준다
    color('black')                          
    width(5)

    for x in range(-200, 200, 40):                              # 각각 x와 y를 (-200, 200) 사이의 40간격으로 for문을 돌리고
        for y in range(-200, 200, 40):                          # random 함수를 통해 나온 값이 0.5보다 크면 (x, y)에서 (x + 40, y + 40)까지 직선을 그리고
            if random() > 0.5:                                  # 값이 0.5보다 작거나 같으면 (x, y + 40)에서 (x + 40, y)까지 직선을 그려준다
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()                                                    # 화면을 갱신해준다

def tap(x, y):                                                  # 
    "Draw line and dot for screen tap."
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()

    width(2)
    color('red')
    goto(x, y)
    dot(4)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()

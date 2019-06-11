"""Paint.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Paint, for drawing shapes.                                   # Paint, 모양을 그리기 위한 게임

Exercises                                                       # 연습문제들

1. Add a color.                                                 # 1. 색깔을 추가하자
2. Complete circle.                                             # 2. 원을 완성하자
3. Complete rectangle.                                          # 3. 직사각형을 완성하자
4. Complete triangle.                                           # 4. 삼각형을 완성하자
5. Add width parameter.                                         # 5. 너비 변수를 추가하자

"""

from turtle import *                                            # turtle 모듈을 불러온다
from freegames import vector                                    # freegames utils.py에서 선언된 vector를 불러온다

def line(start, end):                                           # 시작점부터 끝점까지 직선을 그리는 함수
    "Draw line from start to end."                              # 펜을 들어 시작점으로 이동해서 그 곳에서부터 그리기 시작해서 끝점까지 이동하여 직선을 그려준다
    up()                                                        
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):                                         # 시작점부터 끝점까지 사각형을 그리는 함수
    "Draw square from start to end."                            # 펜을 들어 시작점으로 이동해서 사각형의 네 모서리를 돌면서 색을 채워준다
    up()                                                        # 색 채우기가 완료되면 작업을 끝내준다
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):                                         #
    "Draw circle from start to end."
    pass  # TODO

def rectangle(start, end):
    "Draw rectangle from start to end."
    pass  # TODO

def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()

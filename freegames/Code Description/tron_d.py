"""Tron.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Tron, classic arcade game.                                   # Tron, 클래식 아케이드 게임
  
Exercises                                                       # 연습문제들

1. Make the tron players faster/slower.                         # 1. tron 플레이어들의 속도를 빠르게/느리게 만들자
2. Stop a tron player from running into itself.                 # 2. tron 플레이어가 스스로 뛰어드는 것을 막자
3. Allow the tron player to go around the edge of the screen.   # 3. tron 플레이어가 화면의 가장자리를 돌아다닐 수 있게 허용하자 
4. How would you create a computer player?                      # 4. 컴퓨터 플레이어는 어떻게 만들 수 있을까?

"""

from turtle import *                                            # turtle 모듈을 불러온다
from freegames import square, vector                            # freegames utils.py에서 선언된 square와 vector를 불러온다

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def inside(head):
    "Return True if head inside screen."
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():
    "Advance players and draw game."
    p1xy.move(p1aim)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    p2head = p2xy.copy()

    if not inside(p1head) or p1head in p2body:
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:
        print('Player red wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 50)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()
done()

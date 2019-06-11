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

p1xy = vector(-100, 0)                                          # p1xy는 초기 좌표를 (-100, 0)으로 설정해준다
p1aim = vector(4, 0)                                            # p1aim은 초기 좌표를 (4, 0)으로 설정해준다
p1body = set()                                                  # p1body를 집합 자료형인 set으로 설정해준다

p2xy = vector(100, 0)                                           # p1xy는 초기 좌표를 (-100, 0)으로 설정해준다                                            # p1aim은 초기 좌표를 (4, 0)으로 설정해준다                                              # p1body를 집합 자료형은 set으로 설정해준다
p2aim = vector(-4, 0)                                           # p2aim은 초기 좌표를 (-4, 0)으로 설정해준다
p2body = set()                                                  # p2body를 집합 자료형인 set으로 설정해준다

def inside(head):                                               # tron의 head의 범위를 제한해주는 함수
    "Return True if head inside screen."                        # head의 x와 y좌표를 각각 (-200, 200) 사이로 제한해준다
    return -200 < head.x < 200 and -200 < head.y < 200

def draw():                                                     # 플레이어들을 진행시키고 화면에 그려주는 함수
    "Advance players and draw game."
    p1xy.move(p1aim)                                            # p1xy좌표를 p1aim에 설정되있는 좌표만큼 움직여준다
    p1head = p1xy.copy()                                        # p1xy의 복사본을 만들고 그것을 p1head라고 선언해준다

    p2xy.move(p2aim)                                            # p2xy좌표를 p2aim에 설정되있는 좌표만큼 움직여준다
    p2head = p2xy.copy()                                        # p2xy의 복사본을 만들고 그것을 p2head라고 선언해준다

    if not inside(p1head) or p1head in p2body:                  # p1head가 범위를 벗어나거나 p2body에 부딪히면 함수를 종료시킨다
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body:                  # p2head가 범위를 벗어나거나 p1body에 부딪히면 함수를 종료시킨다
        print('Player red wins!')
        return

    p1body.add(p1head)                                          # 아까 복사해서 만들었던 p1head를 p1body에 추가시켜준다
    p2body.add(p2head)                                          # 아까 복사해서 만들었던 p2head를 p2body에 추가시켜준다

    square(p1xy.x, p1xy.y, 3, 'red')                            # p1xy가 지나가는 곳에는 빨간색 정사각형을 그려준다
    square(p2xy.x, p2xy.y, 3, 'blue')                           # p2xy가 지나가는 곳에는 파란색 정사각형을 그려준다
    update()                                                    # 화면을 갱신해준다
    ontimer(draw, 50)                                           # 50ms 마다 draw 함수가 실행되도록 해준다

setup(420, 420, 370, 0)                                         # 초기 그래픽 설정을 해준다
hideturtle()                                                    # turtle 모듈의 거북이를 숨겨준다
tracer(False)                                                   # 거북이가 움직이는 자취를 숨겨준다
listen()                                                        # 사용자가 입력하는 키의 입력을 받아준다
onkey(lambda: p1aim.rotate(90), 'a')                            # p1aim에서 'a'는 왼쪽, 'd'는 오른쪽으로 꺾이게 해주고
onkey(lambda: p1aim.rotate(-90), 'd')                           # p2aim에서 'j'는 왼쪽, 'l'는 오른쪽으로 꺾이게 해준다
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')
draw()                                                          # 화면에 그림을 그려준다
done()                                                          # turtle 모듈을 종료 시켜준다  

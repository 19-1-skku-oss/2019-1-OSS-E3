"""snake.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Snake, classic arcade game.                                  #Snake, 클래식 아케이드 게임

Excercises                                                      # 연습문제들

1. How do you make the snake faster or slower?                  # 1. snake를 어떻게 하면 빠르거나 느리게 만들 수 있을까?
2. How can you make the snake go around the edges?              # 2. 어떻게 snake가 가장자리를 돌게 만들 수 있을까?
3. How would you move the food?                                 # 3. 먹이는 어떻게 움직일 수 있을까?
4. Change the snake to respond to arrow keys.                   # 4. 방향키에 맞게 snake를 바꾸자

"""

from turtle import *                                            # 터틀 모듈을 불러온다
from random import randrange                                    # random 모듈에서 randrange 함수를 불러온다
from freegames import square, vector                            # freegames utils.py에서 선언된 square와 vector를 불러온다

food = vector(0, 0)                                             # 먹이는 움직이지 않도록 벡터를 (0, 0)으로 설정한다
snake = [vector(10, 0)]                                         # snake는 길이가 유동적으로 늘어나고 줄어들어야 하므로 리스트형으로 만들고 머리의 벡터를 (10, 0)으로 설정한다
aim = vector(0, -10)                                            # aim은 snake의 방향을 위한 것이고 초기 설정은 벡터에 (0, -10)을 대입해서 아래쪽으로 내려가는 방향이 되도록 한다 

def change(x, y):                                               # snake의 방향을 정하는 change 함수
    "Change snake direction."                                   # aim vector의 x값과 y값 재설정 해준다    
    aim.x = x
    aim.y = y

def inside(head):                                               # snake의 head의 범위를 제한해주는 inside 함수
    "Return True if head inside boundaries."                    # head의 x와 y좌표 모두 (-200, 100) 사이에 있게 한다
    return -200 < head.x < 190 and -200 < head.y < 190

def move():                                                     # snake를 움직이는 move 함수
    "Move snake forward one segment."
    head = snake[-1].copy()                                     # snake의 리스트에 복사해서 뒤에 추가해준다
    head.move(aim)                                              # head를 aim의 vector를 이용해서 움직여준다

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'gold')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()


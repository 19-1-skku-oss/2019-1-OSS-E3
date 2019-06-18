"""snake.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Snake, classic arcade game.                                  # Snake, 클래식 아케이드 게임

Excercises                                                      # 연습문제들

1. How do you make the snake faster or slower?                  # 1. snake를 어떻게 하면 빠르거나 느리게 만들 수 있을까?
2. How can you make the snake go around the edges?              # 2. 어떻게 snake가 가장자리를 돌게 만들 수 있을까?
3. How would you move the food?                                 # 3. food는 어떻게 움직일 수 있을까?
4. Change the snake to respond to arrow keys.                   # 4. 방향키에 맞게 snake를 바꾸자

"""

from turtle import *                                            # 터틀 모듈을 불러온다
from random import randrange                                    # random 모듈에서 randrange 함수를 불러온다
from freegames import square, vector                            # freegames utils.py에서 선언된 square와 vector를 불러온다

food = vector(0, 0)                                             # food는 초기 좌표를 (0, 0)으로 설정해준다
snake = [vector(10, 0)]                                         # snake는 길이가 유동적으로 늘어나고 줄어들어야 하므로 리스트형으로 만들고 초기 좌표를 (10, 0)으로 설정해준다
aim = vector(0, -10)                                            # aim은 snake의 방향을 위한 것이고 초기 좌표는 (0, -10)으로 설정해서 아래쪽으로 내려가는 방향이 되도록 한다 

def change(x, y):                                               # snake의 방향을 정하는 change 함수
    "Change snake direction."                                   # aim 좌표의 x값과 y값을 재설정 해준다    
    aim.x = x
    aim.y = y

def inside(head):                                               # snake의 head의 범위를 제한해주는 inside 함수
    "Return True if head inside boundaries."                    # head의 x와 y좌표 모두 (-200, 190) 사이에 있게 한다
    return -200 < head.x < 190 and -200 < head.y < 190

def move():                                                     # snake를 움직이는 move 함수
    "Move snake forward one segment."                           # head를 snake 리스트의 마지막값의 복사본으로 만들어준다
    head = snake[-1].copy()                                     # head를 aim의 vector를 이용해서 움직여준다
    head.move(aim)                                              

    if not inside(head) or head in snake:                       # head가 범위를 벗어나거나 head가 snake의 몸통과 부딫힐 경우
        square(head.x, head.y, 9, 'red')                        # 길이가 9인 정사각형을 왼쪽 아래 꼭지점이 (head.x, head.y)가 되도록 또한 빨간색으로 채워지도록 한다
        update()                                                # 새로 적용한 애니메이션이 나오도록 화면을 갱신하고 if 문에 들어온 경우 함수를 종료시킨다
        return

    snake.append(head)                                          # snake의 리스트 뒤에 head를 추가해준다

    if head == food:                                            # 만약 head가 food와 만난 경우
        print('Snake:', len(snake))                             # 'Snake: '와 함께 그 길이가 몇 인지 출력하도록 하고
        food.x = randrange(-15, 15) * 10                        # food.x와 food.y를 다시 지정해준다
        food.y = randrange(-15, 15) * 10
    else:                                                       # head와 food가 만나지 않으면 snake의 리스트에서 0번째 값을 제거해준다
        snake.pop(0)

    clear()                                                     # turtle 모듈의 함수인데 거북이를 그대로 둔 채 화면을 지워준다

    for body in snake:                                          # snake 리스트에서 Iterator 'body'를 설정하고
        square(body.x, body.y, 9, 'black')                      # snake 리스트의 점들이 만들어내는 정사각형을 검은색으로 칠해준다

    square(food.x, food.y, 9, 'green')                          # food가 있는 곳의 정사각형은 초록색으로 칠해준다
    update()                                                    # 위와 마찬가지로 화면을 갱신해준다
    ontimer(move, 100)                                          # 100ms 마다 move 함수가 실행되도록 해준다

setup(420, 420, 370, 0)                                         # 초기 그래픽 설정을 해준다
hideturtle()                                                    # turtle 모듈의 거북이를 숨겨준다    
tracer(False)                                                   # 거북이가 움직이는 자취를 숨겨준다
listen()                                                        # 사용자가 입력하는 키의 입력을 받아준다
onkey(lambda: change(10, 0), 'Right')                           # 누르는 키에 맞게 각각 오른쪽, 왼쪽, 위, 아래 방향을 설정해준다
onkey(lambda: change(-10, 0), 'Left')                           
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()                                                          # 키에 따라 움직이도록 move 함수를 실행시켜준다            
done()                                                          # turtle 모듈을 종료시켜준다


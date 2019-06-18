"""Flappy.py를 한국어로 알기 쉽게 설명하는 파일"""

"""Flappy, game inspired by Flappy Bird.

Exercises                                                 #연습문제 

1. Keep score.                                     #1. 점수를 계속 보여주게 하자 
2. Vary the speed.                                 #2. 속도를 다양하게 해보자    
3. Vary the size of the balls.                     #3. 공의 크기를 다양하게 해보자  
4. Allow the bird to move forward and back.        #4. 새가 앞 뒤로 움직일 수 있게 해보자 

"""

from random import *
from turtle import *
from freegames import vector

bird = vector(0, 0)                                          #새의 위치 초기 설정 
balls = []

def tap(x, y):                                    #새의 위치를 위로 이동시키는 함수 
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def inside(point):                                #점이 스크린에 있으면 참을 반환 
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):                                 #새의 생사에 따라 색깔 변경
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

def move():                                     #공의 위치를 업데이트해주는 함수 
    "Update object positions."
    bird.y -= 5

    for ball in balls:                          #공의 위치를 왼쪽으로 이동 
        ball.x -= 3

    if randrange(10) == 0:                       #화면 왼쪽끝에 다다르면 오른쪽 끝으로 이동 
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):        
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)

setup(420, 420, 370, 0) 
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

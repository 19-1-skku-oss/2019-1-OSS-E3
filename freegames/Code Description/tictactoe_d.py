"""Tic Tac Toe.py를 한국어로 알기 쉽게 설명하는 파일""" 

"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.                   #X와 O에 다른 색깔과 너비로 설정하세요
2. What happens when someone taps a taken spot?                    #다른 사람이 이미 탭한 곳을 탭하면 무슨 일이 발생할까요?
3. How would you detect when someone has won?                      #누가 이겼는지 어떻게 알까요?
4. How could you create a computer player?                         #컴퓨터 플레이어는 어떻게 만들 수 있을까요?

"""

from turtle import *
from freegames import line

def grid():                                                        #격자 그리기
    "Draw tic-tac-toe grid."
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):                                                   #x 그리기
    "Draw X player."
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):                                                   #o 그리기
    "Draw O player."
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):                                                  #133크기 정사각형에 격자크기 맞추기
    "Round value down to grid with square size 133."
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0}
players = [drawx, drawo]

def tap(x, y):                                                     #탭한 사각형에 X 또는 O 그리기
    "Draw X or O in tapped square."
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

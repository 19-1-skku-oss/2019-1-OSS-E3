"""connect.py를 한국어로 알기 쉽게 설명하는 파일"""  



"""Connect Four Exercises                                           # 연습문제

1. Change the colors.                                               # 1. 색깔을 바꿔보세요.
2. Draw squares instead of circles for open spaces.                 # 2. 빈공간에 원을 대신해 사각형을 그려보세요.
3. Add logic to detect a full row.                                  # 3. 꽉 찬 열을 판단하는 코드를 작성해 보세요.
4. Create a random computer player.                                 # 4. 가상의 컴퓨터 플레이어를 만들어보세요.
5. How would you detect a winner?                                   # 5. 어떻게하면 승자를 판단할 수 있을까요?                

"""

from turtle import *                                                # turrtle 모듈을 불러온다    
from freegames import line                                          # freegames 모듈에서 line함수를 불러온다            

turns = {'red': 'yellow', 'yellow': 'red'}                          # 색깔 바꾸기를 위한 색 선언
state = {'player': 'yellow', 'rows': [0] * 8}                       # 현재 플레이어의 색 상태 표시

def grid():                                         
    "Draw Connect Four grid."                                       # 배경이 되는 판 그리기 함수
    bgcolor('light blue')                                           # 배경색 설정

    for x in range(-150, 200, 50):                                  #
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):                                  #
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()

def tap(x, y):                                                      # 사용자에게 입력받았을 때의 동작 
    "Draw red or yellow circle in tapped row."                      #
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    rows[row] = count + 1
    state['player'] = turns[player]

setup(420, 420, 370, 0)                                             #  
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()

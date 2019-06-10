"""snake.py를 한국어로 알기 쉽게 설명하는 파일"""            


"""Tiles, number swapping game                          # Tiles, 숫자바꾸기 게임

Exercises                                               # 연습문제

1. Track a score by the number of tile moves.           # 1. 타일 이동 횟수로 점수를 획득합니다.
2. Permit diagonal squares as neighbors.                # 2. 대각선을 이동을 허용하십시오.
3. Respond to arrow keys instead of mouse clicks.       # 3. 마우스 클릭 대신 화살표 키를 이용해보세요.
4. Make the grid bigger.                                # 4. 숫자판를 더 크게 만듭니다.

"""

from random import *                                    # random 모듈을 불러온다        
from turtle import *                                    # turtle 모듈을 불러온다
from freegames import floor, vector                     # freegames 모듈에서 floor, vector함수를 불러온다.

tiles = {}                                              # 타일들을 위한 배열 선언
neighbors = [                                           # 인접 타일 관리를 위한 배열 선언
    vector(100, 0),                                     # 오른쪽 인접 타일
    vector(-100, 0),                                    # 왼쪽 인접 타일
    vector(0, 100),                                     # 위쪽 인접 타일
    vector(0, -100),                                    # 아래쪽 인접 타일
]

def load():                                             
    "Load tiles and scramble."                          # 타일들을 불러오는 함수
    count = 1

    for y in range(-200, 200, 100):                     # 타일 바깥의 윤곽선 그리기
        for x in range(-200, 200, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None

    for count in range(1000):                           # 타일 로딩하기
        neighbor = choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot

def square(mark, number):
    "Draw white square with black outline and number."  # 흰색 정사각형과 검정 윤곽선을 그린다.
    up()
    goto(mark.x, mark.y)
    down()

    color('black', 'white')
    begin_fill()                                             
    for count in range(4):                              # 검정 윤곽선 그리기
        forward(99)
        left(90)
    end_fill()

    if number is None:                                  # 깔끔한 인터페이스를 위한 그리기 설정
        return
    elif number < 10:                                            
        forward(20)

    write(number, font=('Arial', 60, 'normal'))         # 글씨 폰트, 크기 설정

def tap(x, y):                                          # 사용자의 입력을 받았을 때의 동작을 설정하는 함수
    "Swap tile and empty square."                       # 빈 정사각형과 타일을 바꾼다.
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    for neighbor in neighbors:                          # 인접 타일 swap을 위한 for문
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:       # 인접타일이 빈 정사각형일 때 swap
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)

def draw():                                             
    "Draw all tiles."                                   # 모든 타일을 그린다.
    for mark in tiles:                                  
        square(mark, tiles[mark])
    update()

setup(420, 420, 370, 0)                                 # 인터페이스 크기 설정
hideturtle()                                            # turtle 숨기기
tracer(False)
load()                                                  # 인터페이스 로딩
draw()                                                  # 타일 그리기
onscreenclick(tap)                                      # 사용자입력 설정
done()

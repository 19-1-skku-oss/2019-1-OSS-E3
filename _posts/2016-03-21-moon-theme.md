---
layout: post
title:  "Various Games"
date:   2019-06-09
excerpt: "python games."
project: true
tag:
- jekyll 
- moon
- blog
- about
- theme
comments: true
---

![Moon Homepage](https://cloud.githubusercontent.com/assets/754514/14509720/61c61058-01d6-11e6-93ab-0918515ecd56.png)    
    
<center><b>Moon</b> is a minimal, one column jekyll theme.</center>
 
 이 프로젝트 페이지는 저희가 **수정** 혹은 **기여**한 파이썬 코드들을 정리한 곳입니다. 
 <br>
 <br>
 
## **김민수**
### *Maze*

#### original code

    """
    Maze, move from one side to another.
    Excercises
    1. Keep score by counting taps.
    2. Make the maze harder.
    3. Generate the same maze twice.
    """

    from turtle import *
    from random import random
    from freegames import line
    
    def draw():
    "Draw maze."
    color('black')
    width(5)
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()

    def tap(x, y):
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

#### 코드에 대한 소개 추가

    



### *pong*
#### <original code>
  
    """Pong, classic arcade game.
    Exercises
    1. Change the colors.
    2. What is the frame rate? Make it faster or slower.
    3. Change the speed of the ball.
    4. Change the size of the paddles.
    5. Change how the ball bounces off walls.
    6. How would you add a computer player?
    6. Add a second ball.
    """
    
    from random import choice, random
    from turtle import *
    from freegames import vector
    
    def value():
     "Randomly generate value between (-5, -3) or (3, 5)."
      return (3 + random() * 2) * choice([1, -1])
    
    ball = vector(0, 0)
    aim = vector(value(), value())
    state = {1: 0, 2: 0}
    
    def move(player, change):
        "Move player position by change."
        state[player] += change
    
    def rectangle(x, y, width, height):
       "Draw rectangle at (x, y) with given width and height."
       up()
       goto(x, y)
        down()
       begin_fill()
      for count in range(2):
           forward(width)
            left(90)
            forward(height)
         left(90)
        end_fill()
    
    def draw():
        "Draw game and move pong ball."
       clear()
       rectangle(-200, state[1], 10, 50)
       rectangle(190, state[2], 10, 50)
    
      ball.move(aim)
      x = ball.x
      y = ball.y
    
      up()
      goto(x, y)
      dot(10)
       update()
    
    if y < -200 or y > 200:
        aim.y = -aim.y
    
    if x < -185:
        low = state[1]
        high = state[1] + 50
    
        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    ontimer(draw, 50)

    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: move(1, 20), 'w')
    onkey(lambda: move(1, -20), 's')
    onkey(lambda: move(2, 20), 'i')
    onkey(lambda: move(2, -20), 'k')
    draw()
    done()

#### 코드에 대한 소개 추가

    """Pong, classic arcade game.                                   # Pong, 클래식 아케이드 게임
    Excercises                                                      # 연습문제들
    1. Change the colors.                                           # 1. pong에서 색깔을 어떻게 수정하느냐
    2. What is the frame rate? Make it faster or slower.            # 2. 프레임의 속도는 어떤가? 이를 수정해보라
    3. Change the speed of the ball.                                # 3. 공의 속도를 수정해보라
    4. Change the size of the paddles.                              # 4. 페달의 사이즈를 수정해보라
    5. Change how the ball bounces off walls.                       # 5. 공이 벽을 넘어갔을 때 어떻게 되는지를 수정하라
    6. How would you add a computer player?                         # 6. 컴퓨터 플레이어를 어떻게 추가할까?
    6. Add a second ball.                                           # 7. 두번째 공을 추가해보라
    """
    
    from random import choice, random                               # 랜덤 모듈에서 choice와 random을 불러온다.
    from turtle import *                                            # 터틀 모듈을 불러온다.
    from freegames import vector                                    # freegames util.py에서 선언된 vector를 불러온다.
    
    global round
    round = 0
    
    def value():                                                    # value() 함수
        "Randomly generate value between (-5, -3) or (3, 5)."       # 위 함수는 (-5,-3) 또는 (3,5) 중의 값을 랜덤으로 불러온다.
        return ((2+round) + random() * 3) * choice([1, -1]) 
    
    ball = vector(0, 0)                                             # 처음 공의 벡터를 0으로 설정한다.
    aim = vector(value(), value())                                  # 공의 진행방향을 vector(value(),value())로 초기화한다.
    state = {1: 0, 2: 0}                                            # 1과 2의 상태를 0으로 초기화한다.
    
    def move(player, change):                                       # move(player, change) 함수
        "Move player position by change."                           # 각 플레이어의 페달의 포지션을 move함수를 통해 바꿔준다.
                                                                   # player = 1일때 : 왼쪽 페달, player = 2일때 : 오른쪽 페달
    state[player] += change                                     # change만큼 state[player]를 증가시킨다. (페달의 y좌표)
    
    def rectangle(x, y, width, height):                             # rectangle(x, y, width, height) 함수
        "Draw rectangle at (x, y) with given width and height."     # 이 함수는 게임판을 초기화하는 함수이다.
        up()
       goto(x, y)
       down()
       begin_fill()
       for count in range(2):
           forward(width)
            left(90)
           forward(height)
           left(90)
        end_fill()
    
    def draw():
        "Draw game and move pong ball."
        clear()
        rectangle(-200, state[1], 10, 50)                           # 위의 rectangle을 이용해 함수를 초기화한다. (-200,-200) ~ (200,200)  까지 활성화
        rectangle(190, state[2], 10, 50)
    
        ball.move(aim)                                              # ball의 aim을 초기화 시켜주고
       x = ball.x                                                  # 그에 따라 ball의 x, y 벡터가 설정된다.
       y = ball.y
    
       up()                                                        # 구현하기 위한 환경설정
       goto(x, y)
       dot(10)
       update()
    
        if y < -200 or y > 200:                                     # ball의 y좌표가 200 초과 또는 -200 미만이 되면 aim.y를 -aim.y로 바꾼다.
          aim.y = -aim.y

        if x < -185:                                                # x가 -185 미만이 되면 일때는 되면 high는 state[1] 이고 low는 state[1] + 50이다 (즉 판의 길이가 50임)
           low = state[1]                                          
           high = state[1] + 50
    
            if low <= y <= high:                                    # 만약 y좌표가 low와 high 사이에 있으면, 공의 방향을 오른쪽으로 바꾼다. (즉 튕겨나감)
               aim.x = -aim.x
           else:
               return                                              # 아니면 게임 종료
    
        if x > 185:
            low = state[2]                                          # x가 185 초과일 때, 위의 경우와 같은 케이스로 처리
            high = state[2] + 50
    
            if low <= y <= high:
              aim.x = -aim.x
          else:
              return
    
       ontimer(draw, 50)                                           # draw함수를 0.05초 뒤에 실행한다. 즉 draw함수는 0.05초마다 계속 갱신되는 재귀함수임.
    
    setup(420, 420, 370, 0)                                         # setuptool에서 제공하는 setup()함수임.
    hideturtle()                                                    # 거북이를 화면에서 숨긴다.
    tracer(False)
    listen()
    onkey(lambda: move(1, 20), 'w')                                 # w - 왼쪽 페달을 20 올림, s - 왼쪽 페달을 20 내림, i - 오른쪽 페달을 20 올림, k - 오른쪽 페달을 20 내림
    onkey(lambda: move(1, -20), 's')
    onkey(lambda: move(2, 20), 'i')
    onkey(lambda: move(2, -20), 'k')
    draw()                                                          # draw() 시작해줌
    done()                                                          # draw()가 종료되면 done() 해줌.

    

 <br>
 <br>

## **박정재**
### *Snake*

#### original code
    
    """Snake, classic arcade game.
    Excercises
    1. How do you make the snake faster or slower?
    2. How can you make the snake go around the edges?
    3. How would you move the food?
    4. Change the snake to respond to arrow keys.
    """
    
    from turtle import *
    from random import randrange
    from freegames import square, vector
    
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    
    def change(x, y):
       "Change snake direction."
       aim.x = x
        aim.y = y
    
    def inside(head):
        "Return True if head inside boundaries."
        return -200 < head.x < 190 and -200 < head.y < 190
    
    def move():
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)
    
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
    
       square(food.x, food.y, 9, 'green')
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

#### 코드에 대한 소개 추가

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
    snake = [vector(10, 0)]                                         # snake는 길이가 유동적으로 늘어나고 줄어들어야 하므로 리스트형으로 만들 고 초기 좌표를 (10, 0)으로 설정해준다
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
    onkey(lambda: change(10, 0), 'Right')                           # 오른쪽, 왼쪽, 위, 아래 각 키에 맞게 방향을 설정해준다
    onkey(lambda: change(-10, 0), 'Left')                           
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()                                                          # 키에 따라 움직이도록 move 함수를 실행시켜준다            
    done()                                                          # turtle 모듈을 종료시켜준다

#### modified code (기능 수정 및 추가)
    
    """Snake, classic arcade game.
    Excercises
    1. How do you make the snake faster or slower?
    2. How can you make the snake go around the edges?
    3. How would you move the food?
    4. Change the snake to respond to arrow keys.
    """
    
    from turtle import *
    from random import randrange
    from freegames import square, vector
    
    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    
    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y
    
    def inside(head):
       "Return True if head inside boundaries."
      return -200 < head.x < 190 and -200 < head.y < 190
    
    def move():
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)
    
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


 <br>
 <br>

## **유재원**
### *Flappy*

#### original code

    """Flappy, game inspired by Flappy Bird.
    Exercises
    1. Keep score.
    2. Vary the speed.
    3. Vary the size of the balls.
    4. Allow the bird to move forward and back.
    """
    
    from random import *
    from turtle import *
    from freegames import vector
    
    bird = vector(0, 0)
    balls = []
    
    def tap(x, y):
        "Move bird up in response to screen tap."
        up = vector(0, 30)
        bird.move(up)
    
    def inside(point):
        "Return True if point on screen."
        return -200 < point.x < 200 and -200 < point.y < 200
    
    def draw(alive):
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
    
    def move():
        "Update object positions."
       bird.y -= 5
    
        for ball in balls:
            ball.x -= 3
    
       if randrange(10) == 0:
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

#### 코드에 대한 소개 추가

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


 <br>
 <br>

## **이재웅**
### *Tiles*

#### original code

    """Tiles, number swapping game.
    Exercises
    1. Track a score by the number of tile moves.
    2. Permit diagonal squares as neighbors.
    3. Respond to arrow keys instead of mouse clicks.
    4. Make the grid bigger.
    """
    
    from random import *
    from turtle import *
    from freegames import floor, vector
    
    tiles = {}
    neighbors = [
        vector(100, 0),
        vector(-100, 0),
       vector(0, 100),
       vector(0, -100),
    ]
    
    def load():
     "Load tiles and scramble."
     count = 1
    
      for y in range(-200, 200, 100):
         for x in range(-200, 200, 100):
             mark = vector(x, y)
             tiles[mark] = count
             count += 1
    
     tiles[mark] = None
    
      for count in range(1000):
            neighbor = choice(neighbors)
           spot = mark + neighbor
    
            if spot in tiles:
                number = tiles[spot]
             tiles[spot] = None
             tiles[mark] = number
             mark = spot
    
    def square(mark, number):
       "Draw white square with black outline and number."
       up()
       goto(mark.x, mark.y)
       down()
    
       color('black', 'white')
       begin_fill()
       for count in range(4):
            forward(99)
            left(90)
      end_fill()
    
      if number is None:
          return
      elif number < 10:
          forward(20)
    
      write(number, font=('Arial', 60, 'normal'))
    
    def tap(x, y):
        "Swap tile and empty square."
        x = floor(x, 100)
        y = floor(y, 100)
       mark = vector(x, y)
    
      for neighbor in neighbors:
          spot = mark + neighbor
    
          if spot in tiles and tiles[spot] is None:
              number = tiles[mark]
              tiles[spot] = number
              square(spot, number)
             tiles[mark] = None
              square(mark, None)

    def draw():
      "Draw all tiles."
       for mark in tiles:
           square(mark, tiles[mark])
        update()
    
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    load()
    draw()
    onscreenclick(tap)
    done()

#### 코드에 대한 소개 추가

    """Tiles.py를 한국어로 알기 쉽게 설명하는 파일"""            
        
        
    """Tiles, number swapping game                          # Tiles, 숫자바꾸기 게임
    Exercises                                               # 연습문제
    1. Track a score by the number of tile moves.           # 1. 타일 이동 횟수로 점수를 획득합니다.
    2. Permit diagonal squares as neighbors.                # 2. 대각선을 이동을 허용하십시오.
    3. Respond to arrow keys instead of mouse clicks.       # 3. 마우스 클릭 대신 화살표 키를 이용해보세요.
    4. Make the grid bigger.                                # 4. 숫자판과 사용자 인터페이스를 더 크게 만듭니다.
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
    
        tiles[mark] = None                                  # 빈 타일 표시
    
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

 <br>
 <br>
     
That's all.

## Preview

{% capture images %}
	https://cloud.githubusercontent.com/assets/754514/14509716/61ac6c8e-01d6-11e6-879f-8308883de790.png
	https://cloud.githubusercontent.com/assets/754514/14509717/61ad05ae-01d6-11e6-85ae-5a817dd8763b.png
	https://cloud.githubusercontent.com/assets/754514/14509714/61a89708-01d6-11e6-8fcd-74b002a060df.png
{% endcapture %}
{% include gallery images=images caption="Screenshots of Moon Theme" cols=3 %}

---

{% capture images %}
	https://cloud.githubusercontent.com/assets/754514/14509718/61b09a20-01d6-11e6-8da1-4202ae4d83cd.png
	https://cloud.githubusercontent.com/assets/754514/14509715/61aa9d00-01d6-11e6-81a6-c6837edf2e84.png
{% endcapture %}
{% include gallery images=images caption="Moon Theme on Small Screen Size" cols=2 %}      
      
See a [live version of Moon](http://taylantatli.github.io/Moon) hosted on GitHub.      

## Site Setup
A quick checklist of the files you’ll want to edit to get up and running.    

### Site Wide Configuration
`_config.yml` is your friend. Open it up and personalize it. Most variables are self explanatory but here's an explanation of each if needed:

#### title

The title of your site... shocker!

Example `title: My Awesome Site`

#### bio

The description to show on your homepage.

#### description

The description to use for meta tags and navigation menu.

#### url

Used to generate absolute urls in `sitemap.xml`, `feed.xml`, and for generating canonical URLs in `<head>`. When developing locally either comment this out or use something like `http://localhost:4000` so all assets load properly. *Don't include a trailing `/`*.

Examples:

{% highlight yaml %}
url: http://taylantatli.me/Moon
url: http://localhost:4000
url: //cooldude.github.io
url:
{% endhighlight %}

#### reading_time

Set true to show reading time for posts. And set `words_per_minute`, default is 200.

#### logo
Your site's logo. It will show on homepage and navigation menu. Also used for twitter meta tags.

#### background
Image for background. If you don't set it, color will be used as a background.

#### Google Analytics and Webmaster Tools

Google Analytics UA and Webmaster Tool verification tags can be entered in `_config.yml`. For more information on obtaining these meta tags check [Google Webmaster Tools](http://support.google.com/webmasters/bin/answer.py?hl=en&answer=35179) and [Bing Webmaster Tools](https://ssl.bing.com/webmaster/configure/verify/ownership) support.

#### MathJax
It's enabled. But if you don't want to use it. Set it false in  `_config.yml`.

#### Disqus Comments
Set your disqus shortname in `_config.yml` to use comments.

---

### Navigation Links

To set what links appear in the top navigation edit `_data/navigation.yml`. Use the following format to set the URL and title for as many links as you'd like. *External links will open in a new window.*

{% highlight yaml %}
- title: Home
  url: /

- title: Blog
  url: /blog/

- title: Projects
  url: /projects/

- title: About
  url: /about/

- title: Moon
  url: http://taylantatli.me/Moon
{% endhighlight %}

---

## Layouts and Content

Moon Theme use [Jekyll Compress](https://github.com/penibelst/jekyll-compress-html) to compress html output. But it can cause errors if you use "linenos" (line numbers). I suggest don't use line numbers for codes, because it won't look good with this theme, also i didn't give a proper style for them. If you insist to use line numbers, just remove `layout: compress` string from layouts. It will disable compressing.

### Feature Image

You can set feature image per post. Just add `feature: some link` to your post's front matter.

```
feature: /assets/img/some-image.png
or
feaure: http://example.com/some-image.png
```    
 This also will be used for twitter card:

![Moon Twitter Card](https://cloud.githubusercontent.com/assets/754514/14509719/61c5751c-01d6-11e6-8c29-ce8ccad149bf.png)

### Comments
To show disqus comments for your post add `comments: true` to your post's front matter.

---

## Questions?

Found a bug or aren't quite sure how something works? By all means [file a GitHub Issue](https://github.com/TaylanTatli/Moon/issues/new). And if you make something cool with this theme feel free to let me know.

---

## License

This theme is free and open source software, distributed under the MIT License. So feel free to use this Jekyll theme on your site without linking back to me or including a disclaimer.

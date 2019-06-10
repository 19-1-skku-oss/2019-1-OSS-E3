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
      
## 김민수
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

    



## 박정재

## 유재원

## 이재웅

     
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

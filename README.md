# 2019-1-OSS-E3

## Free Python Games


`Free Python Games` is an Apache2 licensed collection of free Python games
intended for education and fun. The games are written in simple Python code and
designed for experimentation and changes. Simplified versions of several
classic arcade games are included.

Python is one of the top-five most popular programming languages in the world
and available for free from `Python.org` Python
includes an extensive Standard Library distributed with your installation. The
Standard Library has a module called Turtle which is a popular way to introduce
programming to kids. Turtle was part of the original Logo programming language
developed by Wally Feurzig and Seymour Papert in 1966. All of the games in
`Free Python Games` are implemented using Python and its Turtle module.

Starting in 2012, `Free Python Games` began as an after school program to
teach programming to inner-city youth. The goal was to have fun as much as it
was to learn. Since then the games have been improved and used in a variety of
settings ranging from classrooms to summer day-camps.

The games run anywhere Python can be installed which includes desktop computers
running Windows, Mac OS, or Linux and older or low-power hardware such as the
Raspberry Pi. Kids across the United States in grades 6th-12th have enjoyed
learning about topics such as encryption and projectile motion through games.

Each game is entirely independent from the others and includes comments along
with a list of exercises to work through with students. Creativity and
flexibility is important. There is no right or wrong way to implement a new
feature or behavior! You never know which games students will engage with best.

- Free Python Games : <http://www.grantjenks.com/docs/freegames/>
- Python.org :  <https://www.python.org/>


## Quickstart


Installing Free Python Games is simple with pip - <https://pypi.python.org/pypi/pip>

  ` $ python3 -m pip install freegames `

Free Python Games supports a command-line interface (CLI). Help for the CLI is
available using:

  ` $ python3 -m freegames --help `

The CLI supports three commands: list, copy, and show. For a list of all games
run:

  ` $ python3 -m freegames list `

Any of the listed games may be played by executing the Python module from the
command-line. To reference the Python module, combine "freegames" with the name
of the game. For example, to play the "snake" game run:

  ` $ python3 -m freegames.snake `

Games can be modified by copying their source code. The copy command will
create a Python file in your local directory which you can edit. For example,
to copy and play the "snake" game run:

 ` $ python3 -m freegames copy snake `<br>
 ` $ python3 snake.py `

Python includes a built-in text editor named IDLE which can also execute Python
code. To launch the editor and make changes to the "snake" game run:

  ` $ python3 -m idlelib.idle snake.py `

You can also access documentation in the interpreter with Python's built-in
help function:

  ` >>> import freegames `<br>
  ` >>> help(freegames) `


## Team Members


- 김민수(소프트웨어/18) : kimminsuu
- 박정재(소프트웨어/18) : tkfhdk123
- 유재원(소프트웨어/18) : itaewonhreedom
- 이재웅(소프트웨어/18) : jaeung0527


## Our Roles

- 박정재 : README.md 수정, snake.py 코드수정, kor-manual.md 번역, 여러가지 코드 피드백
- 유재원 : gh-page 편집, flappy.py 코드수정, 

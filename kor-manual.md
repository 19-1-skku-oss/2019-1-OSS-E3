## Free Python Games


Free Python Games 는 교육과 재미를 위해 만들어진 Apache2 라이센스를 가진 무료 Python 게임들의 모음입니다. 이 게임들은 간단한 Python 코드로 쓰여져 있고 실험과 변화를 위해 고안되었습니다. 몇 가지 클래식 아케이드 게임들의 단순화된 버전들이 포함되어 있습니다. 

파이썬은 세계에서 가장 인기 있는 프로그래밍 언어 5개중 하나이며 Python.org에서 무료로 사용할 수 있습니다. Python은 설치와 함께 배포된 광범위한 표준 라이브러리를 포함합니다. 그 표준 라이브러리는 Turtle이라고 부르는 모듈을 가지고 있는데 이것은 어린 아이들에게 프로그래밍을 소개하기 위한 인기 있는 방법입니다. Turtle은 1966년 Wally Feurzig와 Seymour Papert가 개발한 오리지널 로고 프로그래밍 언어의 일부였습니다. Free Python Games의 모든 게임들은 Python과 그것의 Turtle 모듈을 사용하여 구현됩니다.

Free Python Games 는 배우는만큼 즐거움을 얻는 것을 목표로, 2012년 학생들에게 프로그래밍을 가르치기위한 방과 후 프로그램으로 시작되었습니다. 그 이후로 이러한 게임들은 교실에서 여름 캠프에 이르기까지 다양한 환경에서 개선되고 사용되었습니다.

윈도우, 맥 OS 또는 리눅스를 실행하는 데스크톱 컴퓨터와 라스베리 파이와 같은 구형 또는 저전력 하드웨어를 포함하여 Python은 어디서나 실행할 수 있는 게임입니다. 미국 전역의 6-12학년 아이들은 게임을 통해 암호화와 발사체 움직임과 같은 주제에 대해 배우는 것을 즐겼습니다.

각 게임은 다른 게임들과 완전히 독립적이며 학생들과 함께 연습할 수 있는 목록과 함께 코멘트를 포함합니다. 창의성과 유연성은 중요합니다. 새로운 특징이나 행동을 구현하는 옳고 그른 방법은 없습니다! 당신은 학생들이 어떤 게임과 가장 잘 어울릴지 결코 알지 못합니다.


- Free Python Games : <http://www.grantjenks.com/docs/freegames/>
- Python.org :  <https://www.python.org/>


## 특정


- 플레이하는게 재미있습니다.
- 간단한 Python 코드로 작성되었습니다.
- 설치하기 쉽습니다.
- 교육을 위해 고안되었습니다.
- Python 표준 라이브러리만 사용합니다.
- 교실 강의에서 수백 시간 사용되었습니다.
- 모든것들이 문서화 되어있습니다.
- Python 3.7에서 개발되었습니다.
- CPython 2.7, 3.4, 3.5, 3.6, 그리고 3.7에서 검증되었습니다.
- 윈도우, 맥 OS X, 라스베리 파이, 그리고 리눅스에서 검증되었습니다.
- Travis CI와 AppVeyor CI를 사용하여 검증되었습니다.


[![](https://api.travis-ci.org/grantjenks/free-python-games.svg?branch=master)](http://www.grantjenks.com/docs/freegames/)
[![](https://ci.appveyor.com/api/projects/status/github/grantjenks/free-python-games?branch=master&svg=true)](http://www.grantjenks.com/docs/freegames/)


## 실행방법


pip만 있으면 Free Python Games를 설치하는 방법은 간단합니다 - <https://pypi.python.org/pypi/pip>


  ` $ python3 -m pip install freegames `


Free Python Games는 커맨드 라인 인터페이스(CLI)를 지원합니다. CLI에 대한 도움말은 다음과 같이 사용할 수 있습니다:


  ` $ python3 -m freegames --help`


CLI는 세 가지 명령을 지원합니다: 목록, 복사, 그리고 보여주기. 실행할 수 있는 모든 게임의 목록을 보기 위해서는:


  `$ python3 -m freegames list`


목록에 있는 게임들 중 어떠한 게임도 커맨드 라인에서 Python 모듈을 실행함으로써 즐길 수 있습니다. Python 모듈을 참조하려면, "freegames" 를 게임의 이름과 결합하세요. 예를 들어 "snake" 게임을 실행시키기 위해서는:


  ` $ python3 -m freegames.snake`
  

게임들은 그것들의 소스코드의 복사를 통하여 수정될 수 있습니다. 복사 명령은 당신이 편집할 수 있는 Python 파일을 당신의 로컬 디렉토리에 만듭니다. 예를 들어, "snake" 게임을 복사하고 실행시키기 위해서는:


  `$ python3 -m freegames copy snake`<br>
  `$ python3 snake.py`


Python은 Python 코드를 실행할 수 있는 IDLE이라는 이름의 기본 제공 텍스트 편집기를 포함합니다. 편집기를 시작하여 "snake" 게임을 바꾸고 싶다면:


  `$ python3 -m idlelib.idle snake.py`
  

당신은 또한 Python의 기본 제공 도움말 함수를 통해 인터프리터의 문서에 접근할 수 있습니다:


  `>>> import freegames`<br>
  `>>> help(freegames)`
  

## 가이드


더 자세한 내용을 원하는 사람들을 위해 이 문서에서는 커리큘럼, API 및 개발에 대해 설명하고 있습니다


- Talk: Give the Gift of Python : <http://www.grantjenks.com/docs/freegames/give-gift-python.html>
- Free Python Games Curriculum : <http://www.grantjenks.com/docs/freegames/curriculum.html>
- Free Python Games API Reference : <http://www.grantjenks.com/docs/freegames/api.html>
- Free Python Games Development : <http://www.grantjenks.com/docs/freegames/development.html>


## 참조

- Free Python Games Documentation : <http://www.grantjenks.com/docs/freegames/>
- Free Python Games at PyPI : <https://pypi.python.org/pypi/freegames>
- Free Python Games at GitHub : <https://github.com/grantjenks/free-python-games>
- Free Python Games Issue Tracker : <https://github.com/grantjenks/free-python-games/issues>


## Free Python Games License


**Copyright 2017-2019 Grant Jenks**

Apache 라이센스, 버전 2.0 (이하 "라이센스")에 의거하여 라이센스가 부여됩니다. 귀하는 라이센스를 준수하는 경우를 제외하고는이 파일을 사용할 수 없습니다. 라이센스의 사본은 다음 주소에서 얻을 수 있습니다.

  <http://www.apache.org/licenses/LICENSE-2.0>

관련 법률에 의해 요구되거나 서면으로 동의하지 않는 한, 라이센스에 따라 배포 된 소프트웨어는 명시적 또는 묵시적으로 어떠한 종류의 보증이나 조건없이 "있는 그대로"의 상태로 배포됩니다. 라이센스에 따라 사용 권한 및 제한 사항을 규정 한 특정 언어에 대한 라이센스를 참조하십시오.

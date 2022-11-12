import turtle                      #turtle 함수를 불러온다 
import random                      #random 함수를 불러온다
t = turtle.Turtle()                # 변수 t를 turtle함수와 같다고 정함
t.shape("turtle")                  #t를 거북이 모양으로 정함
for j in range (1,10):             #9번 반복 
    t.up()                             #펜을 들어올린다
    x = random.randint(-200, 200)      # x를 -200에서 200까지로 랜덤하게 정한다
    y = random.randint(-200, 200)      # y를 -200에서 200까지로 랜덤하게 정한다
    r = random.randint(10, 200)        # r의 좌표를 10에서 200까지 랜덤하게 정한다
    t.goto(x, y)                       # t를 x,y좌표로 이동시킨다
    t.down()                           # 펜을 내린다
    t.circle(r)                        # 원의 반지름을 r로 한다

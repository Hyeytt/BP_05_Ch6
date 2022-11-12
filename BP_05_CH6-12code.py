import turtle                            # turtle 함수를 불러온다 
import math                              # math 함수를 불러온다

t= turtle.Turtle()                       # 변수 t를 turtle함수와 같다고 정함  
t.shape("turtle")                        # 모양을 거북이 모양으로 정함 
t.color('red', 'yellow')                 # 색깔을 빨간색과 노란색으로 정함

for x in range(0, 360):                  # 0에서 360까지 반복
     t.goto(x,200*math.sin(x*3.14/180))  # t를 (x , 계산된 사인값)으로 이동시킨다

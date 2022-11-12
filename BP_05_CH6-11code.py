import turtle                    # turtle 함수를 불러온다 
t = turtle.Turtle()              # 변수 t를 turtle함수와 같다고 정함  
t.shape("turtle")                # t를 거북이 모양으로 정함
t.color('red', 'yellow')         # 색깔을 빨강과 파랑으로 정함
t.begin_fill()                   # 도형의 색을 채운다.
while True:                      # 계속해서 무한히 반복한다
    t.forward(200)                   # 앞으로 200만큼 이동시킨다
    t.left(170)                      # 왼쪽으로 170도 회전시킨다
    if abs(t.pos()) < 1:             # 거북이 좌표의 절댓값이 1보다 작으면(0)이 되었을 경우
         break                       # 반복을 멈춘다
t.end_fill()                     #도형색 채우기을 멈춘다

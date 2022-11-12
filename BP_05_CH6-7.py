import turtle                          #turtle 함수를 불러온다
t = turtle.Turtle()                    # 변수 t를 turtle함수와 같다고 정함
t.shape("turtle")                      # t를 거북이 모양으로 정함
t.left(90)                             # t를 왼쪽으로 90도 회전시킨다
for i in range (1,7):                  # 1에서 6까지 반복                
    t.forward(100)                     # 앞으로 100만큼 이동
    t.forward(-30)                     # -30만큼 이동
    t.left(60)                         # 왼쪽으로 60도 회전
    t.forward(30)                      # 앞으로 30만큼 이동
    t.forward(-30)                     #앞으로 -30만큼 이동
    t.right(120)                       #오른쪽으로 120도 회전 
    t.forward(30)                      #앞으로 30만큼 이동
    t.forward(-30)                     #앞으로 -30만큼 이동
    t.left(60)                         #왼쪽으로 60도 만큼 회전
    t.forward(-70)                     #앞으로 -70만큼 이동
    t.left(60)                         #왼쪽으로 60도 만큼 회전

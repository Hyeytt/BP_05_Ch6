import turtle               #turtle 함수를 불러온다 
t = turtle.Turtle()         # 변수 t를 turtle함수와 같다고 정함
t.shape("turtle")           # 변수 t를 turtle함수와 같다고 정함
for i in range(5):          # 5번 반복한다
    t.forward(200);         # 앞으로 200만큼 이동시킨다  
    t.right(90)             # 오른쪽으로 90도 회전시킨다
    t.forward(20);          # 앞으로 20만큼 이동시킨다
    t.right(90)             # 오른쪽으로 90도 회전시킨다
    t.forward(200);         # 앞으로 200만큼 이동시킨다
    t.left(90)              # 왼쪽 90도 회전시킨다
    t.forward(20);          # 20만큼 앞으로 이동시킨다
    t.left(90)              # 왼쪽으로 90도 회전시킨다     

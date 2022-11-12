import turtle                   #turtle 함수를 불러온다 
myPen = turtle.Turtle()         #변수 mypen을 turtle함수와 같다고 정함
myPen.speed(0)                  #speed(0)을 사용해 프로그램 실행속도를 높임
myPen.color("#FF0000")          #펜의 색을 #FF0000
for j in range (1,10):          #아래에 들어쓰여진 문장들을 반복한다
  for i in range (1,6):          #아래에 들어쓰여진 문장들을 반복한다
    myPen.left(144)               #왼쪽으로 144만큼 이동시킨다
    myPen.forward(200)            #앞으로 200만큼 이동시킨다
  myPen.left(10)                 #왼쪽으로 100만큼 회전시킨다

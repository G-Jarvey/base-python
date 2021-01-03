from turtle import *
reset()
pensize(5)
#画正六边形 ，每步右转60度
for i in range(6):
    right(60)
    fd(100)
#用circle方法画正六边形（半径为 60 像素的圆内正接六边形 ）
color('red')
circle(60,steps=6)
#抬笔移动位置
up()
goto(-50,200)
down()

# 画五角星，每步右转144度
for i in range(5):
    right(144)
    fd(100)
done()

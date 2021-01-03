from tkinter import  *
root=Tk()
root.title('绘制图形')
root.geometry('320x240')
def draw(event):
    # 画矩形
    mycnavas.create_rectangle(90,10,200,200)
    # 画椭圆，填充颜色
    mycnavas.create_oval(90,10,200,200,fill='green')
    # 画扇形
    mycnavas.create_arc(90,10,200,200,fill='pink')
    # 画多边形（三角形），前景为蓝色，无填充色
    mycnavas.create_polygon(10,180,145,10,290,180,outline='blue',fill='')
    # 画直线
    mycnavas.create_line(0,105,300,105,fill='red')
    # 写文字，颜色为十六进制RGB字符串
    mycnavas.create_text(50,10,text='我的画布',fill='#123456')

def delt():
    mycnavas.delete(ALL)

mycnavas = Canvas(root,width=300,height=200)
mycnavas.pack()
mycnavas.bind('<Button-1>',draw)  # 画布绑定鼠标点击事件
btnclear=Button(root,text='清空',command=delt)
btnclear.pack()
root.mainloop()

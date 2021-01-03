from tkinter import *
root=Tk()
root.title('呈现位图图像')
root.geometry('320x240')
mycanvas=Canvas(root)
mycanvas.pack()
photo=PhotoImage(file='e:\\XiaoBai\\呵呵.png') # 图片的格式不要错，否则会报错的
mycanvas.create_image(100,100,image=photo)
root.mainloop()

import tkinter
from tkinter import ttk

def auto():
    pass
def drawoval(x,y):
        canvas.create_oval(x+2, y+2, x+48, y+48, fill="black", width=0)
        canvas.create_text(x+25, y+25,fill="yellow",text="Q",font=("",30))
def drawngarea(x,y):
        canvas.create_rectangle(x+1,y+1,x+50,y+50,fill="green",width=0)
        ngarea.append([x,y])
def click(e):
 if e.x<400 and e.y<400:
        permit=True
        x=e.x//50*50
        y=e.y//50*50
        for i in range(len(ngarea)):
                if ngarea[i][0]==x and ngarea[i][1]==y:
                        permit=False
        if permit==True:
                for i in range(8):
                        n=i*50
                        drawngarea(x,n)
                        drawngarea(n,y)
                        drawngarea(x+n,y+n)
                        drawngarea(x-n,y-n)
                        drawngarea(x+n,y-n)
                        drawngarea(x-n,y+n)
                drawoval(x,y)
                global oval
                oval+=1
                if oval==8:
                        print("やったーーーーー")
                        canvas.create_text(200,200,fill="yellow",text="★CLEAR★",font=("",50))
root = tkinter.Tk()
root.title('8queen')
frame1 = ttk.Frame(root)
frame1['width'] = 400
frame1['height'] = 430
frame1.grid()
#キャンバスエリア
canvas = tkinter.Canvas(root, width = 400, height = 400, bg="white")
def begin():
        global ngarea,oval
        oval=0
        ngarea=[[1000000,10000000]]
        for i in range(1,8):
                canvas.create_line(i*50,0,i*50,400)
                canvas.create_line(0,i*50,400,i*50)
#イベントを設定する
canvas.bind("<Button-1>", click)
#キャンバスバインド
canvas.place(x=0, y=0)
begin()
def reset(e):
        canvas.create_rectangle(0, 0, 400, 400, fill = 'white')
        begin()
button=tkinter.Button(root,text="やり直す",width=15)
button.bind("<Button-1>",reset)
button.place(x=0, y=401)
root.mainloop()
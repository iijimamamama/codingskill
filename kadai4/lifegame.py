import random
import tkinter
from tkinter import ttk
cellnum=220
cellsize=3
gamelist=[]
editmode=True
root = tkinter.Tk()
root.title('lifegame')
frame1 = ttk.Frame(root)
frame1['width'] = cellnum*cellsize
frame1['height'] = cellnum*cellsize+60
frame1.grid()
#キャンバスエリア
canvas = tkinter.Canvas(root, width = cellnum*cellsize, height = cellnum*cellsize, bg="white")
def screenupdate():
    pass
def click(e):
 if e.x<cellnum*cellsize and e.y<cellnum*cellsize and editmode==True:
     changelife(e.x//cellsize,e.y//cellsize)
def modechange(e):
    global editmode
    editmode=not(editmode)
    #print(editmode)
    game()
def changelife(x:int,y:int):
    if gamelist[y+1][x+1]==1:
        gamelist[y+1][x+1]=0
        paintsquare(x,y,"white")
    elif gamelist[y+1][x+1]==0:
        gamelist[y+1][x+1]=1
        paintsquare(x,y,"blue")
def paintsquare(x:int,y:int,color:str):
    canvas.create_rectangle(x*cellsize+1,y*cellsize+1,x*cellsize+cellsize,y*cellsize+cellsize,fill=color,width=0,tag="life")
for i in range(1,cellnum):
    canvas.create_line(i*cellsize,0,i*cellsize,cellnum*cellsize)
    canvas.create_line(0,i*cellsize,cellnum*cellsize,i*cellsize)
#キャンバスバインド
canvas.place(x=0, y=30)
#イベントを設定する
canvas.bind("<Button-1>", click)
button=tkinter.Button(root,text="切り替え",width=15)
button.bind("<Button-1>",modechange)
button.place(x=0, y=cellnum*cellsize+31)
labelstr=tkinter.StringVar()
labelstr.set("編集モード")
label1=tkinter.Label(root,textvariable=labelstr,font=("メイリオ",13))
label1.place(x=0,y=0)
for i in range(cellnum+2):
    gamelist.append([])
    for j in range(cellnum+2):
        gamelist[i].append(0)
changelist=[]
for i in range(cellnum):
    changelist.append([])
    for j in range(cellnum):
        changelist[i].append(random.randint(0,1))
        #changelist[i].append(0)
def change():
    for i in range(cellnum):
        for j in range(cellnum):
            gamelist[i+1][j+1]=changelist[i][j]
            if changelist[i][j]==1:
                paintsquare(j,i,"blue")
            elif changelist[i][j]==0:
                paintsquare(j,i,"white")
def judge():
    for i in range(1,cellnum+1):
        for j in range(1,cellnum+1):
            seibutu=gamelist[i-1][j-1]+gamelist[i-1][j]+gamelist[i-1][j+1]+gamelist[i][j-1]+gamelist[i][j+1]+gamelist[i+1][j-1]+gamelist[i+1][j]+gamelist[i+1][j+1]
            if gamelist[i][j]==0:
                if seibutu==3:
                    changelist[i-1][j-1]=1
            elif gamelist[i][j]==1:
                if seibutu<=1 or seibutu>=4:
                    changelist[i-1][j-1]=0
                else:
                    changelist[i-1][j-1]=1
                pass
            else:
                print("ありえない数字が含まれています")
change()
judge()
change()
def game():
    if editmode==False:
        labelstr.set("成長モード")
        judge()
        canvas.delete("life")
        change()
        root.after(50,game)
    else:
        labelstr.set("編集モード")

"""for i in range(len(gamelist)):
    print(gamelist[i])
print("---------------------------------")"""
#for i in range(len(changelist)):
#    print(changelist[i])
root.mainloop()
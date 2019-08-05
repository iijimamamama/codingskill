import random
import sys
import tkinter
from tkinter import ttk
sys.setrecursionlimit(10000)
tate=20
yoko=20
meiro=[]
wasd=[2,3,5,7]
wasd_houkou=["↑","←","↓","→"]
wasd_zahyhou=[[-1,0],[0,-1],[1,0],[0,1]]
root=[]
for i in range(tate):#meiro[tate][yoko]
    meiro.append([1])
    for j in range(yoko-1):
        meiro[i].append(1)
def anahori(y,x,houkou=4,retry=0):
    if houkou==4:
        houkou=random.randint(0,3)
    next_y=y+wasd_zahyhou[houkou][0]
    next_x=x+wasd_zahyhou[houkou][1]
    if tate>next_y>=0 and yoko>next_x>=0:
        next=meiro[next_y][next_x]
        if next==1:
            #print(wasd_houkou[houkou],y,x,next_y,next_x)
            meiro[y][x]=meiro[y][x]*wasd[houkou]
            meiro[next_y][next_x]=next*wasd[(houkou+2)%4]
            root.append([y,x])
            anahori(next_y,next_x)
        else:
            if retry<3:
                anahori(y,x,(houkou+1)%4,retry+1)
            elif len(root)>0:
                oldroot=root.pop(-1)
                anahori(oldroot[0],oldroot[1])
    else:
        if retry<3:
                anahori(y,x,(houkou+1)%4,retry+1)
        elif len(root)>0:
                oldroot=root.pop(-1)
                anahori(oldroot[0],oldroot[1])

anahori(0,0)
def meiroprint():
    for i in range(tate):
        print(meiro[i])
#meiroprint()
root = tkinter.Tk()
root.title('迷路生成')
frame1 = ttk.Frame(root)
frame1['width'] = 400
frame1['height'] = 400
frame1.grid()
#キャンバスエリア
canvas = tkinter.Canvas(root, width = 400, height = 400,bg="#FFFFFF")
canvas.place(x=0, y=0)
for i in range(tate):
    for j in range(yoko):
        if meiro[i][j]%2!=0:
            canvas.create_line(j*20,i*20,(j+1)*20,i*20)
            pass
        if meiro[i][j]%3!=0:
            canvas.create_line(j*20,i*20,j*20,(i+1)*20)
            pass
        if meiro[i][j]%5!=0:
            canvas.create_line(j*20,(i+1)*20,(j+1)*20,(i+1)*20)
            pass
        if meiro[i][j]%7!=0:
            canvas.create_line((j+1)*20,i*20,(j+1)*20,(i+1)*20)
            pass
root.mainloop()
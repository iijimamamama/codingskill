#coding: UTF-8
import sys
import os
f=open('input.txt','r') #input.txtを読み込み用に開く　この2行は提出する時に消しておく
sys.stdin=f #標準入力にinput.txtを代入
own=list(map(int,input().split()))
enemy_number=int(input())
enemy=[]
for i in range(enemy_number):
    enemy.append(list(map(int,input().split())))
for i in range(enemy_number):
    if own[0]<=enemy[i][0]+enemy[i][2]<=own[0]+own[2]+enemy[i][2]:
        if own[1]<=enemy[i][1]+enemy[i][3]<=own[1]+own[3]+enemy[i][3]:
            print('敵機',i+1,'が当たり')

#coding: UTF-8
import random
def trumprandom(n:int)->list:
    suit=[]
    number=[]
    i=0
    while i<n:
        suit.append(int(random.random()*4))
        number.append(int(random.random()*13))
        if i>0:
            for j in range(i):
                if suit[i]==suit[j] and number[i]==number[j]:
                    suit.pop(-1)
                    number.pop(-1)
                    i-=1
        i+=1

    return suit,number
def syuturyokuyou(suit:list,number:list)->str:
    ans=""
    suit_to_alp=["S","C","D","H"]
    number_to_trump=["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for i in range(5):
        ans+=suit_to_alp[suit[i]]+number_to_trump[number[i]]+","
    return ans[:-1]
def straight(number:list)->bool:
    #[13,1,2,3,4]のようなストレートを判定するための処理
    number2=[]
    for i in range(5):
        if number[i]<5:
            number2.append(number[i]+13)
        else:
            number2.append(number[i])
    number_j=sorted(number)
    number_j2=sorted(number2)
    kaidan=0
    kaidan2=0
    ans=False
    for i in range(1,5):
        if number_j[i-1]+1==number_j[i]:
            kaidan+=1
        if number_j2[i-1]+1==number_j2[i]:
            kaidan2+=1
    if kaidan==4 or kaidan2==4:
        ans=True
    return ans
def pw (n,power):#->int
    #print(n,power)
    if n>power:
        return n
    else:
        return power
    #後々powerはこんな感じで低い値を代入されないようにする
def yakuhantei(suit:list,number:list):#->str,int
    ans=""
    power=0
    suit_j=sorted(suit)
    number_j=sorted(number)
    if suit_j[0]==suit_j[4]:#ロイヤルストレートフラッシュ、ストレートフラッシュ、フラッシュの判定
        if number_j==[1,10,11,12,13]:
            ans="ロイヤルストレートフラッシュ"
            power=pw(9,power)
        elif straight(number)==True:
            ans="ストレートフラッシュ"
            power=pw(8,power)
        else:
            ans="フラッシュ"
            power=pw(5,power)
    elif number_j[0]==number_j[3] or number_j[1]==number_j[4]:
        #ソートをしているので、フォーカードは[A,A,A,A,B]か[A,B,B,B,B]
        ans="フォーカード"
        power=pw(7)
    elif number_j[0]==number_j[2] or number_j[1]==number_j[3] or number_j[2]==number_j[4]:#スリーカードの判定
        #同様に、フルハウスは[A,A,A,B,B]か[A,A,B,B,B]
        if number_j[0]==number_j[1] and number_j[3]==number_j[4] and number_j[1]!=number_j[3]:
            ans="フルハウス"
            power=pw(6,power)
        else:
            ans="スリーカード"
            power=pw(3,power)
    elif straight(number)==True:
        ans="ストレート"
        power=4
    else:
        pair=0
        for i in range(4):
            if number_j[i]==number_j[i+1]:
                pair+=1
        if pair==2:
            ans="ツーペア"
            power=pw(2,power)
        elif pair==1:
            ans="ワンペア"
            power=pw(1,power)
        elif pair==0:
            ans="ノーペア"
            power=pw(0,power)
    return ans,power
    #テスト用出力処理
    '''
    for i in range(5):
        ans+=str(suit_j[i])+","+str(number_j[i])+","
    return ans[:-1]'''
suit,number=trumprandom(10)
suit2=[]
number2=[]
for i in range(5):
    suit2.append(suit.pop())
    number2.append(number.pop())
'''
suit=[]
number=[]
for i in range(5):
    x,y = map(int,input().split())
    suit.append(x)
    number.append(y)'''
ans1=syuturyokuyou(suit,number)
print("1P: "+ans1)
ans2,power1=yakuhantei(suit,number)
print(ans2)
ans3=syuturyokuyou(suit2,number2)
print("2P: "+ans3)
ans4,power2=yakuhantei(suit2,number2)
print(ans4)
#print(power1,power2)
if power1>power2:
    print("1Pの勝ち！")
elif power1<power2:
    print("2Pの勝ち！")
else:
    print("引き分け！")
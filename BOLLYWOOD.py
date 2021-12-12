from clear_screen import clear
m=input("Enter Name Of A Movie :\n")
m=m.upper()
vow=['A','E','I','O','U']
spo=[]
c=k=0
wro=[]
i=9
bol='BOLLYWOOD'
while i>0 and k==0 :
    k=1
    clear()
    for j in range(0,i):
        print(bol[j],end="")
    print("\n")
    c=0
    for e in m:
        if e in vow or e in spo:
            print(e," " ,end="")
        elif e==' ':
            print("/ ",end='')
        else:
            print("_ ",end="")
            k=0
    print("\n")
    if k==1:
    	break
    print("Spoken=",spo,"\nWrong=",wro)
    ch=input("Enter A Letter :\n")
    ch=ch.upper()
    if ch in m:
        if ch not in spo:
            spo.append(ch)
    if ch not in m and ch not in wro and ch not in vow:
        wro.append(ch)
        i-=1
if i!=0:
    c=1
if c==1:
    print("You Win")
else:
    print("You Lose\nThe Name Was :\n",m)

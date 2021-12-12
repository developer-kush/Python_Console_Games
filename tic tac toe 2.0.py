from tkinter import *
from time import sleep
root= Tk()
root.title('Tic Tac Toe')

turn=StringVar()
winner=0
i=1
j=1
v0=StringVar()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
v9 = StringVar()
l1=[v0,v1,v2,v3,v4,v5,v6,v7,v8,v9]
w_zone=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
p1=[]
p2=[]

turn.set('Player1\'s Turn')

#frameset
f=Frame(root)
f2=Frame(root)
f3=Frame(root)
chf=Frame(root)

''' comp code

Label(chf,font=('courier',10),width=20,height=2,text='!!! TIC TAC TOE !!!',bg='black',fg='white').grid(row=0,column=1,columnspan=2)
Button(chf,text='Vs Computer',command=lambda:func1()).grid(row=1,column=1)
Button(chf,text='PvP',command=lambda:func2()).grid(row=1,column=2)

chf.pack()
'''

#f1 setting
Label(f,font=('courier',10),width=20,height=2,text='!!! TIC TAC TOE !!!',bg='black',fg='white').grid(row=0,column=1,columnspan=3)
		
Label(f,width=20,height=2,textvariable=turn).grid(row=1,column=1,columnspan=3)
		
Button(f,bg='brown',fg='yellow',font=('courier',10), textvariable=v1,width=4,height=2, command=lambda: click(1)).grid(row=2,column=1)
		
Button(f, bg='yellow',fg='brown',font=('courier',10), textvariable=v2,width=4,height=2, command=lambda: click(2)).grid(row=2,column=2)
		
Button(f,bg='brown',fg='yellow', font=('courier',10), textvariable=v3,width=4,height=2, command=lambda: click(3)).grid(row=2,column=3)
		
Button(f, bg='yellow',fg='brown',font=('courier',10), textvariable=v4,width=4,height=2, command=lambda: click(4)).grid(row=3,column=1)
		
Button(f, bg='brown',fg='yellow',font=('courier',10), textvariable=v5,width=4,height=2, command=lambda: click(5)).grid(row=3,column=2)
		
Button(f,bg='yellow',fg='brown', font=('courier',10), textvariable=v6,width=4,height=2, command=lambda: click(6)).grid(row=3,column=3)
		
Button(f, bg='brown',fg='yellow',font=('courier',10), textvariable=v7,width=4,height=2, command=lambda: click(7)).grid(row=4,column=1)
		
Button(f, bg='yellow',fg='brown',font=('courier',10), textvariable=v8,width=4,height=2, command=lambda: click(8)).grid(row=4,column=2)
		
Button(f,bg='brown',fg='yellow', font=('courier',10), textvariable=v9,width=4,height=2, command=lambda : click(9)).grid(row=4,column=3)
	
Label(f,text='\n').grid(row=5,column=2)
	
Button(f, font=('courier',10), text='QUIT',width=4,height=2, command=lambda:quit()).grid(row=6,column=2)

f.pack()

# event
def click(event):
	global i
	global winner
	winner=0
	if event in p1 or event in p2:
		event=0
		i=i-1
	if i%2==1:
			l1[event].set('X')
			p1.append(event)
			turn.set('Player2\'s Turn')
	elif i%2==0:
			l1[event].set('O')
			p2.append(event)
			turn.set('Player1\'s Turn')
	if i==9:
		turn.set('')
		winner=4
	i+=1
	#winner declaration
	count1=count2=count3=0
	for lno in range (0,8):
		if not count1 >= 3:
			count1=0
		for ele in p1:
			if ele in w_zone[lno]:
				count1+=1
		if not count2>= 3:
			count2=0
		for ele in p2:
			if ele in w_zone[lno]:
				count2+=1
	if count1 >= 3:
		winner=1
	if count2 >= 3:
		winner=2
		
	if winner in [1,2,4]:
		f.pack_forget()
		f2.pack_forget()
		f3.pack()
	if winner==1:
		wlabel=Label(f3,height=2,width=12,font=('calibri',15),text='Player 1 wins').grid(row=0,column=0,columnspan=2)
	if winner==2:
		wlabel=Label(f3,height=2,width=12,font=('calibri',15),text='Player 2 wins').grid(row=0,column=0,columnspan=2)
	if winner ==4:
		wlabel=Label(f3,height=2,width=12,font=('calibri',15),text='Draw').grid(row=0,column=0,columnspan=2)
	
#f3 setting
Label(f3,font=('courier',10),height=2,width=12,text='Wanna replay ??').grid(row=1,column=0,columnspan=2)
Button(f3,height=2,width=6,text='Yes',command=lambda:replay()).grid(row=2,column=0)
Button(f3,height=2,width=6,text='No',command=quit).grid(row=2,column=1)


#f2 setting
Label(f2,font=('courier',15),height=2,width=12,text='!!QUITTING!!\nAre You Sure').grid(row=0,column=0,columnspan=2)
Button(f2,height=2,width=6,text='Yes',command=quit).grid(row=1,column=0)
Button(f2,height=2,width=6,text='No',command=lambda:No()).grid(row=1,column=1)

#replay
def replay():
	for n_ele in l1:
		n_ele.set('')
	turn.set('Player1\'s Turn')
	i=1
	count1=count2=0
	winner=0
	j=1
	p1=[]
	p2=[]
	f3.pack_forget()
	f.pack()

#f2 functions
def quit():
	f.pack_forget()
	f2.pack()
	
def No():
	f2.pack_forget()
	f.pack()
	
root.mainloop()
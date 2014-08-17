#from tkinter import Frame, Canvas, Label, Button, LEFT, RIGHT, ALL, Tk 
from Tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
from random import randint

class main:

	def __init__ (self, master):
		self.frame = Frame(master) #main frame
		self.frame.pack(fill = 'both', expand = True)
		self.canvas = Canvas(self.frame, width = 300, height = 300)
		self.canvas.pack(fill = 'both', expand = True) #probi zamenjat da vides ucinek
		self.label = Label(self.frame, text	= 'Tic Tac Toe', height = 6, bg = 'black', fg = 'blue')
		self.label.pack(fill='both', expand = True)
		self.framepod = Frame(self.frame)#sub frame
		self.framepod.pack(fill = 'both', expand = True)
		self.Single = Button(self.framepod, text = 'Start single player', height = 4, command = self.startsingle, bg = 'white', fg = 'blue')
		self.Single.pack(fill='both', expand = True, side=RIGHT)
		self.Multi = Button(self.framepod, text = 'Start double player', height = 4, command = self.clean, bg = 'white', fg = 'blue')
		self.Multi.pack(fill='both', expand = True, side=RIGHT)
		self.draw()

	#def startmulti(self):
		#self.clean()
		#self.draw()

	def startsingle(self):
		pass

	def clean(self): #cleans the all simbols from canvas
		self.canvas.delete(ALL)
		self.label['text'] = ('Tic Tac Toe Game')
		self.canvas.bind("<ButtonPress-1>", self.place)
		self.draw() #---------------------------------------
		self.table=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
		self.c=0 #counter
		self.e=False #flag for end game

	def draw(self): #draws the outline lines
		self.canvas.create_rectangle(0,0,300,300, outline='black')
		self.canvas.create_rectangle(100,300,200,0, outline='black')
		self.canvas.create_rectangle(0,100,300,200, outline='black')

	def place(self, event):
		for i in range(0,300,100):
			for j in range(0,300,100):
				if event.x in range(i,i+100) and event.y in range(j, j+100):
					if self.canvas.find_enclosed(i,j,i+100, j+100) == ():
						if self.c % 2 == 0:
							#calculate points to draw circle
							x=(2*i+100)/2
							y=(2*j+100)/2
							x2=int(i/100)
							y2=int(j/100)
							self.canvas.create_oval(x+25,y+25,x-25,y-25, width = 4, outline="black")
							self.table[y2][x2] = 4
							self.c+=1
						else:
							#calculate points to draw cross
							x=(2*i+100)/2
							y=(2*j+100)/2
							x2=int(i/100)
							y2=int(j/100)
							self.canvas.create_line(x+20,y+20,x-20,y-20, width = 4, fill="black")
							self.canvas.create_line(x-20,y+20,x+20,y-20, width = 4, fill="black")
							self.table[y2][x2] = 1
							self.c+=1
		self.check() 


	def check(self):
		#checks for win
		#horitontal
		for i in range(3):
			if sum(self.table[i])==3:
				self.label['text'] = ('X wins')
				self.end()
			if sum(self.table[i])==12:
				self.label['text'] = ('O wins')
				self.end()
		#vertical
		self.vs=[[row[i] for row in self.table] for i in range(3)]
		for i in range(3):
			if sum(self.vs[i])==3:
				self.label['text'] = ('X wins')
				self.end()
			if sum(self.vs[i])==12:
				self.label['text'] = ('O wins')
				self.end()
		#diagonals
		self.dig1=0
		self.dig2=0
		for i in range(3):
			self.dig1+=self.table[i][i]
		for i in range(3):
			self.dig2+=self.table[2-i][i]

		if self.dig1==3:
			self.label['text'] = ('X wins')
			self.end()
		if self.dig1==12:
			self.label['text'] = ('O wins')
			self.end()
		if self.dig2==3:
			self.label['text'] = ('X wins')
			self.end()
		if self.dig2==12:
			self.label['text'] = ('O wins')
			self.end()

		#draw
		if self.e==False:
			a=0
			for i in range(3):
				a+=sum(self.table[i])
			if a == 24: #5 *4 + 4 * 1 --> 5 circles and 4 crosses
				self.label['text'] = ('Draw')
				self.end()

	def end(self):
		self.canvas.unbind("<ButtonPress-1>")
		self.e=True
		

root = Tk()
app = main(root)
root.mainloop()
from Tkinter import Frame, Canvas, Label, Button, LEFT,RIGHT, ALL, Tk
import random
from PIL import Image, ImageTk


#tko delas z fotografijami
#image = Image.open("lenna.jpg")
#photo = ImageTk.PhotoImage(image)

class main:

	def __init__ (self):
		self.app = Tk()
		self.app.title('Tic Tac Toe')
		#self.app.resizable(width=False, height=False)
		#width and hight of window
		w = 900
		h = 1100
		#width and hight of screen
		ws = self.app.winfo_screenwidth()
		hs = self.app.winfo_screenheight()
		#calculate position
		x = ws/2 - w/2
		y = hs/2 - h/2
		#place window -> pramaters(visina, dolzina, pozicija x, pozicija y)
		self.app.geometry("%dx%d+%d+%d" % (w,h, x, y))

		#======================================
		self.frame = Frame() #main frame
		self.frame.pack(fill = 'both', expand = True)
		self.label = Label(self.frame, text	= 'Tic Tac Toe', height = 4, bg = 'white', fg = 'blue')
		self.label.pack(fill='both', expand = True)
		#self.label2 = Label(self.frame, text	= 'here', height = 2, bg = 'white', fg = 'blue') odkomentiri samo za develop-------------
		#self.label2.pack(fill='both', expand = True)
		self.canvas = Canvas(self.frame, width = 900, height = 900)
		self.canvas.pack(fill = 'both', expand = True)
		self.framepod = Frame(self.frame)#sub frame
		self.framepod.pack(fill = 'both', expand = True)
		self.Single = Button(self.framepod, text = 'Start single player', height = 4, command = self.startsingle, bg = 'white', fg = 'blue')
		self.Single.pack(fill='both', expand = True, side=RIGHT)
		self.Multi = Button(self.framepod, text = 'Start double player', height = 4, command = self.double, bg = 'white', fg = 'blue')
		self.Multi.pack(fill='both', expand = True, side=RIGHT)
		self.board = AI()
		self.draw()

	def double(self): 
		#cleans the all simbols from canvas
		self.canvas.delete(ALL)
		self.label['text'] = ('Tic Tac Toe Game')
		self.canvas.bind("<ButtonPress-1>", self.place)
		self.draw() #---------------------------------------
		self.table=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
		self.c=0 #counter
		self.e=False #flag for end game

	def draw(self): #draws the outline lines
		self.canvas.create_rectangle(0,0,900,900, outline='black')
		self.canvas.create_rectangle(300,900,600,0, outline='black')
		self.canvas.create_rectangle(0,300,900,600, outline='black')

	def place(self, event):
		for i in range(0,900,300):
			for j in range(0,900,300):
				if event.x in range(i,i+300) and event.y in range(j, j+300):
					if self.canvas.find_enclosed(i,j,i+300, j+300) == ():
						if self.c % 2 == 0:
							#calculate points to draw circle
							x=(2*i+300)/2
							y=(2*j+300)/2
							x2=int(i/300)
							y2=int(j/300)
							self.canvas.create_oval(x+75,y+75,x-75,y-75, width = 4, outline="blue")
							self.table[y2][x2] = 4
							self.c+=1
						else:
							#calculate points to draw cross
							x=(2*i+300)/2
							y=(2*j+300)/2
							x2=int(i/300)
							y2=int(j/300)
							self.canvas.create_line(x+60,y+60,x-60,y-60, width = 4, fill="red")
							self.canvas.create_line(x-60,y+60,x+60,y-60, width = 4, fill="red")
							self.table[y2][x2] = 1
							self.c+=1
		self.check() 


	def startsingle(self):
		self.canvas.delete(ALL)
		self.label['text'] = ('Tic Tac Toe Game')
		self.canvas.bind("<ButtonPress-1>", self.placeone)
		self.draw()
		self.board = AI()

	def placeone(self, event):
		player = 'X'
		for i in range(0,900,300):
			for j in range(0,900,300):
				if event.x in range(i,i+300) and event.y in range(j, j+300):
					if self.canvas.find_enclosed(i,j,i+300, j+300) == ():
						x=(2*i+300)/2
						y=(2*j+300)/2
						x2=int(i/300)
						y2=int(j/300)
						self.canvas.create_line(x+60,y+60,x-60,y-60, width = 4, fill="red")
						self.canvas.create_line(x-60,y+60,x+60,y-60, width = 4, fill="red")

						
						player_move = x2 + 3*y2 #spremeni
						self.board.make_move(player_move, player)
						
		if self.board.complete():
			self.label['text'] = (self.board.winner())
			self.canvas.unbind("ButtonPress-1")
			self.board = AI()
		elif self.board.winner() != None:
			self.label['text'] = (self.board.winner())
			self.canvas.unbind("ButtonPress-1")
			self.board = AI()
		else:
			player = self.board.get_enemy(player)
			computer_move = self.board.determine(self.board, player)
			self.board.make_move(computer_move, player)

			ti = computer_move % 3
			tj = computer_move / 3

			x=(600*ti+300)/2
			y=(600*tj+300)/2
			#self.label2['text'] = str(computer_move) + '  ti ' + str(ti) + ' tj ' + str(tj) + ' y ' + str(y) + ' x ' +str(x)
			self.canvas.create_oval(x+75,y+75,x-75,y-75, width = 4, outline="blue")
			
			if self.board.winner() != None:
				self.label['text'] = (self.board.winner())
				self.canvas.unbind("ButtonPress-1")
				self.board = AI()

 

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

	def mainloop(self):
		self.app.mainloop()
#===========================================================================
#AI --> MiniMax algorithm and alphabeta puring
class AI(object):
    winning_combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6])

    #winners = ('X-win', 'Draw', 'O-win')
    def __init__(self, squares = []):
		if len(squares) == 0:
			self.squares = [None for i in range(9)]
		else:
			self.squares = squares

    def available_moves(self):
		#empty spots
		return [k for k, v in enumerate(self.squares) if v is None]

    def available_combos(self, player):
		return self.available_moves() + self.get_squares(player)

    def complete(self):
		#Game over?
		if None not in [v for v in self.squares]:
			return True
		if self.winner() != None:
			return True
		return False

	#using in algorihm to easy check who wins
    def X_won(self):
	    return self.winner() == 'X'

    def O_won(self):
    	return self.winner() == 'O'

    def tied(self):
        return self.complete() == True and self.winner() is None
    
    def winner(self):
		for player in ('X', 'O'):
			positions = self.get_squares(player) #all squares
			for combo in self.winning_combos: #single combo
				win = True
				for pos in combo: #single piece of combo
					if pos not in positions: 
						win = False
				if win: 
					return player
		return None
	
    def get_squares(self, player):
		return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self,position, player):
		self.squares[position] = player

    def get_enemy(self,player):
    	if player == 'X':
        	return 'O'
    	return 'X'
	
	#Algorithm------------------------------------------------------------------
    def alphabeta(self, node, player, alpha, beta):
		if node.complete():
			if node.X_won():
				return -1
			if node.O_won():
				return +1
			if node.tied():
				return 0 
		for move in node.available_moves():
			node.make_move(move, player)
			val = self.alphabeta(node, self.get_enemy(player), alpha, beta)
			node.make_move(move, None)
			if player == 'O':
				alpha = max(alpha,val)
				if alpha >= beta:
					return beta
			else:
				beta = min(beta, val)
				if beta	<= alpha:
					return alpha
		if player == 'O':
			return alpha
		else:
			return beta

    def determine(self,board, player):
		a = -2
		choices = []
		if len(self.available_moves()) == 9:
			return 4
		for move in self.available_moves():
			self.make_move(move,player)
			val = self.alphabeta(board,self.get_enemy(player), -2,2)
			self.make_move(move,None)
			if val > a:
				a = val
				choices = [move]
			elif val == a:
				choices.append(move)
		return random.choice(choices)
 
if __name__ == '__main__':
  main().mainloop()
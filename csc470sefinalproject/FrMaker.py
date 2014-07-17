from cs1graphics import *
from Handler import *

class OpFr():
	def __init__(self, mainFr, ID):
		self.mainFr = mainFr
		self.ID = ID
		self.mainFr.setTitle("Operator Terminal")
		self.something = Button("Close", Point(300,350))
		self.sometext = TextBox(100,30,Point(200,200))
		self.mainFr.add(self.sometext)
		self.mainFr.add(self.something)
		x = ButtonHandler2(self.mainFr)
		self.something.addHandler(x)

	def remove(self):
		self.mainFr.remove(self.something)
		self.mainFr.remove(self.sometext)
	
	def wait(self):
		self.mainFr.wait()

class ProvFr():
	def __init__(self, mainFr,ID):
		self.mainFr = mainFr
		self.ID = ID
		self.mainFr.setTitle("Provider Terminal")
		self.something = Button("Close", Point(300,350))
		self.sometext = TextBox(100,30,Point(200,200))
		self.mainFr.add(self.sometext)
		self.mainFr.add(self.something)
		x = ButtonHandler2(self.mainFr)
		self.something.addHandler(x)

	def remove(self):
		self.mainFr.remove(self.something)
		self.mainFr.remove(self.sometext)

	def wait(self):
		self.mainFr.wait()

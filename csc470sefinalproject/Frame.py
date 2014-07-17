from cs1graphics import Canvas

class Frame:
    def __init__(self, width, height, bgColor, title):
        self.frame = Canvas(width, height, bgColor, title)
        #constructs a new Frame object
        
    def getWidth(self):
        return self.frame.getWidth()
        #returns the width of the Frame
        
    def getHeight(self):
        return self.frame.getHeight()
        #returns the height of the Frame
        
    def setWidth(self, width):
        self.frame.setWidth(width)
        #sets a new width for the Frame
        
    def setHeight(self, height):
        self.frame.setHeight(height)
        #sets a new height for the Frame

    def add(self, obj):
		self.frame.add(obj)
        #adds a new object to the Frame
	
    def getContents(self):
	    return self.frame.getContents()

    def close(self):
	    self.frame.close()

    def wait(self):
        self.frame.wait()

    def remove(self,obj):
	    self.frame.remove(obj)

    def setTitle(self,title):
	    self.frame.setTitle(title)

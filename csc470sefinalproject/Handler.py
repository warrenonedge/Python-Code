from cs1graphics import *

class ButtonHandler(EventHandler):
    def __init__(self, textObj):
        EventHandler.__init__(self)
        self.textObj = textObj

    def handle(self, event):
        if event.getDescription() == "mouse release":
           #print self.textObj.getMessage()
           None
            
class ButtonHandler2(EventHandler):
    def __init__(self, frame):
        EventHandler.__init__(self)
        self.frame = frame

    def handle(self, event):
        if event.getDescription() == "mouse release":
           self.frame.close()

class RadioHandler(EventHandler):
    def __init__(self, rad1Obj, rad2Obj):
        EventHandler.__init__(self)
        self.rad1Obj = rad1Obj
        self.rad2Obj = rad2Obj

    def handle(self, event):
        if event.getDescription() == "mouse release":
            if str(self.rad1Obj.getFillColor()) == "white": #is button unselected
                self.rad1Obj.setFillColor("black")    #select button 1
                self.rad2Obj.setFillColor("white")    #unselect button 2
                
            
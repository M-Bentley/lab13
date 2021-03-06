#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemy = drawpad.create_rectangle(200, 200, 300, 250, fill='beige')
direction = 10

enemy2 = drawpad.create_rectangle(600, 100, 750, 120, fill='pink')
direction = 20

enemy3 = drawpad.create_rectangle(500, 500, 550, 550, fill='cyan')
direction = 40

class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "red")
       	    self.down.grid(row=1,column=1)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "orange")
       	    self.left.grid(row=0,column=0)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "yellow")
       	    self.right.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.down.bind('<Button-1>', self.downClicked)
       	    self.left.bind('<Button-1>', self.leftClicked)
       	    self.right.bind('<Button-1>', self.rightClicked)
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    ex1,ex2,ey1,ey2 = drawpad.coords(enemy)
	    rx1,rx2,ry1,ry2 = drawpad.coords(enemy2)
	    qx1,qx2,qy1,qy2 = drawpad.coords(enemy3)
	    # Remember to include your "enemies" with "global"
	    global enemy
	    # Uncomment this when you're ready to test out your animation!
	    if ex2 > 800:
                direction = - 10
            elif ex1 < 0:
                direction = 10
                drawpad.move(enemy, direction, 0)
            drawpad.after(5,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)	
        
        def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player, -20, 0)
	
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player, 20, 0)
	      
app = MyApp(root)
root.mainloop()
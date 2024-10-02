import pygame as py
import math

# Initiate pygame and the modules that comes with pygame 
py.init() 
clock = py.time.Clock()
x = 900
y = 700
# setting frame/window/surface with some dimensions 
window = py.display.set_mode((x, y)) 
  
# to set title of pygame window 
py.display.set_caption("GFG") 

# creating image object 
image1 = py.image.load('./sprides/backgroundImage.jpg').convert() 
# DEFINING MAIN VARIABLES IN SCROLLING
# scroll = 0
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING
tiles = math.ceil(y  /image1.get_width()) + 1
image = py.image.load('./sprides/flappy_bird-removebg.png')
image1 = py.transform.scale(image1, (1300, 720))
image = py.transform.scale(image, (50, 50))
scroll = 0


#to display size of image 
print("size of image is (width,height):", image1.get_size(), image.get_size()) 

  
# loop to run window continuously 
while 1: 
    clock.tick(33)
    # window.blit(image1, (0, 0)) 
    # window.blit(image, (0, 0)) 
  
 # APPENDING THE IMAGE TO THE BACK OF THE SAME IMAGE
    i=0
    while(i<tiles):
        window.blit(image1, (image1.get_width()*i + scroll, 0))
        i+=1
  # FRAME FOR SCROLLING
    scroll -= 8
    window.blit(image, (100, 200))
  # RESET THE SCROLL FRAME
    if abs(scroll) > image1.get_width():
        scroll = 0
    # loop through the list of Event 
    for event in py.event.get(): 

        # to end the event/loop 
        if event.type == py.QUIT: 
  
            # it will deactivate the pygame library 
            py.quit() 
            quit() 

        # to display when screen update 
        py.display.flip()

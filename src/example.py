# filename: mystery.py
# author:   Zachary Marois
# date:     September 2011
#
# purpose:  Welcomes the user to CS1
# Modeled after the Mystery.java program for CS5
# and roll_over_button.py by Kelsey Harris

# imports
from graphics import *
import random

def welcome():    
    
    # Draw a random ellipse
    r = random.randint(0, 255)/255.0
    g = random.randint(0, 255)/255.0
    b = random.randint(0, 255)/255.0
    set_fill_color( r, g, b, .75)
    
    x = random.randint(0, 400)
    y = random.randint(0, 300)
    disable_stroke()
    draw_ellipse(x, y, 50, 40)
    
    # Draw Welcome messages
    enable_stroke()
    set_stroke_color(0, 0, 0, 1)
    if random.randint(1,2)==1:
		draw_text("Communists", x - 30, y - 5)
		draw_text("are Figs", x - 25, y + 15)
	else:
		draw_text("Communists", x - 30, y - 5)
		draw_text("are Fags", x - 25, y + 15)
start_graphics(welcome)
__author__ = "Mauro Pellanda"
__credits__ = ["Mauro Pellanda"]
__license__ = "GNU"
__version__ = "1.1.0"
__maintainer__ = "Mauro Pellanda"
__email__ = "pmauro@ethz.ch"
__status__ = "Devlopment"


''' In this file is contained the snake definition'''

def get_random_color():
    return "#%02x%02x%02x" % (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
from vec import *
import time


class Snake:

    def __init__(self):
        self.head_pos = V4(0,0,0,0) #position of the head
        self.head_dir ="UP" #direction of the head
        self.p_list = [] #store the polygon of the snake
        self.score = 0 #score
        self.score2 = 0 #number of cube taken
        self.time = 0. #boh
        self.color = [0, 255, 0] #color
        self.color_var = "up" #Variable to circulary change color


    def create_cube(self,point):
        '''This function return the polygon coordinates in a
        determined postion defined by point'''
        #calculate coordinates
        v = V4(.4,.4,.4,.4)
        higher = sum4(point,v)
        lower = sub4(point,v)
        c = cube4d(lower,higher)
        #calculate the color
        if self.color_var == "up":          
            self.color[0] += 20
            if self.color[0] > 255-21:
                self.color_var = "down"
        elif self.color_var == "down":
            self.color[0] -= 20
            if self.color[0] < 21:
                self.color_var = "up"           
        color_tuple = (self.color[0],self.color[1],self.color[2])
        c.color = "#%02x%02x%02x" % color_tuple
        #add the tag for the canvas (not used in this version)
        c.tag = "snake"
        return c

    def initialize_snake(self):
        '''it initialize the snake at the original position with 4 cubes'''
        self.__init__()
        size = 4
        for x in range(size+1):
            point = V4(0,-(size-x),0,0)
            self.p_list.append(self.create_cube(point))

    def move(self,dir):
        '''check if is a valid move in that direction, the snake cannot go
        in opposite direction'''
        no_move = False
        if dir == "UP" and self.head_dir != "DOWN":
            dir_v = V4(0,1,0,0)
        elif dir == "DOWN" and self.head_dir != "UP":
            dir_v = V4(0,-1,0,0)
        elif dir == "LEFT" and self.head_dir != "RIGHT":
            dir_v = V4(-1,0,0,0)
        elif dir == "RIGHT" and self.head_dir != "LEFT":
            dir_v = V4(1,0,0,0)
        elif dir == "FW" and self.head_dir != "RW":
            dir_v = V4(0,0,1,0)
        elif dir == "RW" and self.head_dir != "FW":
            dir_v = V4(0,0,-1,0)
        elif dir == "IN" and self.head_dir != "OUT":
            dir_v = V4(0,0,0,-1)
        elif dir == "OUT" and self.head_dir != "IN":
            dir_v = V4(0,0,0,1)
        else:
            no_move = True

        if not no_move:
            #move the snake, and append a new polygon in the new position,
            #take off the polygon from the tail, the snake is stored in the
            #list like this: [tail,->,head]
            self.head_pos = sum4(self.head_pos, dir_v)
            self.head_dir = dir
            self.p_list.pop(0)
            self.p_list.append(self.create_cube(self.head_pos))

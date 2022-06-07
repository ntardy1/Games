
'''
Nathan Tardy
Pong - A Python Rendition
'''

# Importing Modules
import pygame as pg

# Mission critical variables
run = True

win = pg.display.set_mode((500, 500))
pg.display.set_caption("Pong")

class Object:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (100, 100, 50, 50)

    def drawRect(self):
        pg.draw.rect(win, (255,0,0), self.rect)

while run:
    box = Object(100,100,50,50,(255,0,0))
    pg.draw.rect(win, (255,0,0), box.rect)

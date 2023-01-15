import pygame as py
py.init()
running = True
width,height = 800,500
screen = py.display.set_mode((width,height))
player = py.image.load('images/angry-birds.png')
bg_img = py.image.load('images/bg.png').convert()
bg_img = py.transform.scale(bg_img,(width,height))
icon_img = py.image.load('images/icon.png')
title = py.display.set_caption("Angry Bird")
icon = py.display.set_icon(icon_img)
while running:
    screen.blit(bg_img,(0, 0))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # screen.fill((255,255,255))
    screen.blit(player,(370,400))
    py.display.update()
        
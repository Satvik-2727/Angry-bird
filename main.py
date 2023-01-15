import pygame as py
py.init()
running = True
width,height = 800,500
screen = py.display.set_mode((width,height))
# player = py.image.load('images/Flappy bird.png')
bg_img = py.image.load('images/bg.png').convert()
bg_img = py.transform.scale(bg_img,(width,height))
title = py.display.set_caption("Angry Bird")
while running:
    screen.blit(bg_img,(0, 0))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # screen.fill((255,255,255))
    # screen.blit(player,(370,400))
    py.display.update()
        
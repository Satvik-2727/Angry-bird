import pygame as py
py.init()
running = True
width,height = 800,500
screen = py.display.set_mode((width,height))
bg_img = py.image.load('images/bg.png')
bg_img = py.transform.scale(bg_img,(width,height))
while running:
    screen.blit(bg_img,(0, 0))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # screen.fill((255,255,255))
    py.display.update()
        
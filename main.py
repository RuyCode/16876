#import libraries
import pygame
import Modules.view as view
from Modules.PortScan import Window

#screen
WIDTH = 384
HEIGHT = 256
FPS = 25
THEME = (35, 35, 40)

#init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MiniFramework')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
draw = screen.blit

#start
running = True
while running:

    #draw
    all_sprites.update()
    screen.fill(THEME)
    for sprite_i in view.sprites:
        draw(sprite_i, view.positions[sprite_i])
    pygame.display.flip()

    #get and analyze event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (pos_x, pos_y) = pygame.mouse.get_pos()
            if 352 <= pos_x <= 384 and 32 >= pos_y >= 0:
                exit()
            elif 0 <= pos_x <= 32 and 32 >= pos_y >= 0:
                if view.infotxt in view.sprites:
                    view.sprites.remove(view.infotxt)
                else:
                    view.sprites.append(view.infotxt)
            elif 64 < pos_x < 224 and 64 < pos_y < 91:
                win = Window()

    clock.tick(FPS)

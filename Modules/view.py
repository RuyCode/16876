#import libraryies
import pygame

#sprites
quit = pygame.image.load('Sprites/system/quit.png')
info = pygame.image.load('Sprites/system/info.png')
infotxt = pygame.image.load('Sprites/system/infotxt.png')
portscan = pygame.image.load('Sprites/programs/portscan.png')
sprites = [quit, info, portscan]

#position of sprites
positions = {
    quit : (352, 0),
    info : (0, 0),
    infotxt : (0, 32),
    portscan : (64, 64),
}

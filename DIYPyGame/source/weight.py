import sys, pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("weight.jpg").convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        
    def reset(self):
        ""
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])
        
    def update(self):
        self.rect.top += 1
        if self.rect.top > self.sceen_size[1]:
            self.reset()
        
    pygame.init()
    sceen_size = 800, 600
    pygame.display.set_mode(sceen_size,pygame.locals.FULLSCREEN)
    pygame.mouse.set_visible(0)
    
    
    
    sprites = pygame.sprite.RenderUpdates()
    sprites.add(Weight())
    
    
    screen = pygame.display.get_surface()
    bg = (255,255,255)
    screen.fill(bg)
    pygame.display.flip()
    
    def clear_callback(self,surf,rect):
        surf.fill(self.bg,rect)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.type == K_ESCAPE:
                sys.exit()
                
    sprites.clear(screen,clear_callback)
    sprites.update()
    updates = sprites.draw(screen)
    pygame.display.update(updates)
        
    
    
    
    
    
        
        
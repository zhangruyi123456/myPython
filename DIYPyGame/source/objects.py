import pygame, os
from random import randrange

from DIYPyGame.source import weightconfig


class SquishSprite(pygame.sprite.Sprite):
    
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -weightconfig.margin * 2
        self.area = screen.get_rect().inflate(shrink,shrink)
        
class Weight(SquishSprite):
    
    def __init__(self,speed):
        SquishSprite.__init__(self,weightconfig.weight_image)
        self.speed = speed;
        self.reset()
        
        
    def reset(self):
        x = randrange(self.area.left,self.area.right)
        self.rect.midbottom = x,0
        
    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom
        
class Banana(SquishSprite):
    
    def __init__(self):
        SquishSprite.__init__(self,weightconfig.banana_image)
        self.rect.bottom = self.area.bottom
        self.pad_top = weightconfig.banana_pad_top
        self.pad_side = weightconfig.banana_pad_side
    
    def upadte(self):
        
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)
        
    def touches(self,other):
        bounds = self.rect.inflate(-self.pad_side,-self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)
    
    
    
        
    
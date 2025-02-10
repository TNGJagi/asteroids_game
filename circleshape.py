import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        self.rect = pygame.Rect(x - radius, y - radius * 2, radius * 2, radius * 2)
    
    def draw(self, screen): # sub-classes must override
        pass

    
    def update(self, dt): # sub-classes must override
        pass

    
    def check_collision(self, other):
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        else:
            return False

import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)
    

    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <+ ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle1 = random.uniform(20, 50)
            random_angle2 = random.uniform(-20, -50)
           
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = self.velocity.rotate(random_angle1)
            asteroid2.velocity = self.velocity.rotate(random_angle2)

            asteroid1.add(self.groups())  # This ensures they are added to all the groups the original asteroid was in
            asteroid2.add(self.groups())

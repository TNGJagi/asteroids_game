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
        self.rect.center = (int(self.position.x), int(self.position.y))


    def split(self, scoreboard, asteroids, updatables, drawables):
        """Splits an asteroid into two smaller ones if its radius is greater than the minimum."""
        print(f"Splitting asteroid at {self.position}, radius: {self.radius}")  # ✅ Debugging print
        self.kill()  # ✅ Remove the original asteroid

        scoreboard.add_points(int(self.radius) * 10)  # ✅ Add points for destroying this asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            print("Asteroid too small to split, stopping.")  # ✅ Debugging
            return  # Stop if too small to split

        new_radius = self.radius // 2  # ✅ Make new asteroids smaller
        random_angle1 = random.uniform(20, 50)
        random_angle2 = -random_angle1

        # ✅ Create new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = self.velocity.rotate(random_angle1) * 1.2
        asteroid2.velocity = self.velocity.rotate(random_angle2) * 1.2

        # ✅ Explicitly add new asteroids to all relevant groups
        asteroid1.add(asteroids, updatables, drawables)
        asteroid2.add(asteroids, updatables, drawables)

        print("New asteroids created:", asteroid1, asteroid2)

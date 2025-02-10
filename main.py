import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

class ScoreBoard:
    def __init__(self, font, pos=(10,10), color="white"):
        self.score = 0
        self.font = font
        self.pos = pos
        self.color = color
    
    def add_points(self, points):
        self.score += points
    
    def draw(self, surface):
        try:
            score_text = self.font.render(f"Score: {self.score}", True, self.color)
            
            # Debug: Ensure the score_text is a valid object
            if not isinstance(score_text, pygame.Surface):
                print("Error: Font rendering did not return a Surface object!")

            # Debug: Ensure self.pos is a tuple of numbers
            if not (isinstance(self.pos, tuple) and len(self.pos) == 2 and all(isinstance(i, (int, float)) for i in self.pos)):
                print(f"Error: Invalid position {self.pos}, expected a tuple of two numbers!")

            surface.blit(score_text, self.pos)

        except Exception as e:
            print(f"ScoreBoard.draw() error: {e}")

def main():
    try:
        print("Starting asteroids!")
        pygame.init()
        pygame.font.init()
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0
        score = 0

        font = pygame.font.SysFont("Arial", 36)
        scoreboard = ScoreBoard(font)
        
        Player.containers = (updatables, drawables)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        Asteroid.containers = (asteroids, updatables, drawables)
        AsteroidField.containers = (updatables, )
        AsteroidField() 
        
        Shot.containers = (shots, updatables, drawables)
      
        while True:
            try:
                dt = clock.tick(MAX_FRAME_RATE) / 1000
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("quit event detected!")
                        return

                screen.fill("black")

                for updatable in updatables:
                    try:
                        updatable.update(dt)
                    except Exception as e:
                        print(f"Error updating {updatable}: {e}")

                collisions = pygame.sprite.groupcollide(shots, asteroids, True, True)
                for hit_shot, hit_asteroids in collisions.items():
                    try:
                        points = 100 * len(hit_asteroids)
                        scoreboard.add_points(points)
                    except Exception as e:
                        print(f"Error updating score: {e}")

                for asteroid in asteroids:
                    try:
                        if asteroid.check_collision(player):
                            print("Game Over!")
                            sys.exit()
                    except Exception as e:
                        print(f"Error checking collision with asteroid: {e}")

                for shot in shots:
                    for asteroid in asteroids:
                        if asteroid.check_collision(shot):  # ✅ Use circle collision detection
                            shot.kill()  # Destroy the shot
                            asteroid.split(scoreboard)
                
                for drawable in drawables:
                    try:
                        drawable.draw(screen)
                    except Exception as e:
                        print(f"Error drawing {drawable}: {e}")

                try:
                    scoreboard.draw(screen)
                except Exception as e:
                    print(f"Error drawing scoreboard: {e}")

                pygame.display.flip()

            except Exception as e:
                print(f"Main loop error: {e}")
                           
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

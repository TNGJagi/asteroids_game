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

def main():
    try:
        print("Starting asteroids!")
        pygame.init()
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        dt = 0

        Player.containers = (updatables, drawables)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        Asteroid.containers = (asteroids, updatables, drawables)
        AsteroidField.containers = (updatables, )
        AsteroidField() 
        
        Shot.containers = (shots, updatables, drawables)
      
        while True:
            dt = clock.tick(MAX_FRAME_RATE)/1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit event detected!")
                    return
            
            screen.fill("black")

            for updatable in updatables:
                updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    print("Game Over!")
                    sys.exit()
                
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.check_collision(shot):
                        asteroid.split()
                        shot.kill()
                                                        
            for drawable in drawables:
                drawable.draw(screen)
            
            pygame.display.flip()
                           
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

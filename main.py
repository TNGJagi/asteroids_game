import pygame
from constants import *

def main():
    try:
        print("Starting asteroids!")
        pygame.init()
        print("Pygame initialized")

        screen = pygame.display.set_mode((800, 600))
        print("Screen created!")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    print("quit event detected!")
                    return
            screen.fill((0, 0, 0))
            pygame.display.flip()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

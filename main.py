# First, import the warnings module
import warnings
import os

# Filter out RuntimeWarnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

# Now import pygame (after the warnings filter)
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:

        dt = clock.tick(60) / 1000    # Calculate dt
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)    # Update player and all other updatable objects

        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game over!")
                import sys
                sys.exit()

            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")    # Clear the screen

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()   # Update the display with all changes

if __name__ == "__main__":
    main()
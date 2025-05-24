import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot  

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable_groups = pygame.sprite.Group()
    drawable_groups = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable_groups, drawable_groups)
    Asteroid.containers = (asteroids, updatable_groups, drawable_groups)
    AsteroidField.containers = (updatable_groups)
    Shot.containers = (shots, updatable_groups, drawable_groups)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable_groups.update(dt)   

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

        
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
            
        screen.fill("black")

        for obj in drawable_groups:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

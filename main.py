import pygame
import sys

from logger import log_state, log_event

from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

from player import Player

from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot


def main():
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0.0
 
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return         
        dt = clock.tick(60) / 1000
        
        screen.fill((0,0,0))

        for d in drawable:
            d.draw(screen)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()



        updatable.update(dt)
        pygame.display.flip()


    #print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

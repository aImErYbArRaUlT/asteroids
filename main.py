import pygame
from logger import log_state
from constants import PLAYER_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player






def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return         
        dt = clock.tick(60) / 1000
        

        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

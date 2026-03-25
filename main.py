from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteriods, updatable, drawable)
    AsteroidField.containers = updatable
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)


if __name__ == "__main__":
    main()

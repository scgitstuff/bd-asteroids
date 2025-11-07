import pygame
import constants as CONST
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {CONST.SCREEN_WIDTH}")
    print(f"Screen height: {CONST.SCREEN_HEIGHT}")

    numpass, numfail = pygame.init()
    print(f"init: {pygame.get_init()}  numpass: {numpass}  numfail: {numfail}")

    game()


def game():
    screen = pygame.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(CONST.SCREEN_WIDTH / 2, CONST.SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        updatable.update(dt)

        for thingy in drawable:
            thingy.draw(screen)

        pygame.display.flip()

        # I do this after flip, because I want to see them crash
        # idealy leave it on screen with a crash animation
        for rock in asteroids:
            if rock.collide(player):
                log_event("player_hit")
                print("Game over!")
                pygame.quit()
                return
            for shot in shots:
                if rock.collide(shot):
                    log_event("asteroid_shot")
                    rock.split()
                    shot.kill()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

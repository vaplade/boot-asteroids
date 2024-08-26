import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    player.timer = 0

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if CircleShape.collision_check(object, player) == True:
                print("Game Over!")
                raise SystemExit
        for asteroid in asteroids:
            for shot in shots:
                if CircleShape.collision_check(shot, asteroid) == True:
                    shot.kill()
                    asteroid.split()
        pygame.Surface.fill(screen, (0,0,0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt += clock.tick(60) / 1000



if __name__ == "__main__":
    main()
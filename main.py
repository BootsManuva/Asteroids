import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0 

    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    

    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        for item in asteroids:
            if item.collision(player) == True:
                print("Game Over!")
                return pygame.quit
            for shot in shots:
                if item.collision(shot):
                    item.split()
                    shot.kill()

            
        updateable.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) /1000 # Convert milliseconds to seconds



if __name__ == "__main__":
    main()
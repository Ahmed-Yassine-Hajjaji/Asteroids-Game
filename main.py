import pygame,sys
from logger import log_state
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,PLAYER_SHOOT_SPEED
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Creating new clock object & a variable Delta time(dt) 
    # dt : represents the amount of time that has passed since the last frame was drawn
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable 
    AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable )
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        updatable.update(dt)
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid_ in asteroids:
            for shot_ in shots:
                if asteroid_.collides_with(shot_):
                    log_event("asteroid_shot")
                    asteroid_.split()
                    shot_.kill()
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit") 
                print("Game over!") 
                sys.exit()  
        pygame.display.flip()
        dt = clock.tick(60)/1000 # Pausing the game loop until 1/60th of a second has passed & Converting from milliseconds to seconds
    



if __name__ == "__main__":
    main()
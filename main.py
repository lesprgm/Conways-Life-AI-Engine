import pygame 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CELL_SIZE = 10     

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Conway's Game of Life Test")


running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill("black") 

    pygame.display.update() 

pygame.quit()
print("Pygame window closed.")
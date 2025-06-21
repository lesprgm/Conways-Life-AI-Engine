import pygame 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

CELL_SIZE = 10 

BLACK = (0, 0, 0)       
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0)     

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Conway's Game of Life Test")


running = True 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill(BLACK) 

    pygame.display.update() 

pygame.quit()
print("Pygame window closed.")
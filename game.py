import pygame

from auto import Car

pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game")

all_sprites_list = pygame.sprite.Group()
 
playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300
 
# Add the car to the list of objects
all_sprites_list.add(playerCar)

carryOn = True
 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while carryOn:
	# --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			carryOn = False # Flag that we are done so we exit this loop
 
     # --- Game logic should go here
 
     # --- Drawing code should go here
     # First, clear the screen to white.

	all_sprites_list.update()


	screen.fill(WHITE)

	all_sprites_list.draw(screen)
 
 
     # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
     
     # --- Limit to 60 frames per second
	clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
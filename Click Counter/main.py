import pygame
import sys
import mouse
import threading

clicks = 0

def on_click():
    global clicks
    clicks += 1

def main():
    pygame.init()
    screen = pygame.display.set_mode((150, 80))
    pygame.display.set_caption("Click Counter")

    # Start global mouse listener in background thread
    mouse.on_click(on_click)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill the screen with white
        screen.blit(pygame.font.SysFont(None, 36).render("Clicks", True, (0, 0, 0)), (10, 20))  # Draw text
        screen.blit(pygame.font.SysFont(None, 36).render(str(clicks), True, (0, 0, 0)), (10, 50))  # Draw click count
        pygame.display.flip()  # Update the display

main()
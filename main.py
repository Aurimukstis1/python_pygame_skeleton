import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

running = 1

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = 0

  screen.fill((0, 0, 0))
  pygame.display.flip()

pygame.quit()
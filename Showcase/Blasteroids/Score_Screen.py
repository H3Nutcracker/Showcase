import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

initials = ""

font = pygame.font.Font(None, 36)
input_rect = pygame.Rect(300, 250, 200, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = not active
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # Guardar las iniciales ingresadas
                    print("Iniciales ingresadas:", initials)
                    active = False
                    initials = ""
                elif event.key == pygame.K_BACKSPACE:
                    initials = initials[:-1]
                else:
                    initials += event.unicode

    screen.fill((255, 255, 255))
    text_surface = font.render(initials, True, color)
    width = max(200, text_surface.get_width() + 10)
    input_rect.w = width
    pygame.draw.rect(screen, color, input_rect, 2)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    pygame.display.flip()
    clock.tick(30)
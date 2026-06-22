import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lightning Generator")

clock = pygame.time.Clock()

# -----------------------------
# Generate lightning bolt
# -----------------------------
def generate_lightning(start, end, displacement, detail):
    if displacement < detail:
        return [start, end]

    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2

    mid_x += random.uniform(-displacement, displacement)
    mid_y += random.uniform(-displacement, displacement)

    left = generate_lightning(start, (mid_x, mid_y), displacement/2, detail)
    right = generate_lightning((mid_x, mid_y), end, displacement/2, detail)

    return left[:-1] + right


def draw_bolt(points, color, width):
    for i in range(len(points) - 1):
        pygame.draw.line(screen, color, points[i], points[i+1], width)


# -----------------------------
# Main loop
# -----------------------------
running = True

bolt_timer = 0
lightning_points = []

while running:
    screen.fill((10, 10, 30))  # night sky

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # regenerate lightning every few frames
    bolt_timer += 1
    if bolt_timer > 20:
        bolt_timer = 0

        start = (random.randint(100, WIDTH-100), 0)
        end = (random.randint(100, WIDTH-100), HEIGHT)

        lightning_points = generate_lightning(start, end, 120, 8)

    # draw glow layers (fake lightning bloom)
    if lightning_points:
        draw_bolt(lightning_points, (120, 120, 255), 6)  # outer glow
        draw_bolt(lightning_points, (180, 180, 255), 3)  # mid glow
        draw_bolt(lightning_points, (255, 255, 255), 1)  # core

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

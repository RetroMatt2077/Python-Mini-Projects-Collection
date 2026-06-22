import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Julia Fractal SAFE Version")

MAX_ITER = 50

# complex plane range
xmin, xmax = -1.6, 1.6
ymin, ymax = -1.2, 1.2

def julia(c):
    for y in range(HEIGHT):
        for x in range(WIDTH):

            zx = xmin + (x / WIDTH) * (xmax - xmin)
            zy = ymin + (y / HEIGHT) * (ymax - ymin)

            z = complex(zx, zy)

            i = 0
            while abs(z) < 2 and i < MAX_ITER:
                z = z*z + c
                i += 1

            color = (i * 5 % 255, i * 9 % 255, i * 15 % 255)
            screen.set_at((x, y), color)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()

    # smooth Julia parameter mapping
    c = complex(
        -0.8 + (mx / WIDTH) * 1.6,
        0.156 + (my / HEIGHT) * 1.6
    )

    julia(c)
    pygame.display.flip()

pygame.quit()

import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# =========================
# SCENES
# =========================
MENU = "menu"
GAME = "game"
GAMEOVER = "gameover"

scene = MENU

# =========================
# INPUT SYSTEM
# =========================
class Input:
    def __init__(self):
        self.keys = pygame.key.get_pressed()
        self.mouse = (0, 0)
        self.click = False

    def update(self):
        self.keys = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pos()
        self.click = False

input = Input()

# =========================
# PHYSICS ENGINE
# =========================
class PhysicsObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def apply_force(self, fx, fy):
        self.dx += fx
        self.dy += fy

    def update(self):
        self.x += self.dx
        self.y += self.dy

        self.dx *= 0.99
        self.dy *= 0.99

        # screen wrap
        self.x %= WIDTH
        self.y %= HEIGHT

# =========================
# PLAYER
# =========================
player = PhysicsObject(WIDTH//2, HEIGHT//2)

# =========================
# ENEMIES
# =========================
enemies = []

def spawn_enemy():
    return PhysicsObject(random.randint(0, WIDTH), random.randint(0, HEIGHT))

# =========================
# GAME RESET
# =========================
def reset_game():
    global player, enemies
    player = PhysicsObject(WIDTH//2, HEIGHT//2)
    enemies = [spawn_enemy() for _ in range(5)]

# =========================
# COLLISION
# =========================
def dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

# =========================
# MAIN LOOP
# =========================
running = True

while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    input.update()

    # =========================
    # EVENTS
    # =========================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            input.click = True

    # =========================
    # SCENES
    # =========================

    # -------- MENU --------
    if scene == MENU:
        font = pygame.font.SysFont(None, 50)
        text = font.render("CLICK TO START", True, (255, 255, 255))
        screen.blit(text, (250, 250))

        if input.click:
            reset_game()
            scene = GAME

    # -------- GAME --------
    elif scene == GAME:

        # INPUT MOVEMENT
        if input.keys[pygame.K_LEFT]:
            player.apply_force(-0.2, 0)
        if input.keys[pygame.K_RIGHT]:
            player.apply_force(0.2, 0)
        if input.keys[pygame.K_UP]:
            player.apply_force(0, -0.2)
        if input.keys[pygame.K_DOWN]:
            player.apply_force(0, 0.2)

        player.update()

        # ENEMIES UPDATE
        for e in enemies:
            e.update()

            # simple chase AI
            dx = player.x - e.x
            dy = player.y - e.y
            d = math.hypot(dx, dy)

            if d > 0:
                e.apply_force(dx/d * 0.05, dy/d * 0.05)

            # collision
            if dist(player, e) < 20:
                scene = GAMEOVER

        # DRAW PLAYER
        pygame.draw.circle(screen, (0, 255, 0), (int(player.x), int(player.y)), 10)

        # DRAW ENEMIES
        for e in enemies:
            pygame.draw.circle(screen, (255, 0, 0), (int(e.x), int(e.y)), 10)

    # -------- GAME OVER --------
    elif scene == GAMEOVER:
        font = pygame.font.SysFont(None, 50)
        text = font.render("GAME OVER - CLICK TO RESTART", True, (255, 0, 0))
        screen.blit(text, (120, 250))

        if input.click:
            scene = MENU

    pygame.display.flip()

pygame.quit()

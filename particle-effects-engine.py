import pygame
import random
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle System Engine")

clock = pygame.time.Clock()

# -----------------------------
# Particle Class
# -----------------------------
class Particle:
    def __init__(self, x, y, ptype="fire"):
        self.x = x
        self.y = y

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(1, 5)

        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

        self.life = random.randint(30, 100)

        self.ptype = ptype

        if ptype == "fire":
            self.color = [255, random.randint(100, 200), 0]
        elif ptype == "smoke":
            self.color = [120, 120, 120]
        else:  # spark
            self.color = [255, 255, 255]

        self.size = random.randint(2, 5)

    def update(self):
        # physics
        self.x += self.vx
        self.y += self.vy

        # gravity (different per type)
        if self.ptype == "fire":
            self.vy -= 0.05
        elif self.ptype == "smoke":
            self.vy -= 0.01
        else:
            self.vy += 0.02

        # fade life
        self.life -= 1

        # fade color
        fade = self.life / 100
        self.color = [int(c * fade) for c in self.color]

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)


# -----------------------------
# Particle System
# -----------------------------
class Emitter:
    def __init__(self, x, y, ptype="fire"):
        self.x = x
        self.y = y
        self.ptype = ptype
        self.particles = []

    def emit(self):
        for _ in range(5):
            self.particles.append(Particle(self.x, self.y, self.ptype))

    def update(self):
        self.emit()

        for p in self.particles[:]:
            p.update()
            if p.life <= 0:
                self.particles.remove(p)

    def draw(self, surface):
        for p in self.particles:
            p.draw(surface)


# -----------------------------
# Setup emitters
# -----------------------------
emitters = [
    Emitter(WIDTH//2, HEIGHT//2, "fire")
]

mode = "fire"

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # switch particle type
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "fire"
            if event.key == pygame.K_2:
                mode = "smoke"
            if event.key == pygame.K_3:
                mode = "spark"

        # move emitter with mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            emitters.append(Emitter(x, y, mode))

    # update emitters
    for e in emitters:
        e.update()
        e.draw(screen)

    # instructions
    font = pygame.font.SysFont(None, 24)
    text = font.render("1=Fire  2=Smoke  3=Spark  Click=New Emitter", True, (200,200,200))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

from config import SCREEN_WIDTH

class Cube:
    def __init__(self, x, y, mass, velocity, color, size):
        self.x = x
        self.y = y
        self.mass = mass
        self.velocity = velocity
        self.color = color
        self.size = size

    def collides_with(self, other):
        return self.x < other.x + other.size and self.x + self.size > other.x

    def resolve_collision(self, other):
        v1, v2 = self.velocity, other.velocity
        m1, m2 = self.mass, other.mass
        self.velocity = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
        other.velocity = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

        overlap = (self.x + self.size) - other.x
        if overlap > 0:
            self.x -= overlap / 2
            other.x += overlap / 2

    def update(self, dt, steps=10):
        sub_dt = dt / steps
        for _ in range(steps):
            self.x += self.velocity * sub_dt * 50

            if self.x <= 0:
                self.x = 0
                self.velocity *= -1
            elif self.x + self.size >= SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - self.size
                self.velocity *= -1

    def draw(self, screen):
        import pygame
        rect = pygame.Rect(int(self.x), int(self.y - self.size), self.size, self.size)
        pygame.draw.rect(screen, self.color, rect)

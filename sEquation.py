import math, pygame

# Window Setup
windowWidth = 500
windowHeight = 500
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Schrodinger's Equation")


class Particle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Wall:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


# The Particle
particle = Particle(250, 250, 10, (120, 60, 245))

# Walls
bottom = Wall(100, 480, 300, 20, (100, 100, 100))
left = Wall(100, 0, 20, 500, (100, 100, 100))
right = Wall(380, 0, 20, 500, (100, 100, 100))
walls = [bottom, left, right]

running = True
while running:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    particle.draw()
    for wall in walls:
        wall.draw()

    pygame.display.update()

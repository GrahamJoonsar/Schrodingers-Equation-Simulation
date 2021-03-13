import math, pygame

# Window Setup
windowWidth = 1000
windowHeight = 500
leftLimit = 0
rightLimit = 1000
globalAmplitude = 50
globalFrequency = 100
# This represents time
fakeTime = 0
pygame.init()
win = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Schrodinger's Equation")


class Particle:
    def __init__(self, x, y, radius, velocity, speed, mass, frequency, amplitude, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.velocity = velocity
        self.speed = speed
        self.mass = mass
        self.frequency = frequency
        self.amplitude = amplitude
        self.initialPosition = y
        self.color = color

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def move(self):
        # Moving back anf forth
        if leftLimit + 20 < self.x < rightLimit - 20:
            self.x += self.velocity[0]
        else:
            self.velocity[0] *= -1
            self.x += self.velocity[0]

        # self.x = pygame.mouse.get_pos()[0]
        
        # This is where the wave is generated
        self.y = math.sin(self.x/self.frequency) * self.amplitude + self.initialPosition


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
particle = Particle(250, 250, 10, [2, 0], 0, 1, 20, 25, (120, 60, 245))

particlePath = []

# Creating the path that the particle goes along
def drawPath():
    for i in range(leftLimit + 20, rightLimit - 20, 10):
        particlePath.append(Particle(i, 250, 2, [0, 0], 0, 1, 20, 25, (100, 40, 225)))

# Walls
bottom = Wall(leftLimit, 480, rightLimit - leftLimit, 20, (100, 100, 100))
left = Wall(leftLimit, 0, 20, 500, (100, 100, 100))
right = Wall(rightLimit - 20, 0, 20, 500, (100, 100, 100))
middleLine = Wall(250, 0, 2, 500, (60, 60, 60))
walls = [bottom, left, right]

drawPath()

running = True
while running:
    pygame.time.delay(10)
    fakeTime += 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill((0, 0, 0))

    # Changing the Frequency and amplitude
    globalFrequency += math.cos(fakeTime)/1.5
    #globalAmplitude += math.cos(fakeTime)/5

    # this is the line that goes down the middle of the particle
    middleLine.x = particle.x
    middleLine.draw()

    hinderance = 2.5

    # this is the code that makes the walls move
    # leftLimit += math.sin(fakeTime)/hinderance
    # left.x += math.sin(fakeTime)/hinderance
    # rightLimit -= math.sin(fakeTime)/hinderance
    # right.x -= math.sin(fakeTime)/hinderance

    # drawing the particle with the global frequency and amplitude.
    particle.frequency = globalFrequency
    particle.amplitude = globalAmplitude
    particle.draw()
    particle.move()

    for wall in walls:
        wall.draw()
    
    # Updating the particle path
    for pathParticle in particlePath:
        pathParticle.frequency = globalFrequency
        pathParticle.amplitude = globalAmplitude
        if leftLimit + 20 < pathParticle.x < rightLimit - 20:
            pathParticle.draw()
        pathParticle.move()

    pygame.display.update()

pygame.quit()

# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
generations = random.randint(10, 500)
screenColor = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

# Random color array
# [R, G, B, A, center, randomRadius]
colorList = []
for node in range(generations*4):
    R = random.randint(0, 255)
    colorList.append(R)

# Random center (x,y)
randomCenter = []
for node in range(generations*4):
    node = pygame.Vector2(random.randint(screen.get_width() - screen.get_width() + 25, screen.get_width() - 25), random.randint(screen.get_height() - screen.get_height() + 25, screen.get_height() - 25))
    randomCenter.append(node)

# Random radius array
randomRadius = []
for node in range(generations):
    node = random.randint(1, 30)
    randomRadius.append(node)


# Generate Circles
gen_counter = 0
circleList = []
while gen_counter < generations+1:
    circle = pygame.draw.circle(screen, (1,1,1), random.choice(randomCenter), random.choice(randomRadius))
    circleList.append(circle)
    gen_counter += 1


# Game Start
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(screenColor)

    # Draw circles
    for x in range(generations):
        pygame.draw.rect(screen, (colorList[x],colorList[x+1],colorList[x+2],colorList[x+3] ), circleList[x+1])


    # WASD Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
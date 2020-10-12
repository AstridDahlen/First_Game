import pygame

walkRight = [pygame.image.load("Run (1) mini.png"), pygame.image.load("Run (2) mini.png"),
             pygame.image.load("Run (3) mini.png"), pygame.image.load("Run (4) mini.png"),
             pygame.image.load("Run (5) mini.png"), pygame.image.load("Run (6) mini.png"),
             pygame.image.load("Run (7) mini.png"), pygame.image.load("Run (8) mini.png")]
walkLeft = [pygame.image.load("Run (1)Left mini.png"), pygame.image.load("Run (2)Left mini.png"),
            pygame.image.load("Run (3)Left mini.png"), pygame.image.load("Run (4)Left mini.png"),
            pygame.image.load("Run (5)Left mini.png"), pygame.image.load("Run (6)Left mini.png"),
            pygame.image.load("Run (7)Left mini.png"), pygame.image.load("Run (8)Left mini.png")]
char = pygame.image.load("Standing (1) mini.png")
# bg = pygame.image.load("space1.jpg")


x = 1
y = 700
width = 5
height = 5
vel = 50

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500, 1500))
BLACK = [0, 0, 0]

screen.fill(BLACK)
isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    screen.fill(BLACK)
    # screen.blit(bg, (0, 0))
    if walkCount + 1 >= 28:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount // 8], (x, y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount // 8], (x, y))
        walkCount += 1
    else:
        screen.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()


run = True

while run:
    clock.tick(10)

    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                is_running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 1415 - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()

    pressed_keys = pygame.key.get_pressed()

    # screen.blit(bg, (0, 0))

    pygame.display.update()

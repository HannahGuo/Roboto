import pygame
import os

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 155)

display_height = 600
display_width = 800
imageWidth = 130
imageHeight = 130
x = imageWidth
y = display_height - 155 - (imageHeight / 2)
groundHeight = display_height - 150
velocity = 5
FPS = 60
jumping = False
jumpCounter = 12
jumpBound = jumpCounter
# icon = pygame.image.load("../Roboto/images/Idle.png")
lastKey = 0
goingLeft = False
goingRight = True


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Test")
# pygame.display.set_icon(icon)
clock = pygame.time.Clock()

idleImages = [pygame.image.load("../Roboto/images/Idle1.png"),
              pygame.image.load("../Roboto/images/Idle2.png"),
              pygame.image.load("../Roboto/images/Idle3.png"),
              pygame.image.load("../Roboto/images/Idle4.png"),
              pygame.image.load("../Roboto/images/Idle5.png"),
              pygame.image.load("../Roboto/images/Idle6.png"),
              pygame.image.load("../Roboto/images/Idle7.png"),
              pygame.image.load("../Roboto/images/Idle8.png"),
              pygame.image.load("../Roboto/images/Idle9.png"),
              pygame.image.load("../Roboto/images/Idle10.png")]

runImages = [pygame.image.load("../Roboto/images/Run1.png"),
              pygame.image.load("../Roboto/images/Run2.png"),
              pygame.image.load("../Roboto/images/Run3.png"),
              pygame.image.load("../Roboto/images/Run4.png"),
              pygame.image.load("../Roboto/images/Run5.png"),
              pygame.image.load("../Roboto/images/Run6.png"),
              pygame.image.load("../Roboto/images/Run7.png"),
              pygame.image.load("../Roboto/images/Run8.png")]

jumpImages = [pygame.image.load("../Roboto/images/Jump1.png"),
              pygame.image.load("../Roboto/images/Jump2.png"),
              pygame.image.load("../Roboto/images/Jump3.png"),
              pygame.image.load("../Roboto/images/Jump4.png"),
              pygame.image.load("../Roboto/images/Jump5.png"),
              pygame.image.load("../Roboto/images/Jump6.png"),
              pygame.image.load("../Roboto/images/Jump7.png"),
              pygame.image.load("../Roboto/images/Jump8.png")]


def leftImageMode(player):
    return pygame.transform.flip(player, True, False)


rightPlayer = pygame.transform.scale(idleImages[0], (imageWidth, imageHeight))
leftPlayer = leftImageMode(rightPlayer)
currentPlayer = rightPlayer
idleCycleCount = 0
runCycleCount = 0


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (x > -30) and not keys[pygame.K_RIGHT]:
        x -= velocity
        runCycleCount += 1
        goingRight = False
        goingLeft = True
        if runCycleCount > 23:
            runCycleCount = 0
        currentPlayer = leftImageMode(pygame.transform.scale(runImages[runCycleCount//3], (imageWidth, imageHeight)))

    elif keys[pygame.K_RIGHT] and (x < 695) and not keys[pygame.K_LEFT]:
        x += velocity
        runCycleCount += 1
        goingRight = True
        goingLeft = False
        if runCycleCount > 23:
            runCycleCount = 0
        currentPlayer = pygame.transform.scale(runImages[runCycleCount // 3], (imageWidth, imageHeight))
    else:
        idleCycleCount += 1
        if idleCycleCount > 29:
            idleCycleCount = 0
        if goingLeft:
            currentPlayer = leftImageMode(
                pygame.transform.scale(idleImages[idleCycleCount // 3], (imageWidth, imageHeight)))
        else:
            currentPlayer = pygame.transform.scale(idleImages[idleCycleCount // 3], (imageWidth, imageHeight))
    if not jumping:
        if keys[pygame.K_UP]:
            jumping = True
        elif not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            idleCycleCount += 1
            if idleCycleCount > 29:
                idleCycleCount = 0
            if goingLeft:
                currentPlayer = leftImageMode(pygame.transform.scale(idleImages[idleCycleCount//3], (imageWidth, imageHeight)))
            else:
                currentPlayer = pygame.transform.scale(idleImages[idleCycleCount // 3], (imageWidth, imageHeight))
    else:
        if jumpCounter >= -(jumpBound):
            y -= (jumpCounter * 2)
            jumpCounter -= 1
            if goingRight:
                currentPlayer = pygame.transform.scale(jumpImages[jumpCounter//3], (imageWidth, imageHeight))
            else:
                currentPlayer = leftImageMode(pygame.transform.scale(jumpImages[jumpCounter // 3], (imageWidth, imageHeight)))
        else:
            jumpCounter = jumpBound
            jumping = False

    gameDisplay.fill(white)
    gameDisplay.fill(black, (0, display_height - 100, display_width, 100))
    gameDisplay.blit(currentPlayer, (x, y))

    pygame.display.update()
    clock.tick(FPS)

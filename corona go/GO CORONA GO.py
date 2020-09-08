import pygame
import random

print("HOW IS IT SHAHZAIB NAWAZ ")
print(' * * *   * * * ')
print('*      *      *')
print('  *          *')
print('   *       *')
print('     *   *')
print('       * ')

pygame.init()

screen = pygame.display.set_mode((600, 650))
pygame.display.set_caption("CORONA")
score = 0

x = 0
y = 440
width = 40
height = 60
vel = 7
red = (200, 0, 0)
green = (0, 200, 0)
white = (255, 255, 255)
black = (0, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

r = random.randrange(0, y)
t = -50

p = random.randrange(0, y)
q = -100


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def text_objects1(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def text_objects2(text, font):
    textSurface = font.render(text, True, bright_green)
    return textSurface, textSurface.get_rect()


bg = pygame.image.load("bg-morn.png").convert_alpha()
base = pygame.image.load("city--base1.png").convert_alpha()
covid1 = pygame.image.load("covid-fighter1.png").convert_alpha()
virus = pygame.image.load("virus.png").convert_alpha()
virus1 = pygame.image.load("virus1.png").convert_alpha()
BL = pygame.image.load("buttonL.png").convert_alpha()
BR = pygame.image.load("buttonR.png").convert_alpha()
BLG = pygame.image.load("buttonLglow.png").convert_alpha()
BRG = pygame.image.load("buttonRglow.png").convert_alpha()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.time.delay(50)
    screen.blit(bg, (-20, -100))
    screen.blit(base, (-15, 235))
    screen.blit(virus, (r, t))
    sd = screen.blit(covid1, (x, y))
    screen.blit(virus1, (p, q))
    screen.blit(BL, (30, 580))
    screen.blit(BR, (470, 580))

    mouse = pygame.mouse.get_pos()
    if 30+100 > mouse[0] > 30 and 580+70 > mouse[1] > 580:
        screen.blit(BLG, (25, 580))
        x -= vel
    if 470+100 > mouse[0] > 470 and 580+70 > mouse[1] > 580:
        screen.blit(BRG, (470, 580))
        x += vel

    if x > -70 - vel:
        x -= vel
    if x < 500 - width - vel:
        x += vel

    smallText3 = pygame.font.Font("freesansbold.ttf", 30)
    textSurf, textRect = text_objects("Score : {} ".format(score), smallText3)
    textRect.center = (100, 30)
    screen.blit(textSurf, textRect)
    t = t + vel
    if t >= y and (x + 30) <= r <= (x + 150):
        r = random.randrange(0, y)
        t = 0
        score += 1
        textSurf, textRect = text_objects("Score : {} ".format(score), smallText3)
        sd = pygame.mixer_music.load("sound.wav")
        pygame.mixer_music.play(0)
    if (score % 5) == 0 and score != 0:
        r = random.randrange(0, y)
        t = -70
        q = q + vel
    if q >= y and (x + 30) <= p <= (x + 150):
        sd = pygame.mixer_music.load("sound.wav")
        pygame.mixer_music.play(0)
        score += 1
        p = random.randrange(0, y)
        q = -70
    if score == 10:
        vel = 10
    if score == 20:
        vel = 12
    if score == 30:
        vel = 13
    if score == 40:
        vel = 15
    if score == 50:
        vel = 20

    if t >= 550 or q >= 550:
        vel = 0
        smallText1 = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = text_objects1("GAME OVER", smallText1)
        textRect.center = (300, 325)
        screen.blit(textSurf, textRect)

        smallText1 = pygame.font.Font("freesansbold.ttf", 30)
        textSurf, textRect = text_objects1("PLAY AGAIN", smallText1)
        textRect.center = (300, 400)
        screen.blit(textSurf, textRect)
        if 200+200 > mouse[0] > 200 and 385+100 > mouse[1] > 385:
            smallText2 = pygame.font.Font("freesansbold.ttf", 30)
            textSurf, textRect = text_objects2("PLAY AGAIN", smallText2)
            textRect.center = (300, 400)
            screen.blit(textSurf, textRect)
    pygame.display.update()
pygame.quit()

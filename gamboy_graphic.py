import pygame
import math
import random

pygame.init()

SIZE = (800,600)
TITLE = "Erik's first drawing"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


clock = pygame.time.Clock()
refresh_rate = 60

RED =(255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255,125,0)
GREY = (196, 190, 186)
MAGENTA = (196, 37, 92)
SCREEN_GREEN = (125,158,82)
GREY2 = (141,135,141)
SPACE_GREEN = (0,255,0)
SATURN = (187,162,121)
NEPTUNE = (72,115,253)
MARS = (254,132,95)

planet_colors = [GREY,NEPTUNE,SATURN,MARS]
screen.fill(BLACK)

def draw_alien(a):
    x = a[0]
    y = a[1]
    pygame.draw.rect(screen,WHITE,a)
    pygame.draw.rect(screen,BLACK,[x + 4,y+2,3,3])
    pygame.draw.rect(screen,BLACK,[x + 14,y+2,3,3])
    pygame.draw.rect(screen,BLACK,[x + 4,y+14,12,3])
    pygame.draw.rect(screen,BLACK,[x+8,y+14,4,6])
    
    
def draw_invader(x,y):
    pygame.draw.rect(screen,SPACE_GREEN,[x,y,20,10])
    pygame.draw.rect(screen,SPACE_GREEN,[x + 7.5,y-10,5,10])

def draw_planet(x,y,color):
    pygame.draw.arc(screen,GREY,[x-40,y-27,80,40],0,math.pi,5)
    pygame.draw.circle(screen,color,[x,y],25)
    pygame.draw.arc(screen,GREY,[x-40,y-35,80,50],math.pi,2*math.pi,5)

def draw_bigstar(x,y):
    pass

stars = []
aliens = []
planets = []

#makes list of aliens
for i in range(10):
    x = random.randrange(301,520)
    y = random.randrange(80,160)
    a = [x,y,20,20]
    aliens.append(a)

#makes list of stars
for i in range(50):
    x = random.randrange(301,530)
    y = random.randrange(71,240)
    r = 1
    s = [x,y,r,r]
    stars.append(s)

#make list of planets
for i in range(15):
    x = random.randrange(1,800)
    y = random.randrange(1,600)
    c = random.choice(planet_colors)
    p = [x,y,c]
    planets.append(p)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    #draw planets
    for p in planets:
        draw_planet(p[0],p[1],p[2])
        
    #body of gameboy
    pygame.draw.rect(screen,GREY,[280,50,280,440])
    
    #screen
    pygame.draw.rect(screen,BLACK,[300,70,240,180])

    #stars
    for s in stars:
        pygame.draw.ellipse(screen,WHITE,s)

    #invader
    draw_invader(410,235)

    #draw aliens
    for a in aliens:
        draw_alien(a)
    
    #a and b buttons
    pygame.draw.circle(screen,MAGENTA,[520,340],20)
    pygame.draw.circle(screen,MAGENTA,[475,365],20)

    # d-pad
    pygame.draw.rect(screen,BLACK,[340,290,20,80])
    pygame.draw.rect(screen,BLACK,[310,320,80,20])

    #screen bezel
    pygame.draw.rect(screen,GREY2,[300,70,240,180],15)

    #start and select buttons
    pygame.draw.polygon(screen,GREY2,[[380,440],[410,430]],8)
    pygame.draw.polygon(screen,GREY2,[[415,440],[445,430]],8)
    
    pygame.display.flip()
    clock.tick(refresh_rate)

pygame.quit()

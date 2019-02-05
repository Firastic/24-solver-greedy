import pygame
import time
import random
 
pygame.init()

 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
grey = (125,125,125)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)
 

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('24 Game Solver')
clock = pygame.time.Clock()
 
gameIcon = pygame.image.load('./PNG/red_back.png')

pygame.display.set_icon(gameIcon)

pause = False
#crash = True
def shuffle():
    gameDisplay.fill(white)
    button(str(card[0]),150+17.5,200,100,50,green,bright_green,None)
    button(str(card[1]),275+17.5,200,100,50,green,bright_green,None)
    button(str(card[2]),400+17.5,200,100,50,green,bright_green,None)
    button(str(card[3]),525+17.5,200,100,50,green,bright_green,None)
    Ccard = pygame.image.load('./PNG/' + str(card[0]) + '.png')
    Dcard = pygame.image.load('./PNG/' + str(13 + card[1]) + '.png')
    Hcard = pygame.image.load('./PNG/' + str(26 + card[2]) + '.png')
    Scard = pygame.image.load('./PNG/' + str(39 + card[3]) + '.png')
    gameDisplay.blit(pygame.transform.scale(Ccard,(100,153)), (150+17.5,40))
    gameDisplay.blit(pygame.transform.scale(Dcard,(100,153)), (275+17.5,40))
    gameDisplay.blit(pygame.transform.scale(Hcard,(100,153)), (400+17.5,40))
    gameDisplay.blit(pygame.transform.scale(Scard,(100,153)), (525+17.5,40))
#gameDisplay.blit(Ccard, (0,0))
#screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
#♣ Clubs 1 - 13
#♦ Diamonds 14 - 26
#♥ Hearts 27 - 39
#♠ Spades 40 - 52
    global isShuffled
    isShuffled = True
    # button("Play Again",150,450,100,50,green,bright_green,game_loop)

def lala(x):
    return (abs(24-x))

#Todo: Improve case 12 12 1 1
def solve():
	global isShuffled
	global card
	if(not isShuffled):
		return
	isShuffled = False
	arr = card
	arr.sort()
	total = sum(arr)
	cur = arr[3]
	vall = 0
	flag = False
	v = []
	if(total <= 20 and arr[3]*arr[2] >= 32):
		if(arr[0] != 1):
			arr[0],arr[2] = arr[2],arr[0]
		else:
			arr[1],arr[2] = arr[2],arr[1]
	for j in range(2,-1,-1):
		if(cur*arr[j] >= 6 and cur*arr[j] <= 35 and ((arr[j] != 1 and not flag) or (cur == 24 and j == 0))):
			v.append('*');
			vall += 3;
			cur *= arr[j];
		else:
			flag = True;
			if(lala(cur+arr[j]) <= lala(cur-arr[j])):
				v.append('+');
				vall += 5;
				cur += arr[j];
			else:
				v.append('-');
				vall += 4;
				cur -= arr[j];			
	arr.reverse()
	for j in range(4):
		button(str(arr[j])+' ',150+j*2*75,350,50,50,green,bright_green,None)
		if(j < 3):
			button(str(v[j])+' ',150+(j*2+1)*75,350,50,50,green,bright_green,None)
	button('result :' + str(cur), display_width/2-50, 400,100,50,green,bright_green,None)
	button('operator\'s point:' + str(vall), display_width/2-100,450,200,50,green,bright_green,None)
	card = [random.randrange(1,13),random.randrange(1,13),random.randrange(1,13),random.randrange(1,13)]
# button("Play Again",150,450,100,50,green,bright_green,game_loop)


def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))
 
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
 
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
 
 
def crash():
    ####################################
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    ####################################
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)   


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(grey)
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("24 Game Solver", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        global isShuffled
        isShuffled = False
        button("Start",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def game_loop():
    global pause
    global card
    
    card = [random.randrange(1,13),random.randrange(1,13),random.randrange(1,13),random.randrange(1,13)]
    ############
    #pygame.mixer.music.load('jazz.wav')
    #pygame.mixer.music.play(-1)
    ############
    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    dodged = 0
 
    gameExit = False
    gameDisplay.fill(white)
    while not gameExit:
        
        for event in pygame.event.get():
			
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            button("Shuffle",150,450,100,50,green,bright_green,shuffle)
            button("Solve",550,450,100,50,red,bright_red,solve)
        
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
import pygame
import time
import random
import sys
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

myfont = "buvard"

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('24 Game Solver')
clock = pygame.time.Clock()

gameIcon = pygame.image.load('./PNG/red_back.png')
pygame.display.set_icon(gameIcon)
def shuffle():
    gameDisplay.fill(white)
    button(str(card[0]),150+17.5,200,100,50,white,bright_green,None)
    button(str(card[1]),275+17.5,200,100,50,white,bright_green,None)
    button(str(card[2]),400+17.5,200,100,50,white,bright_green,None)
    button(str(card[3]),525+17.5,200,100,50,white,bright_green,None)
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

def dist(x):
    return (abs(24-x))

def solve(arr):
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
			if(dist(cur+arr[j]) <= dist(cur-arr[j])):
				v.append('+');
				vall += 5;
				cur += arr[j];
			else:
				v.append('-');
				vall += 4;
				cur -= arr[j];
	arr.reverse()
	for j in range(4):
		print(arr[j],end=' ')
		if(j < 3):
			print(v[j],end=' ')

#Todo: Improve case 12 12 1 1
def game_solve():
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
			if(dist(cur+arr[j]) <= dist(cur-arr[j])):
				v.append('+');
				vall += 5;
				cur += arr[j];
			else:
				v.append('-');
				vall += 4;
				cur -= arr[j];
	arr.reverse()
	for j in range(4):
		button(str(arr[j])+' ',150+j*2*75,350,50,50,white,white,None)
		if(j < 3):
			button(str(v[j])+' ',150+(j*2+1)*75,350,50,50,white,white,None)
	button('result :' + str(cur), display_width/2-50, 400,100,50,white,white,None)
	button('operator\'s point:' + str(vall), display_width/2-100,450,200,50,white,white,None)
	card = [random.randrange(1,13),random.randrange(1,13),random.randrange(1,13),random.randrange(1,13)]

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont(myfont,20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()



def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(grey)
        largeText = pygame.font.SysFont(myfont,100)
        TextSurf, TextRect = text_objects("24 Game Solver", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        global isShuffled
        isShuffled = False
        button("Start",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def keyb_inp():
	print('\n')
	card[0] = int(input("Input your 1st card: "))
	card[1] = int(input("Input your 2nd card: "))
	card[2] = int(input("Input your 3rd card: "))
	card[3] = int(input("Input your 4th card: "))		
		
def rfileext():
    pygame.quit()
    inputFile = input("Masukkan nama file input! ")
    outputFile = input("Masukkan nama file output! ")
    orig_stdout = sys.stdout
    orig_stdin = sys.stdin
    fin = open(inputFile, 'r')
    fout = open(outputFile, 'w')
    sys.stdin = fin
    sys.stdout = fout
    a,b,c,d = map(int, input().split())
    card = [a,b,c,d]
    solve(card)
    sys.stdout = orig_stdout
    sys.stdin = orig_stdin
    print("file telah di save di ",outputFile)
    fin.close()
    fout.close()
    quit()
def game_loop():
    global card

    card = [random.randrange(1,13),random.randrange(1,13),random.randrange(1,13),random.randrange(1,13)]
    gameExit = False
    gameDisplay.fill(white)
    while not gameExit:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            button("Input",250,525,100,50,green,bright_green,keyb_inp)
            button("Shuffle",150,450,100,50,green,bright_green,shuffle)
            button("Solve",550,450,100,50,red,bright_red,game_solve)
            button("Input File",450,525,100,50,green,bright_green,rfileext)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shuffle()
                if event.key == pygame.K_RIGHT:
                    game_solve()


        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()

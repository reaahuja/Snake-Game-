#import of libraries
import pygame, sys, math, random
from pygame.locals import *

# Set the width and height of the screen [width,height]
w=800
h=600

# Menu cover
a= pygame.image.load('Start Up.jpg')
b= pygame.image.load('Instruction_1.jpg')
c= pygame.image.load('Instruction_2.jpg')

pygame.init()

# Used to manage how fast the screen updates
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption ('Tron')

# Music that will repeat
pygame.mixer.music.load('Get Dripped.mp3')
pygame.mixer.music.play(-1)

# Menu screen counters

menu = -2
gamestart=0
aigamestart=0

# Function to draw upon images
def image(x):
    """image(x)- Returnns comands for picture display after a round is over"""
    screen.blit(x,(0,0))
    pygame.display.update()
    pygame.time.delay(1000)

# Scoring images
_0_1 = pygame.image.load('0-1.jpg')
_0_2 = pygame.image.load('0-2.jpg')
_0_3 = pygame.image.load('0-3.jpg')
_1_0 = pygame.image.load('1-0.jpg')
_1_1 = pygame.image.load('1-1.jpg')
_1_2 = pygame.image.load('1-2.jpg')
_1_3 = pygame.image.load('1-3.jpg')
_2_0 = pygame.image.load('2-0.jpg')
_2_1 = pygame.image.load('2-1.jpg')
_2_2 = pygame.image.load('2-2.jpg')
_2_3 = pygame.image.load('2-3.jpg')
_3_0 = pygame.image.load('3-0.jpg')
_3_1 = pygame.image.load('3-1.jpg')
_3_2 = pygame.image.load('3-2.jpg')


tie=pygame.image.load ('Tie.jpg')
red_round=pygame.image.load('Red_round.jpg')
blue_round=pygame.image.load('Blue_round.jpg')

p1winner = pygame.image.load('Blue_win.jpg')
p2winner = pygame.image.load('Red_win.jpg')


# Define some colors
red = 255,0,0
blue = 0,0,255

# -------- Main Program Loop -----------        
while True:
    # Loading screen
    if menu ==-2:
        while True:
            screen.fill (pygame.Color (0,0,0))
            screen.blit(a,(0,0))
            pygame.display.update()
            for event in pygame.event.get():  
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        menu+=1
            if menu == -1:
                break                
            fpsClock.tick(100) 
            
    # Instruction screen
    if menu ==-1:
        while True:
            screen.fill (pygame.Color (0,0,0))
            screen.blit(b,(0,0))
            pygame.display.update()
            for event in pygame.event.get():  
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        menu+=1
            if menu == 0:
                break                
            fpsClock.tick(100) 
    
    # Instruction screen
    if menu ==0:
        while True:
            screen.fill (pygame.Color (0,0,0))
            screen.blit(c,(0,0))
            pygame.display.update()
            for event in pygame.event.get():  
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        menu+=1
            if menu == 1:
                break                
            fpsClock.tick(100) 
    # Main Menu
    if menu==1:
        while True:
            screen.blit(pygame.image.load('Menu 1.jpg'),(0,0))
            pygame.display.update()
            
            for event in pygame.event.get():  
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        menu+=1
                    if event.key == K_RETURN:
                        gamestart+=1
            if menu != 1:
                break
            if gamestart == 1:
                break
            fpsClock.tick(100)  
    # 2 Player Game
    if gamestart==1:
        while True:
            # scoring counters
            p1_score = 0
            p2_score = 0
            
            while True:
                pygame.init()
                screen = pygame.display.set_mode((w,h))
                #start off positions 
                cor_x = 600
                cor_y = 300
                length = [[600,300]]
                position = cor_y,cor_x
                direc = 4 
                
                cor_x1 = 200
                cor_y1 = 300
                length1 = [[200,300]]
                position1 = cor_y1,cor_x1
                direc1 = 6 
                
                #loops to direct breaking mechanism
                loop3 = 0
                loop4 = 0
                while True:
                    # moveent
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                            if event.key == K_UP and direc != 2:
                                direc = 8
                            if event.key == K_RIGHT and direc != 4:
                                direc = 6                
                            if event.key == K_LEFT and direc != 6:
                                direc = 4
                            if event.key == K_DOWN and direc != 8:
                                direc = 2
                            if event.key == K_w and direc1 != 2:
                                direc1 = 8
                            if event.key == K_d and direc1 != 4:
                                direc1 = 6                
                            if event.key == K_a and direc1 != 6:
                                direc1 = 4
                            if event.key == K_s and direc1 != 8:
                                direc1 = 2
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                    
                    # Adding to line
                    if direc == 8:
                        cor_y -= 1
                    elif direc == 6:
                        cor_x += 1
                    elif direc == 4:
                        cor_x -= 1
                    elif direc == 2:
                        cor_y += 1 
                    length.append([cor_x,cor_y])
                    
                    #checking line on itself
                    count = length.count([cor_x,cor_y]) 
                    if count == 2:
                        loop4+=1
                        break
                    if cor_y <= 0 or cor_y >= h or cor_x <= 0 or cor_x >= w:
                        loop4+=1
                        break
                    
                    #drawing the line
                    cor = cor_x,cor_y,5,5 
                    
                    pygame.draw.rect(screen, blue, cor, 0)
                    
                    #second line adding             
                    if direc1 == 8:
                        cor_y1 -= 1
                    elif direc1 == 6:
                        cor_x1 += 1
                    elif direc1 == 4:
                        cor_x1 -= 1
                    elif direc1 == 2:
                        cor_y1 += 1
                    length1.append([cor_x1,cor_y1])
                    
                    #second line checking itself
                    count1 = length1.count([cor_x1,cor_y1]) 
                    if count1 == 2:
                        loop3+=1
                        break
                    if cor_y1 <= 0 or cor_y1 >= h or cor_x1 <= 0 or cor_x1 >= w:
                        loop3+=1
                        break
                    
                    #lines detecting for any intercepts
                    count3 = length.count([cor_x1,cor_y1])
                    count4 = length1.count([cor_x,cor_y])
                    if count3 == 1:
                        loop3+=1
                        if count4 == 1:
                            loop4+=1
                            break
                        else:
                            break
                    
                    if count4 == 1:
                        loop4+=1
                        break
                    
                    # delay as screen never resets, just gets added to, allows for minimal lag
                    pygame.time.delay(10) 
                    
                    #drawing the line
                    cor1 = cor_x1,cor_y1,5,5
                    
                    pygame.draw.rect(screen, red, cor1, 0)
                    pygame.display.update()
                
                # showing images
                if loop3==1 and loop4==1:
                        image(tie)
                        pygame.time.delay(1000)
                
                elif loop3==1:
                        image(blue_round)
                        p2_score+=1
                        pygame.time.delay(1000)
                    
                elif loop4==1:
                        image(red_round)
                        p1_score+=1
                        pygame.time.delay(1000)
                
                if p1_score ==0 and p2_score==1:
                    image(_0_1)
                    
                elif p1_score ==0 and p2_score==2:
                    image(_0_2)
                
                elif p1_score ==0 and p2_score==3:
                    image(_0_3)
                    image(p1winner)
                    break
                    
                elif p1_score ==1 and p2_score==0:
                    image(_1_0)
                
                elif p1_score ==1 and p2_score==1:
                    image(_1_1)
                
                elif p1_score ==1 and p2_score==2:
                    image(_1_2)
                
                elif p1_score ==1 and p2_score==3:
                    image(_1_3)
                    image(p1winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==2 and p2_score==0:
                    image(_2_0)
                
                elif p1_score ==2 and p2_score==1:
                    image(_2_1)
                    
                elif p1_score ==2 and p2_score==2:
                    image(_2_2)
                
                elif p1_score ==2 and p2_score==3:
                    image(_2_3)
                    image(p1winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==3 and p2_score==0:
                    image(_3_0)
                    image(p2winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==3 and p2_score==1:  
                    image(_3_1)
                    image(p2winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==3 and p2_score==2:  
                    image(_3_2)
                    image(p2winner)
                    pygame.time.delay(1000)
                    break
            
            #breaking loop to menu screen     
            if p1_score ==0 and p2_score==3:
                gamestart-=1
                break
            elif p1_score ==1 and p2_score==3:
                gamestart-=1
                break
            elif p1_score ==2 and p2_score==3:
                gamestart-=1
                break
            elif p1_score ==3 and p2_score==0:
                gamestart-=1
                break
            elif p1_score ==3 and p2_score==1: 
                gamestart-=1
                break
            elif p1_score ==3 and p2_score==2: 
                gamestart-=1
                break
    
    # Menu screen part
    if menu ==2:
        while True:
            screen.blit(pygame.image.load('Menu 2.jpg'),(0,0))
            pygame.display.update()
            
            for event in pygame.event.get():  
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        menu+=1
                    if event.key == K_UP:
                        menu-=1
                    if event.key == K_RETURN:
                        aigamestart+=1
            if menu != 2:
                break
            if aigamestart == 1:
                break
            fpsClock.tick(100)
    
    #CPU Vs Player ------Same functions as above except for CPU parts--------
    if aigamestart==1:
        while True:
            p1_score = 0
            p2_score = 0
            
            while True:
                pygame.init()
                screen = pygame.display.set_mode((w,h))
                cor_x = 600
                cor_y = 300
                length = [[600,300]]
                position = cor_y,cor_x
                direc = 4 
                
                cor_x1 = 300
                cor_y1 = 300
                length1 = [[300,300]]
                position1 = cor_y1,cor_x1
                direc1 = 6 
                
                
                loop3 = 0
                loop4 = 0
                
                #ai counter for the 50 tick
                ai_count=0
                while True:
                    ai_count+=1
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                pygame.quit()
                                sys.exit()
                            if event.key == K_UP and direc != 2:
                                direc = 8
                            if event.key == K_RIGHT and direc != 4:
                                direc = 6                
                            if event.key == K_LEFT and direc != 6:
                                direc = 4
                            if event.key == K_DOWN and direc != 8:
                                direc = 2
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                    
                    if direc == 8:
                        cor_y -= 1
                    elif direc == 6:
                        cor_x += 1
                    elif direc == 4:
                        cor_x -= 1
                    elif direc == 2:
                        cor_y += 1 
                    length.append([cor_x,cor_y])
                    
                    count = length.count([cor_x,cor_y]) 
                    if count == 2:
                        loop4+=1
                        break
                    if cor_y <= 0 or cor_y >= h or cor_x <= 0 or cor_x >= w:
                        loop4+=1
                        break
                    
                    cor = cor_x,cor_y,5,5 
                    
                    pygame.draw.rect(screen, blue, cor, 0)
                    
                    #allows for the random to occur afterwards, so line does not turn on itself           
                    current_direc = direc1
                    
                    # make the CPU react only after every 50 loops, so delays how fast the turns occur
                    if ai_count==50:
                        direc_ai_all = [8,6,4,2]
                        direc1 = random.choice(direc_ai_all)
                        if current_direc == 2:
                            direc_ai = [6,4,2,2]
                            direc1 = random.choice(direc_ai)
                            
                        if current_direc == 4:
                            direc_ai1 = [8,4,4,2]
                            direc1 = random.choice(direc_ai1)   
                                     
                        if current_direc == 6:
                            direc_ai2 = [8,6,6,2]
                            direc1 = random.choice(direc_ai2)
                            
                        if current_direc == 8:
                            direc_ai3 = [8,8,6,4]
                            direc1 = random.choice(direc_ai3)
                        ai_count= 0
                        
                    if direc1 == 8:
                        cor_y1 -= 1        
                    elif direc1 == 6:
                        cor_x1 += 1
                    elif direc1 == 4:
                        cor_x1 -= 1
                    elif direc1 == 2:
                        cor_y1 += 1                   
                    length1.append([cor_x1,cor_y1])
                    
                    count1 = length1.count([cor_x1,cor_y1]) 
                    if count1 == 2:
                        loop3+=1
                        break
                    if cor_y1 <= 0 or cor_y1 >= h or cor_x1 <= 0 or cor_x1 >= w:
                        loop3+=1
                        break
                    
                    count3 = length.count([cor_x1,cor_y1])
                    count4 = length1.count([cor_x,cor_y])
                    if count3 == 1:
                        loop3+=1
                        if count4 == 1:
                            loop4+=1
                            break
                        else:
                            break
                    
                    if count4 == 1:
                        loop4+=1
                        break
                        
                            
                    pygame.time.delay(10) 
                    cor1 = cor_x1,cor_y1,5,5
                    
                    pygame.draw.rect(screen, red, cor1, 0)
                    pygame.display.update()
                    
                if loop3==1 and loop4==1:
                        image(tie)
                        pygame.time.delay(1000)
                
                elif loop3==1:
                        image(blue_round)
                        p2_score+=1
                        pygame.time.delay(1000)
                    
                elif loop4==1:
                        image(red_round)
                        p1_score+=1
                        pygame.time.delay(1000)
                
                if p1_score ==0 and p2_score==1:
                    image(_0_1)
                    
                elif p1_score ==0 and p2_score==2:
                    image(_0_2)
                
                elif p1_score ==0 and p2_score==3:
                    image(_0_3)
                    image(p1winner)
                    break
                    
                elif p1_score ==1 and p2_score==0:
                    image(_1_0)
                
                elif p1_score ==1 and p2_score==1:
                    image(_1_1)
                
                elif p1_score ==1 and p2_score==2:
                    image(_1_2)
                
                elif p1_score ==1 and p2_score==3:
                    image(_1_3)
                    image(p1winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==2 and p2_score==0:
                    image(_2_0)
                
                elif p1_score ==2 and p2_score==1:
                    image(_2_1)
                    
                elif p1_score ==2 and p2_score==2:
                    image(_2_2)
                
                elif p1_score ==2 and p2_score==3:
                    image(_2_3)
                    image(p1winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==3 and p2_score==0:
                    image(_3_0)
                    image(p2winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==3 and p2_score==1:  
                    image(_3_1)
                    image(p2winner)
                    pygame.time.delay(1000)
                    break
                
                elif p1_score ==3 and p2_score==2:  
                    image(_3_2)
                    image(p2winner)
                    pygame.time.delay(1000)
                    break
                 
            if p1_score ==0 and p2_score==3:
                aigamestart-=1
                break
            elif p1_score ==1 and p2_score==3:
                aigamestart-=1
                break
            elif p1_score ==2 and p2_score==3:
                aigamestart-=1
                break
            elif p1_score ==3 and p2_score==0:
                aigamestart-=1
                break
            elif p1_score ==3 and p2_score==1: 
                aigamestart-=1
                break
            elif p1_score ==3 and p2_score==2: 
                aigamestart-=1
                break
    #Menu screen
    if menu ==3:
        # Exiting program
        while True:
            screen.blit(pygame.image.load('Menu 3.jpg'),(0,0))
            pygame.display.update()
            
            for event in pygame.event.get():  
                if event.type == KEYDOWN:
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_UP:
                        menu-=1
                    if event.key == K_RETURN:
                        pygame.quit()
                        sys.exit()
            if menu != 3:
                break
            fpsClock.tick(100)

    
         
    
    
    

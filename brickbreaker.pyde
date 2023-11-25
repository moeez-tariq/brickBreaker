#import libraries
add_library("minim")
player = Minim(this)
import random
import time
import os

path = os.getcwd() #get current working directory

#initialize constants
DIMENSIONS_HEIGHT = 500
DIMENSIONS_WIDTH = 750
BRICK_WIDTH = 50
BRICK_HEIGHT = 25
BALL_HEIGHT = 17
TOTAL_COLS = DIMENSIONS_WIDTH/BRICK_WIDTH
TOTAL_ROWS = DIMENSIONS_HEIGHT/BRICK_HEIGHT

#gridlines used for debugging
# def gridlines():
#     for i in range(DIMENSIONS_WIDTH + 1):
#         if i % BRICK_WIDTH == 0:
#             line(i, 0, i, DIMENSIONS_HEIGHT)
#         if i % BRICK_HEIGHT  == 0:
#             line(0, i, DIMENSIONS_WIDTH, i)

#brick class
class Brick():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visibility = False 
        self.hardness = 1
        
    #changes hardness of the brick    
    def changeHardness(self, hardness):
        if hardness == 3:
            self.hardness = 3
            
        elif hardness == 2:
            self.hardness = 2
            
        elif hardness == 1:
            self.hardness = 1
            
        elif hardness == 0:
            self.hardness = 0
            self.visibility = False #the brick ceases to exist for user

#levels class            
class Levels():
    def __init__(self):
        self.brick3 = loadImage(path + "/images/brick3.jpg") #load images for each brick hardness
        self.brick2 = loadImage(path + "/images/brick2.jpg")
        self.brick1 = loadImage(path + "/images/brick1.jpg")
        self.xvelocity = 6 #velocity defined here if we want to increase velocity every level
        self.yvelocity = 5 #not done in this game to make it easier/not too hard
        self.currentlevel = 1
        self.gamelist = []
        self.gamewon = False
        #fills gamelist with bricks
        for rows in range(TOTAL_ROWS):
            rowlist = []
            for cols in range(TOTAL_COLS):
                brick = Brick()
                rowlist.append(brick)
            self.gamelist.append(rowlist)    
        self.makeLevel1()
        
    # displays level 
    def display(self):
        self.count = 0
        for row in range(TOTAL_ROWS):
            for col in range(TOTAL_COLS):
                if self.gamelist[row][col].visibility == True:
                    self.count += 1
                    if self.gamelist[row][col].hardness == 3:
                        image(self.brick3, self.gamelist[row][col].x, self.gamelist[row][col].y, BRICK_WIDTH, BRICK_HEIGHT)
                    elif self.gamelist[row][col].hardness == 2:
                        image(self.brick2, self.gamelist[row][col].x, self.gamelist[row][col].y, BRICK_WIDTH, BRICK_HEIGHT)
                    elif self.gamelist[row][col].hardness == 1:
                        image(self.brick1, self.gamelist[row][col].x, self.gamelist[row][col].y, BRICK_WIDTH, BRICK_HEIGHT)
                        
        #if none of the bricks is visible, change level                
        if self.count == 0:
            self.changelevel()
    
    def changelevel(self):
        if self.currentlevel == 1:
            self.makeLevel2()
        elif self.currentlevel == 2:
            self.makeLevel3()
        elif self.currentlevel == 3:
            self.makeLevel4()
        elif self.currentlevel == 4:
            self.makeLevel5()
        else:
            self.gamewon = True
        #sets the ball and the paddle to starting position and status
        global ball
        ball = Ball()
        paddle.permission = False
        paddle.revertback = False
        paddle.x = (DIMENSIONS_WIDTH/2) - (1.5*BRICK_WIDTH)
        paddle.y = DIMENSIONS_HEIGHT - BRICK_HEIGHT
        paddle.lengthofpaddle = 3*BRICK_WIDTH
        self.currentlevel += 1
        
    #level 1 defined with bricks of different hardness
    def makeLevel1(self):
       for i in range(DIMENSIONS_WIDTH + 1):
            for row in range(0, 10, 3):
                if i >= BRICK_WIDTH and i <= DIMENSIONS_WIDTH - 2*BRICK_WIDTH and i % (2*BRICK_WIDTH) == 0:
                    col = i/BRICK_WIDTH
                    self.gamelist[row][col].x = col * BRICK_WIDTH
                    self.gamelist[row][col].y = row * BRICK_HEIGHT
                    self.gamelist[row][col].visibility = True
                    self.gamelist[row][col].changeHardness(1)
        
                    if row == 3 or row == 9:
                        self.gamelist[row][col].changeHardness(2)
                    if row == 6:
                        self.gamelist[row][col].changeHardness(3)
    
    def makeLevel2(self):
        for i in range(DIMENSIONS_WIDTH + 1):
            for row in range(0,8):
                if i >= 350 - (row * BRICK_WIDTH) and i <= 350 + (row * BRICK_WIDTH) and i % BRICK_WIDTH == 0:
                    col = i/BRICK_WIDTH
                    self.gamelist[row][col].x = col * BRICK_WIDTH
                    self.gamelist[row][col].y = row * BRICK_HEIGHT
                    self.gamelist[row][col].visibility = True
                    self.gamelist[row][col].changeHardness(1)
                    
                    if i % 100 == 0:
                        self.gamelist[row][col].changeHardness(2)    
                
    def makeLevel3(self):
        for i in range(DIMENSIONS_WIDTH + 1):
            for row in range(5,12):
                if i >= 2*BRICK_WIDTH and i <= DIMENSIONS_WIDTH - 3*BRICK_WIDTH and i % BRICK_WIDTH == 0:
                    col = i/BRICK_WIDTH
                    self.gamelist[row][col].x = col * BRICK_WIDTH
                    self.gamelist[row][col].y = row * BRICK_HEIGHT
                    self.gamelist[row][col].visibility = True
                    self.gamelist[row][col].changeHardness(2)
                    if i % 100 == 0:
                        self.gamelist[row][col].changeHardness(3)
                        
    def makeLevel4(self):
        for i in range(DIMENSIONS_WIDTH + 1):
            for row in range(0,13):
                if row <= 6:
                    if i >= 350 - (row * BRICK_WIDTH) and i <= 350 + (row * BRICK_WIDTH) and i % BRICK_WIDTH == 0:
                        col = i/BRICK_WIDTH
                        self.gamelist[row][col].x = col * BRICK_WIDTH
                        self.gamelist[row][col].y = row * BRICK_HEIGHT
                        self.gamelist[row][col].visibility = True
                        self.gamelist[row][col].changeHardness(3)
                        if i % 100 == 0:
                            self.gamelist[row][col].changeHardness(2)                    
                else:
                    if i >= 350 - ((row - 6) * BRICK_WIDTH) and i <= 350 + ((row - 6) * BRICK_WIDTH) and i % BRICK_WIDTH == 0:
                        col = i/BRICK_WIDTH
                        self.gamelist[row][col].x = col * BRICK_WIDTH
                        self.gamelist[row][col].y = row * BRICK_HEIGHT
                        self.gamelist[row][col].visibility = True
                        self.gamelist[row][col].changeHardness(3)
                        if i % 100 == 0:
                            self.gamelist[row][col].changeHardness(2)
    
    def makeLevel5(self):
        for i in range(DIMENSIONS_WIDTH + 1):
            for row in range(1,18):
                if i >= 0 and i <= DIMENSIONS_WIDTH - BRICK_WIDTH and i % BRICK_WIDTH == 0:
                    col = i/BRICK_WIDTH
                    self.gamelist[row][col].x = col * BRICK_WIDTH
                    self.gamelist[row][col].y = row * BRICK_HEIGHT
                    self.gamelist[row][col].visibility = True
                    self.gamelist[row][col].changeHardness(3)
                
#paddle class                            
class Paddle():
    def __init__(self):
        self.x = (DIMENSIONS_WIDTH/2) - (1.5*BRICK_WIDTH)
        self.y = DIMENSIONS_HEIGHT - BRICK_HEIGHT
        self.velocity = BRICK_WIDTH/2
        self.lengthofpaddle = BRICK_WIDTH*3  
        self.leftboundarytouch = False
        self.rightboundarytouch = False
        self.permission = False
        self.life = 3
        self.gameover = False
        self.timecount = 0
        self.starttime = 0
        self.endtime = 0
        self.revertback = False
        self.paddleimage = loadImage(path + "/images/paddle1.jpg")
        self.bg_sound = player.loadFile(path + "/bgmusic.mp3") #loads music
        self.bg_sound.loop() #loops music
    
    #restricts the movement of paddle within the bounds
    def outofbounds(self):
        if self.x <= 0:
            self.leftboundarytouch = True
        elif self.x + self.lengthofpaddle >= DIMENSIONS_WIDTH:
            self.rightboundarytouch = True
            
    #movement of paddle        
    def movement(self):
        self.outofbounds()
        if key == CODED and self.permission == True:
            if keyCode == RIGHT and self.rightboundarytouch == False:
                self.x = self.x + self.velocity
            elif keyCode == LEFT and self.leftboundarytouch == False:
                self.x = self.x - self.velocity
        self.leftboundarytouch = False
        self.rightboundarytouch = False
    
    #size of paddle increases when powerup caught    
    def increasesize(self):
        if self.timecount == 0: #so that start time is noted only once
            self.starttime = time.time() #starts time
            self.timecount += 1
        self.x = self.x - BRICK_WIDTH/2
        self.lengthofpaddle += BRICK_WIDTH
        self.revertback = True
    
    def originalsize(self):
        self.endtime = time.time()
        if self.endtime - self.starttime > 10: #if the powerup has been on for 10 seconds, revert back to original size
            self.x = self.x + BRICK_WIDTH/2
            self.lengthofpaddle -= BRICK_WIDTH
            self.revertback = False
            
    #adds life when powerup caught
    def addlife(self):
        self.life += 1
        
    def display(self):
        if self.revertback == True:
            self.originalsize()
        image(self.paddleimage, self.x, self.y, self.lengthofpaddle, BRICK_HEIGHT)

#ball class
class Ball():
    def __init__(self):
        self.x = DIMENSIONS_WIDTH/2
        self.y = DIMENSIONS_HEIGHT - BRICK_HEIGHT - BALL_HEIGHT/2
        self.xvelocity = level.xvelocity
        self.yvelocity = level.yvelocity
        self.r, self.g, self.b = 30,255,30
        self.bounce = 1
        self.start = False
        self.paddlepart = 1
        self.sideboundarytouch = False
        self.upboundarytouch = False
        self.tempcheckdown = False
        self.tempcheckside = False
        self.tempcheckup = False
        self.strong_ball = False
        self.startcount = 0
        self.starttime = 0
        self.endtime = 0
        self.revertback = False
        self.guarded = False
        self.upmovementdictionary = {0:4, 1:3, 2:5, 3:1, 4:0, 6:9, 7:8, 8:7, 9:6}
        self.downmovementdictionary = {0:9, 1:8, 2:5, 3:7, 4:6, 5:5, 6:9, 7:8, 8:7, 9:6}
        self.brickupmovementdictionary = {0:9, 1:8, 2:5, 3:7, 4:6, 6:4, 7:3, 8:1, 9:0}
        self.brickdownmovementdictionary = {5:2, 6:4, 7:3, 8:1, 9:0}
    
    #ball and paddle would only move when up key pressed
    def ballstart(self):
        if keyCode == UP:
            self.start = True
            paddle.permission = True
    
    #ball hitting the side boundary
    def sideboundary(self):
        if (self.x - BALL_HEIGHT/2 <= DIMENSIONS_WIDTH + 6 and self.x + BALL_HEIGHT/2 >= DIMENSIONS_WIDTH - 6) or (self.x - BALL_HEIGHT/2 <= 6 and self.x + BALL_HEIGHT/2 >= 6):
            self.sideboundarytouch = True
            self.bounce += 1
        else:
            if self.tempcheckside == False: #if it hasn't already hit brick side boundary
                self.sideboundarytouch = False
    
    #ball hitting the up boundary        
    def upboundary(self):
        if self.y - BALL_HEIGHT/2 < 0:
            self.upboundarytouch = True
            self.bounce += 1
        else:
            if self.tempcheckdown == False and self.tempcheckup == False: #if it hasn't already hit brick up and down boundary
                self.upboundarytouch = False
    
    #brick down boundary hit    
    def brickdownboundary(self):
        self.tempcheckdown = False
        for row in range(TOTAL_ROWS):
            for col in range(TOTAL_COLS): #loop through all the bricks
                if level.gamelist[row][col].visibility == True:  #choose only the bricks that are visible
                    if self.paddlepart == 0 or self.paddlepart == 1 or self.paddlepart == 2 or self.paddlepart == 3 or self.paddlepart == 4:
                        if self.y - BALL_HEIGHT/2 <= level.gamelist[row][col].y + BRICK_HEIGHT and self.y - BALL_HEIGHT/2 >= level.gamelist[row][col].y + (0.8*BRICK_HEIGHT) and ((self.x - BALL_HEIGHT/2 > level.gamelist[row][col].x and self.x - BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH) or (self.x + BALL_HEIGHT/2 > level.gamelist[row][col].x and self.x + BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH)):
                            if self.strong_ball == True: #strong ball will make brick of any hardness completely vanish
                                level.gamelist[row][col].hardness = 1
                            level.gamelist[row][col].changeHardness(level.gamelist[row][col].hardness - 1) #decreases brick hardness by 1
                            self.upboundarytouch = True 
                            self.tempcheckdown = True
                            self.bounce += 1
                            break
                        else:
                            self.upboundarytouch = False
                            self.tempcheckdown = False
            if self.tempcheckdown == True:
                break
    
    #same logic as brickdown boundary        
    def brickupboundary(self):
        self.tempcheckup = False
        for row in range(TOTAL_ROWS):
            for col in range(TOTAL_COLS):
                if level.gamelist[row][col].visibility == True:
                    if self.paddlepart == 6 or self.paddlepart == 7 or self.paddlepart == 8 or self.paddlepart == 9 or self.paddlepart == 5:
                        if self.y + BALL_HEIGHT/2 >= level.gamelist[row][col].y and self.y + BALL_HEIGHT/2 <= level.gamelist[row][col].y + BRICK_HEIGHT/2 and self.x + BALL_HEIGHT/2 >= level.gamelist[row][col].x and self.x - BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH:
                            if self.strong_ball == True:
                                level.gamelist[row][col].hardness = 1
                            level.gamelist[row][col].changeHardness(level.gamelist[row][col].hardness - 1)
                            self.upboundarytouch = True
                            self.tempcheckup = True
                            self.bounce += 1
                            break
                        else:
                            if self.tempcheckdown == False:
                                self.upboundarytouch = False
                                self.tempcheckup = False
            if self.tempcheckup == True:
                break
    
    #brick side boundary takes into account all 4 corners as well
    def bricksideboundary(self):
        self.tempcheckside = False
        for row in range(TOTAL_ROWS):
            for col in range(TOTAL_COLS):
                if level.gamelist[row][col].visibility == True:
                    if self.y - BALL_HEIGHT/2 <= level.gamelist[row][col].y + BRICK_HEIGHT and self.y - BALL_HEIGHT/2 >= level.gamelist[row][col].y and self.x - BALL_HEIGHT/2 >= level.gamelist[row][col].x and self.x - BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH:
                        if self.strong_ball == True:
                                level.gamelist[row][col].hardness = 1
                        level.gamelist[row][col].changeHardness(level.gamelist[row][col].hardness - 1)
                        self.sideboundarytouch = True
                        self.tempcheckside = True
                        self.bounce += 1
                        break
                    elif self.y + BALL_HEIGHT/2 <= level.gamelist[row][col].y + BRICK_HEIGHT and self.y + BALL_HEIGHT/2 >= level.gamelist[row][col].y and self.x - BALL_HEIGHT/2 >= level.gamelist[row][col].x and self.x - BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH:
                        if self.strong_ball == True:
                                level.gamelist[row][col].hardness = 1
                        level.gamelist[row][col].changeHardness(level.gamelist[row][col].hardness - 1)
                        self.sideboundarytouch = True
                        self.tempcheckside = True
                        self.bounce += 1
                        break
                    elif self.y + BALL_HEIGHT/2 <= level.gamelist[row][col].y + BRICK_HEIGHT and self.y + BALL_HEIGHT/2 >= level.gamelist[row][col].y and self.x + BALL_HEIGHT/2 >= level.gamelist[row][col].x and self.x + BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH:
                        if self.strong_ball == True:
                                level.gamelist[row][col].hardness = 1
                        level.gamelist[row][col].changeHardness(level.gamelist[row][col].hardness - 1)
                        self.sideboundarytouch = True
                        self.tempcheckside = True
                        self.bounce += 1
                        break
                    elif self.y - BALL_HEIGHT/2 <= level.gamelist[row][col].y + BRICK_HEIGHT and self.y - BALL_HEIGHT/2 >= level.gamelist[row][col].y and self.x +BALL_HEIGHT/2 >= level.gamelist[row][col].x and self.x + BALL_HEIGHT/2 <= level.gamelist[row][col].x + BRICK_WIDTH:
                        if self.strong_ball == True:
                                level.gamelist[row][col].hardness = 1
                        level.gamelist[row][col].changeHardness(level.gamelist[row][col].hardness - 1)
                        self.sideboundarytouch = True
                        self.tempcheckside = True
                        self.bounce += 1
                        break
                    else:
                        self.sideboundarytouch = False
                        self.tempcheckside = False
            if self.tempcheckside == True:
                break
    
    #paddle part defined out of the 5 parts to encourage ball movement in the appropriate direction
    def definepaddlepart(self):
        if self.x + BALL_HEIGHT/2 <= paddle.x + 1*(paddle.lengthofpaddle/5) and self.x + BALL_HEIGHT/2 >= paddle.x and self.y >= DIMENSIONS_HEIGHT - BRICK_HEIGHT - BALL_HEIGHT/2 and self.y <= DIMENSIONS_HEIGHT - (0.5*BRICK_HEIGHT):
            self.paddlepart = 0
            self.bounce += 1

        elif self.x <= paddle.x + 2*(paddle.lengthofpaddle/5) and self.x + BALL_HEIGHT/2 >= paddle.x and self.y >= DIMENSIONS_HEIGHT - BRICK_HEIGHT - BALL_HEIGHT/2 and self.y <= DIMENSIONS_HEIGHT - (0.5*BRICK_HEIGHT):
            self.paddlepart = 1
            self.bounce += 1

        elif self.x <= paddle.x + 3*(paddle.lengthofpaddle/5) and self.x + BALL_HEIGHT/2 >= paddle.x and self.y >= DIMENSIONS_HEIGHT - BRICK_HEIGHT - BALL_HEIGHT/2 and self.y <= DIMENSIONS_HEIGHT - (0.5*BRICK_HEIGHT):
            self.paddlepart = 2
            if self.start == True:
                self.bounce += 1

        elif self.x <= paddle.x + 4*(paddle.lengthofpaddle/5) and self.x + BALL_HEIGHT/2 >= paddle.x and self.y >= DIMENSIONS_HEIGHT - BRICK_HEIGHT - BALL_HEIGHT/2 and self.y <= DIMENSIONS_HEIGHT - (0.5*BRICK_HEIGHT):
            self.paddlepart = 3
            self.bounce += 1

        elif self.x - BALL_HEIGHT/2 <= paddle.x + 5*(paddle.lengthofpaddle/5) and self.x + BALL_HEIGHT/2 >= self.x + BALL_HEIGHT/2 >= paddle.x and self.y >= DIMENSIONS_HEIGHT - BRICK_HEIGHT - BALL_HEIGHT/2 and self.y <= DIMENSIONS_HEIGHT - (0.5*BRICK_HEIGHT):
            self.paddlepart = 4
            self.bounce += 1
    
    #ball movement
    def movement(self):
        sideinelse = False
        self.definepaddlepart()
        if self.start == True:
            if self.upboundarytouch == True:
               self.sideboundarytouch = False #ensuring any overlapping of boundaries is discarded
                   
            if self.sideboundarytouch == False: 
                if self.upboundarytouch == False:
                    if self.paddlepart == 0: #right to left up movement
                        self.x = self.x - self.xvelocity
                        self.y = self.y - self.yvelocity/2 #decreases the angle of trajectory
                        
                    elif self.paddlepart == 1: #right to left up movement
                        self.x = self.x - self.xvelocity
                        self.y = self.y - self.yvelocity
                        
                    elif self.paddlepart == 3: #left to right up movement
                        self.x = self.x + self.xvelocity
                        self.y = self.y - self.yvelocity
                        
                    elif self.paddlepart == 4: #left to right up movement
                        self.x = self.x + self.xvelocity
                        self.y = self.y - self.yvelocity/2   
            else:
                self.paddlepart = self.upmovementdictionary[self.paddlepart] #takes the current paddlepart and then changes it to a reflection of it with the boundary
                self.sideboundarytouch = False
                sideinelse = True
            
            if self.upboundarytouch == False:
                if self.paddlepart == 2: #up movement
                    self.y = self.y - self.xvelocity 
                
                elif self.paddlepart == 5: #down movement
                    self.y = self.y + self.xvelocity
                
                elif self.paddlepart == 6: #left to right down movement
                    self.x = self.x + self.xvelocity
                    self.y = self.y + self.yvelocity/2
                
                elif self.paddlepart == 7: #left to right down movement
                    self.x = self.x + self.xvelocity
                    self.y = self.y + self.yvelocity
                
                elif self.paddlepart == 8: #right to left down movement
                    self.x = self.x - self.xvelocity
                    self.y = self.y + self.yvelocity
                    
                elif self.paddlepart == 9:  #right to left down movement
                    self.x = self.x - self.xvelocity
                    self.y = self.y + self.yvelocity/2
                
                self.brickdownboundary()  
                self.brickupboundary()
                self.upboundary()
            else:
                if self.tempcheckdown == True or self.tempcheckup == True:
                    self.paddlepart = self.brickupmovementdictionary[self.paddlepart]
                    self.upboundarytouch = False
                else:
                    self.paddlepart = self.downmovementdictionary[self.paddlepart]
                    self.upboundarytouch = False
                    
        if sideinelse == False and self.tempcheckdown == False and self.tempcheckup == False:
            self.bricksideboundary()
            self.sideboundary()
    
    #losing a life when the ball goes below paddle
    def lifelost(self):
        if self.y >= DIMENSIONS_HEIGHT:
            if self.guarded == False: #checking if the shield was off or not. if not only then decrease life
                paddle.life -= 1
            #setting the ball and paddle to their original position and status
            global ball
            ball = Ball()
            paddle.permission = False
            paddle.revertback = False
            paddle.x = (DIMENSIONS_WIDTH/2) - (1.5*BRICK_WIDTH)
            paddle.y = DIMENSIONS_HEIGHT - BRICK_HEIGHT
            paddle.lengthofpaddle = 3*BRICK_WIDTH
            #paddle.revertback 
            if paddle.life == 0: #game is over when lives are 0
                paddle.gameover = True
    
    def strongballpowerup(self):
        if self.timecount == 0:
            self.starttime = time.time()
            self.timecount += 1
        self.strong_ball = True
        self.revertback = True
        #changes color of the ball to differentiate from normal ball
        self.r = 255
        self.g = 50
        self.b = 50
    
    def originalball(self):
        self.endtime = time.time()
        if self.endtime - self.starttime > 10:  #reverts to normal ball after 10 seconds
            self.revertback = False
            self.strong_ball = False
            self.r, self.g, self.b = 30,255,30
    
    #activates shield if powerup is caught        
    def shield_on(self):
        if self.timecount == 0:
            self.starttime = time.time()
            self.timecount += 1
        self.guarded = True
        fill(25, 25, 200)
        rect(0, DIMENSIONS_HEIGHT - BRICK_HEIGHT/4, DIMENSIONS_WIDTH, BRICK_HEIGHT/4)
    
    def shield_off(self):
        self.endtime = time.time()
        if self.endtime - self.starttime > 20: #deactivates shield after 20 seconds
            self.guarded = False    
                
    def display(self):
        if self.revertback == True:
            self.originalball()
        if self.guarded == True:
            self.shield_on()
            self.shield_off()
            
        self.lifelost()
        fill(self.r, self.g, self.b)
        circle(self.x, self.y, BALL_HEIGHT)
            

#powerups class
class Powerups():
    def __init__(self):
        self.x = random.randint(0, DIMENSIONS_WIDTH - BRICK_HEIGHT)
        self.y = -BRICK_HEIGHT
        self.velocity = BRICK_HEIGHT/6
        self.r = 0
        self.g = 0
        self.b = 0
        self.drop = False
        self.visibility = True
        self.type = random.randint(1,4) #randomly chosen powerup
        self.shield = loadImage(path + "/images/shield.png")
        self.enlarge = loadImage(path + "/images/enlarge.png")
        self.fireball = loadImage(path + "/images/fireball.png")
        self.heart = loadImage(path + "/images/heart.png")

        
    def poweritup(self):
        if self.type == 1: #shield
            ball.timecount = 0
            ball.shield_on()
            
        elif self.type == 2: #paddlesize
            paddle.timecount = 0
            paddle.increasesize()
            
        elif self.type == 3: #strong ball
            ball.timecount = 0
            ball.strongballpowerup()
            
        elif self.type == 4: #additional life
            paddle.addlife()
    
    #checking to see if powerup is caught    
    def caught(self):
        if self.x + BRICK_HEIGHT >= paddle.x and self.x <= paddle.x + paddle.lengthofpaddle and self.y >= DIMENSIONS_HEIGHT - (2*BRICK_HEIGHT) and self.y <= DIMENSIONS_HEIGHT - (BRICK_HEIGHT):
            self.visibility = False
            return True

    #powerup widget falling    
    def falling(self):
        self.y = self.y + self.velocity
        temp = self.caught() #if caught 
        if self.y >= DIMENSIONS_HEIGHT - BRICK_HEIGHT/2 or self.visibility == False:
            ball.bounce = 1 #set bounce back to 1 so that it can restart for next poweup
            if temp == True:
                self.poweritup() #after powerup is called and implemented
            global powerup
            powerup = Powerups() #reinstantiate powerup to reset its position and new random type
            
    def display(self):
        self.falling()
        self.choice()
    
    #randomly chosen powerup
    def choice(self):
        if self.type == 1: #shield
            image(self.shield, self.x, self.y, BRICK_HEIGHT, BRICK_HEIGHT)
            
        elif self.type == 2: #paddlesize
            image(self.enlarge, self.x, self.y, BRICK_HEIGHT, BRICK_HEIGHT)
            
        elif self.type == 3: #strong ball
            image(self.fireball, self.x, self.y, BRICK_HEIGHT, BRICK_HEIGHT)
            
        elif self.type == 4: #additional life
            image(self.heart, self.x, self.y, BRICK_HEIGHT, BRICK_HEIGHT)
            
paddle = Paddle() 
level = Levels()
ball = Ball()
powerup = Powerups()
bg = loadImage(path + "/images/bg.jpg")
lose = loadImage(path + "/images/lose.png")
win = loadImage(path + "/images/win.png")
instruct = loadImage(path + "/images/instruct.png")
instructions_over = False

def setup():
    size(DIMENSIONS_WIDTH, DIMENSIONS_HEIGHT)
    background(205)
    
def draw():
    #ensuring only instructions are loaded and not the game until the user presses down key
    if instructions_over == False:
        image(instruct, 0, 0, DIMENSIONS_WIDTH, DIMENSIONS_HEIGHT)
    else:
        if frameCount % 1 == 0:
            global bg
            image(bg, 0, 0, DIMENSIONS_WIDTH, DIMENSIONS_HEIGHT)
            #gridlines()
            paddle.display()
            ball.movement()
            ball.display()
            level.display()
            fill(255, 255, 255)
            textSize(20)
            text("Lives: " + str(paddle.life), 0 ,20)
            #drop powerup after every 70 bounces
            if ball.bounce % 70 == 0:
                powerup.drop = True
            if powerup.drop == True:
                powerup.display()
            if paddle.gameover:
                image(lose, 0, 0, DIMENSIONS_WIDTH, DIMENSIONS_HEIGHT)
            elif level.gamewon:
                image(win, 0, 0, DIMENSIONS_WIDTH, DIMENSIONS_HEIGHT)
            
def keyPressed():
    global instructions_over
    
    if keyCode == DOWN:
        instructions_over = True
            
    if instructions_over == True:
        ball.ballstart()
        paddle.movement()

#restarts the game and resets everything
def mouseClicked():
    global paddle, ball, level, powerup, instructions_over
    if paddle.gameover == True or level.gamewon == True:
        instructions_over = False
        paddle = Paddle() 
        ball = Ball()
        level = Levels()
        powerup = Powerups()

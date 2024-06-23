import random
import pygame as pg

square_width = 50
square_height = 50

class Agent:
    def __init__(self, game):
        self.game = game
        self.agent_icon= pg.image.load("graphics/agent.jpg").convert_alpha()
        self.agent_rect = pg.Rect(self.game.screen_width/2-square_width,self.game.screen_height-square_height,square_height,square_width)

    def draw(self):
        self.game.screen.blit(self.agent_icon, self.agent_rect)
        
    def draw_ai(self):
        self.agent_rect=pg.Rect(self.game.aI.current_col-square_width,self.game.aI.current_row-square_height,square_width,square_height)
        start_rect=pg.Rect(self.game.screen_width/2-square_width,self.game.screen_height-square_height,square_height,square_width)
        pg.draw.rect(self.game.screen, "green", start_rect)
        self.game.screen.blit(self.agent_icon, self.agent_rect)
        
    def go_up(self):
        # Move the square up
        self.agent_rect.bottom -= square_height
        for block in self.game.blocks.blocks:
            if self.agent_rect.colliderect(block):
                self.agent_rect.top = block.bottom
        if self.agent_rect.top==0:
            pg.display.set_caption("You Win!")
            self.game.game_active = False
            
    def go_down(self):
        # Move the square down
        self.agent_rect.bottom += square_height
        if self.agent_rect.bottom > self.game.screen_height:
            self.agent_rect.bottom = self.game.screen_height
        for block in self.game.blocks.blocks:
            if self.agent_rect.colliderect(block):
                self.agent_rect.bottom = block.top
                
    def go_left(self):
        # Move the square left
        self.agent_rect.left -= square_width
        if self.agent_rect.left < 0:
            self.agent_rect.left = 0
        for block in self.game.blocks.blocks:
            if self.agent_rect.colliderect(block):
                self.agent_rect.left = block.right
                
    def go_right(self):
        # Move the square right
        self.agent_rect.right += square_width
        if self.agent_rect.right > self.game.screen_width:
            self.agent_rect.right = self.game.screen_width
        for block in self.game.blocks.blocks:
            if self.agent_rect.colliderect(block):
                self.agent_rect.right = block.left
    
    def control(self,event):
        if event.type == pg.KEYDOWN and self.game.game_active:
            self.game.score -= 1
            if event.key == pg.K_UP:
                self.go_up()
            elif event.key == pg.K_DOWN:
                self.go_down()
            elif event.key == pg.K_LEFT:
                self.go_left()
            elif event.key == pg.K_RIGHT:
                self.go_right()
    
        
        


class Blocks_In_Game:
    def __init__(self, game):
        self.game = game
        self.blocks = []
        self.block_color='yellow'
        # block_y = int(game.screen_height/square_height*.75) #random.randint(0, 6)
        # block_x = int(game.screen_width/square_width/4) #random.randint(0, 7)
        block_y=4
        block_x=2
        random.seed(2023-5-1140)
        for i in range(block_y):  # choose raw
            for j in range(block_x):
                in_raw= random.randint(0,int(game.screen_width/square_width)-1)
                addition_square=pg.Rect(in_raw*square_width, i*square_height, square_width, square_height)
                self.blocks.append(addition_square)

    def draw(self):
        for block in self.blocks:
            pg.draw.rect(self.game.screen, self.block_color, block)
    

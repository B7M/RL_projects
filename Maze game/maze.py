"""
Reinforcement learning example with off policy Q-learning.

Yellow rectangles:  walls      [reward = -100]
Top row :           Nirvana    [reward = +10]
All other states:   Path       [reward = -1]
"""


import pygame as pg
import maze_objects
import ai
""" define the environment """

class Maze():
    epsilon=.95 # exploration rate
    
    def __init__(self):
        pg.init()
        self.player='human' # 'human' or 'ai'
        self.screen_width = 200
        self.screen_height = 300
        self.clock = pg.time.Clock()
        self.screen=pg.display.set_mode((self.screen_width, self.screen_height)) 
        self.running=True
        self.game_active=True
        self.new_game()
        
    
        
    def update(self):
        pg.display.update()
        self.clock.tick(10)
        
    def build_maze(self):
        background_image = pg.image.load("graphics/sky.jpg").convert()
        self.screen.blit(background_image, (0, 0))
        if self.score == 0:
            pg.display.set_caption("Move the Square to the Top")
        else:
            pg.display.set_caption("Score: " + str(self.score))
        
    def new_game(self):
        self.agent = maze_objects.Agent(self)
        self.blocks = maze_objects.Blocks_In_Game(self)
            
    def draw(self):
        if self.player == 'human':
            if self.game_active:
                self.build_maze()
                self.blocks.draw()
                self.agent.draw()
            else:
                self.screen.fill((255, 255, 255)) # white screen
                score_font = pg.font.Font(None, 50)
                score_surface = score_font.render("Score: " + str(self.score),False,(0,0,0))
                score_rect = score_surface.get_rect(center = (self.screen_width/2, self.screen_height/2))
                self.screen.blit(score_surface, score_rect)
        elif self.player == 'ai':
            if self.game_active:
                self.build_maze()
                self.blocks.draw()
                self.agent.draw_ai()
            else:
                self.screen.fill((255, 255, 255)) # white
                score_font = pg.font.Font(None, 50)
                score_surface = score_font.render("Score: " + str(self.score),False,(0,0,0))
                score_rect = score_surface.get_rect(center = (self.screen_width/2, self.screen_height/2))
                self.screen.blit(score_surface, score_rect)
                self.score = 0
    
    def events(self):
        if self.player == 'human':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                self.agent.control(event)
        elif self.player == 'ai':
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    pg.quit()
            self.aI.AI_learning()
            
    
    def run(self):
        if self.player == 'human':
            self.score = 0
            while self.running:
                self.events()
                self.update()
                self.draw()
        elif self.player == 'ai':
            self.score = 0
            self.aI=ai.AI(self)
            while self.running:
                self.events()
                self.update()
        
        
        
if __name__ == '__main__':
    game = Maze()
    game.run()
    
    
    
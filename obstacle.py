import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        '''
        Flappy Bird pipe spawning logic
        '''
        self.rect_y_down = randint(400, 600)
        self.rect_y_up = randint(100, 300)
        if self.rect_y_down > self.rect_y_up:
            bigger = self.rect_y_down
            smaller = self.rect_y_up
        else: bigger = self.rect_y_up; smaller = self.rect_y_down

        if bigger - smaller < 100:
            if self.rect_y_down > self.rect_y_up:
                self.rect_y_down -= 100
            else:
                self.rect_y_up += 100
        if bigger - smaller > 400:
            if self.rect_y_down > self.rect_y_up:
                self.rect_y_down += 100
            else:
                self.rect_y_up += 100

        self.type = type
        self.pipe_green = pygame.image.load('assets/sprites/pipe-green.png').convert_alpha()
        self.pipe_green = pygame.transform.scale(self.pipe_green, (100, 700))
        # self.pipe_red = pygame.image.load('assets/sprites/pipe-red.png').convert_alpha()
        # self.pipe_red = pygame.transform.scale(self.pipe_red, (100, 700))
        # self.pipe_list = [self.pipe_green, self.pipe_red]
        # self.pipe_index = 0
        # self.image = self.pipe_list[self.pipe_index]
        self.image = self.pipe_green
        self.rect = self.image.get_rect(midtop=(800, self.rect_y_down))
        if self.type == 'up_pipe':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(midbottom=(800, self.rect_y_up))
        
    def move_obstacles(self):
        self.rect.x -= 2
        if self.rect.x < -100:
            self.kill()

    def update(self):
        self.move_obstacles()
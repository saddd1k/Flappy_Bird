import pygame
from bird import Bird
from obstacle import Obstacle
from textures import *

def collision_sprite():
    if pygame.sprite.spritecollide(bird.sprite, obstacle_group, False) or pygame.Rect.colliderect(bird.sprite.rect, bottom_base_rect):
        if pygame.Rect.colliderect(bird.sprite.rect, bottom_base_rect):
            bird.sprite.die.play()
        else:
            bird.sprite.hit.play()
        bird.sprite.rect = bird.sprite.image.get_rect(center=(50, 256))
        bird.sprite.gravity = 0
        obstacle_group.empty()
        return False
    return True

def check_score(score):
    for obstacles in obstacle_group:
        if bird.sprite.rect.centerx == obstacles.rect.centerx:
            bird.sprite.point.play()
            score += 0.5
    return score

def score_displayer(score):
    for index, digit in enumerate(str(int(score))):
        if index < len(digit_rects):
            screen.blit(score_surfs[digit], digit_rects[index])

# Initialization
pygame.display.set_caption('Flappy Bird Modded')
pygame.display.set_icon(pygame.image.load('assets/favicon.ico'))
clock = pygame.time.Clock()
score = 0
game_active = False
start_screen = True

# Classes
bird = pygame.sprite.GroupSingle()
bird.add(Bird())
obstacle_group = pygame.sprite.Group()

# Timers
pipe_timer = pygame.USEREVENT + 2
pygame.time.set_timer(pipe_timer, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_active:
                bird.sprite.bird_input()
            else:
                obstacle_group.empty()
                game_active = True
                start_screen = False
        if event.type == pipe_timer:
            obstacle_group.add(Obstacle('down_pipe'))
            obstacle_group.add(Obstacle('up_pipe'))

    screen.blit(background_surf, (0, 0))
    obstacle_group.draw(screen)
    obstacle_group.update()
    
    if game_active:
        bird.draw(screen)
        bird.update()
        game_active = collision_sprite()
        score = check_score(score)
        score_displayer(score)
    elif start_screen:
        screen.blit(get_ready_surf, get_ready_rect)
    else:
        screen.blit(game_over_surf, game_over_rect)
        score = 0
    screen.blit(base_surf, base_rect)
    
    pygame.display.update()
    clock.tick(240)
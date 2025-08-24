import pygame

pygame.init()
screen = pygame.display.set_mode((576, 1024))

# Background
background_surf = pygame.image.load('assets/sprites/background-day.png')
background_surf = pygame.transform.scale2x(background_surf)

# Base
base_surf = pygame.image.load('assets/sprites/base.png')
base_surf = pygame.transform.scale2x(base_surf)
base_rect = base_surf.get_rect(topleft=(0, 900))
bottom_base_rect = base_surf.get_rect(midbottom=(0, 1250)) # for better triggers

# Get Ready
get_ready_surf = pygame.image.load('assets/sprites/message.png').convert_alpha()
get_ready_surf = pygame.transform.scale2x(get_ready_surf)
get_ready_rect = get_ready_surf.get_rect(center=(288, 512))

# Game over
game_over_surf = pygame.image.load('assets/sprites/gameover.png').convert_alpha()
game_over_surf = pygame.transform.scale2x(game_over_surf)
game_over_rect = game_over_surf.get_rect(center=(288, 512))

# Score
score_0_surf = pygame.image.load('assets/sprites/0.png')
score_1_surf = pygame.image.load('assets/sprites/1.png')
score_2_surf = pygame.image.load('assets/sprites/2.png')
score_3_surf = pygame.image.load('assets/sprites/3.png')
score_4_surf = pygame.image.load('assets/sprites/4.png')
score_5_surf = pygame.image.load('assets/sprites/5.png')
score_6_surf = pygame.image.load('assets/sprites/6.png')
score_7_surf = pygame.image.load('assets/sprites/7.png')
score_8_surf = pygame.image.load('assets/sprites/8.png')
score_9_surf = pygame.image.load('assets/sprites/9.png')
score_0_surf = pygame.transform.scale2x(score_0_surf)
score_1_surf = pygame.transform.scale2x(score_1_surf)
score_2_surf = pygame.transform.scale2x(score_2_surf)
score_3_surf = pygame.transform.scale2x(score_3_surf)
score_4_surf = pygame.transform.scale2x(score_4_surf)
score_5_surf = pygame.transform.scale2x(score_5_surf)
score_6_surf = pygame.transform.scale2x(score_6_surf)
score_7_surf = pygame.transform.scale2x(score_7_surf)
score_8_surf = pygame.transform.scale2x(score_8_surf)
score_9_surf = pygame.transform.scale2x(score_9_surf)
score_surfs = {
    '0': score_0_surf,
    '1': score_1_surf,
    '2': score_2_surf,
    '3': score_3_surf,
    '4': score_4_surf,
    '5': score_5_surf,
    '6': score_6_surf,
    '7': score_7_surf,
    '8': score_8_surf,
    '9': score_9_surf
}
score_first_digit_rect = score_0_surf.get_rect(topleft=(280, 100))
score_second_digit_rect = score_0_surf.get_rect(topleft=(325, 100))
score_third_digit_rect = score_0_surf.get_rect(topleft=(370, 100))
digit_rects = [score_first_digit_rect, score_second_digit_rect, score_third_digit_rect]
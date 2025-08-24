import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.yellow_bird_mid = pygame.image.load('assets/sprites/yellowbird-midflap.png').convert_alpha()
        self.yellow_bird_down = pygame.image.load('assets/sprites/yellowbird-downflap.png').convert_alpha()
        self.yellow_bird_up = pygame.image.load('assets/sprites/yellowbird-upflap.png').convert_alpha()
        self.yellow_bird = [self.yellow_bird_up, self.yellow_bird_mid, self.yellow_bird_down]
        self.bird_index = 0
        self.die = pygame.mixer.Sound('assets/audio/die.wav')
        self.hit = pygame.mixer.Sound('assets/audio/hit.wav')
        self.point = pygame.mixer.Sound('assets/audio/point.wav')
        self.swoosh = pygame.mixer.Sound('assets/audio/swoosh.wav')
        self.wing = pygame.mixer.Sound('assets/audio/wing.wav')
        self.wing.set_volume(0.1)
        self.swoosh.set_volume(0.1)
        self.point.set_volume(0.03)
        self.hit.set_volume(0.1)
        self.die.set_volume(0.1)
        self.image = self.yellow_bird[self.bird_index]
        self.rect = self.image.get_rect(center=(50, 256))
        self.gravity = 0

    def bird_input(self):
        self.wing.play()
        self.gravity = -3

    def apply_gravity(self):
        # self.gravity = min(self.gravity, 10)
        self.gravity += 0.05
        self.rect.y += self.gravity

    def animate_bird(self):
        self.bird_index += 0.1
        if self.bird_index >= len(self.yellow_bird):
            self.bird_index = 0
        self.image = self.yellow_bird[int(self.bird_index)]
        self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.rotozoom(self.image, -self.gravity * 3, 1) # rotation
    
    def update(self):
        self.animate_bird()
        self.apply_gravity()
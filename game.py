import pygame
from random import randint
from os import path

from new_hiscore import run_hiscore

# Framerate
FPS = 30

# Images
bg = (0, 130, 0)
diglett_img = pygame.image.load(path.join('images', 'diglett.png'))

# Classes
class Diglett():
    def __init__(self, screen:pygame.Surface):
        self.x = randint(0, screen.get_width()-130)
        self.y = randint(0, screen.get_height()-130)
        self.hitbox = (self.x, self.y, 130, 130)
        self.timer = Timer(2)
    
    def draw(self, win:pygame.Surface):
        win.blit(diglett_img, (self.x, self.y))


class Timer():
    def __init__(self, time:int):
        self.time = time
        self.font = pygame.font.Font('freesansbold.ttf', 18)
    
    def count_down(self, frame_count:int):
        if frame_count == FPS:
            self.time -= 1

    def draw(self, win:pygame.Surface):
        text = self.font.render(f'Time: {str(self.time)}', True, (255,255,255))
        text_rect = text.get_rect()
        win.blit(text, text_rect)
    

class Player():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 18)
    
    def increase_score(self, score:int):
        self.score += score

    def draw(self, win:pygame.Surface):
        text = self.font.render(f'Score: {str(self.score)}', True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.y = 20
        win.blit(text, text_rect)

    def whack(self, coords:tuple, digletts:list):
        x, y, *_ = coords
        for diglett in digletts:
            if diglett.hitbox[0] + diglett.hitbox[2] > x > diglett.hitbox[0] and diglett.hitbox[1] + diglett.hitbox[3] > y > diglett.hitbox[1]:
                # Diglett whacked
                digletts.remove(diglett)
                self.increase_score(10)

# General functions
def redraw_gamewindow(screen:pygame.Surface, digletts:list, player:Player, timer:Timer):
    screen.fill(bg)
    for diglett in digletts:
        if diglett.timer.time <= 0:
            digletts.remove(diglett)
        diglett.draw(screen)
    timer.draw(screen)
    player.draw(screen)
    pygame.display.update()


# Exported function
def run_game(screen:pygame.Surface):
    # Initial stuff
    clock = pygame.time.Clock()
    game_running = True
    
    # Variable initialization
    digletts = []
    frame_count = 0
    player = Player()
    timer = Timer(5)
    
    # Game Loop
    while game_running:
        clock.tick(FPS)
        
        # Check game ending
        frame_count += 1
        timer.count_down(frame_count)
        if timer.time == 0:
            game_running = False

        # Spawn Digletts
        if randint(1, FPS) == 1:
            digletts.append(Diglett(screen))
        for diglett in digletts:
            diglett.timer.count_down(frame_count)

        # Event handling
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    player.whack(pygame.mouse.get_pos(), digletts)
                # if e.button == 3:
                #     digletts.clear()
        
        # Reset frame count for good measure
        if frame_count == FPS:
            frame_count = 0
        redraw_gamewindow(screen, digletts, player, timer)
    run_hiscore(screen, player.score)
    
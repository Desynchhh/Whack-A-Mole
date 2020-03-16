import pygame
from random import randint
from os import path

# Framerate
FPS = 30

# Images
diglett_img = pygame.image.load(path.join('images', 'diglett.png'))

# Classes
class Diglett():
    def __init__(self, screen):
        self.x = randint(0, screen.get_width()-130)
        self.y = randint(0, screen.get_height()-130)
        self.hitbox = (self.x, self.y, 130, 130)
        self.timer = Timer(2)
    
    def draw(self, win:pygame.Surface):
        win.blit(diglett_img, (self.x, self.y))


class Timer():
    game_running = True
    def __init__(self, time:int):
        self.init_time = time
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.reset_timer()
    
    def manage_timer(self, frame_count:int):
        if frame_count % FPS == 0:
            self.time -= 1
            print(self.time)
            return 0
        if self.time == 0:
            Timer.game_running = False
        return frame_count

    def reset_timer(self):
        self.time = self.init_time
    
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
        x, y = coords
        for diglett in digletts:
            if x < diglett.hitbox[0]+diglett.hitbox[2] and x > diglett.hitbox[0]:
                if y > diglett.hitbox[1] and y < diglett.hitbox[1]+diglett.hitbox[3]:
                    # Diglett whacked
                    digletts.remove(diglett)
                    self.increase_score(10)

# General functions
def redraw_gamewindow(screen:pygame.Surface, bg:tuple, digletts:list, player:Player, timer:Timer):
    screen.fill(bg)
    for diglett in digletts:
        diglett.draw(screen)
        if diglett.timer.time <= 0:
            digletts.remove(diglett)
    timer.draw(screen)
    player.draw(screen)
    pygame.display.update()


# Exported function
def run_game(screen:pygame.Surface):
    # Initial stuff
    # pygame.init()
    clock = pygame.time.Clock()

    # Images
    bg = (0, 130, 0)
    
    # Variable initialization
    digletts = []
    frame_count = 0
    player = Player()
    timer = Timer(5)
    
    # Game Loop
    while Timer.game_running:
        clock.tick(FPS)
        frame_count += 1
        frame_count = timer.manage_timer(frame_count)

        if randint(1, FPS) == 1:
            digletts.append(Diglett(screen))

        # Event handling
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    player.whack(pygame.mouse.get_pos(), digletts)
                # if e.button == 3:
                #     digletts.clear()
        redraw_gamewindow(screen, bg, digletts, player, timer)
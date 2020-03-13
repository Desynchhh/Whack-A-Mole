import pygame
from random import randint
from os import path

pygame.init()
clock = pygame.time.Clock()
bg = (0, 130, 0)
diglett_img = pygame.image.load(path.join('images', 'diglett.png'))

screen_w = 500
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Whack-A-Diglett')

class Diglett():
    def __init__(self):
        self.x = randint(0, screen_w-130)
        self.y = randint(0, screen_h-130)
        self.hitbox = (self.x, self.y, 130, 130)
    
    def draw(self, win:pygame.Surface):
        win.blit(diglett_img, (self.x, self.y))
    
class Player():
    def __init__(self):
        self.score = 0
    
    def increase_score(self, score):
        self.score += score

def whack(coords:tuple, digletts:list):
    x, y = coords
    for diglett in digletts:
        if x < diglett.hitbox[0]+diglett.hitbox[2] and x > diglett.hitbox[0]:
            if y > diglett.hitbox[1] and y < diglett.hitbox[1]+diglett.hitbox[3]:
                # Diglett whacked
                digletts.remove(diglett)
                player.increase_score(10)


def redraw_gamewindow():
    screen.fill(bg)
    for diglett in digletts:
        diglett.draw(screen)
    pygame.display.update()

def spawn_diglett():
    new_diglett = Diglett()
    digletts.append(new_diglett)


digletts = []
player = Player()
game_running = True
while game_running:
    clock.tick(30)
    if randint(1, 30) == 1:
        spawn_diglett()
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game_running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                whack(pygame.mouse.get_pos(), digletts)
            if e.button == 3:
                digletts.clear()
    redraw_gamewindow()

print(player.score)
pygame.quit()

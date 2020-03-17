import pygame

from utils import Button
from game import run_game
from new_hiscore import run_hiscore # Temp



class Game():
    def __init__(self):
        pygame.init()
        self.screen_w = 500
        self.screen_h = 500
        self.screen = pygame.display.set_mode((self.screen_w, self.screen_h))
        pygame.display.set_caption('Whack-A-Diglett')
        self.bg = (255,255,255)
        self.running = True
        self.buttons = []

    def quit_game(self):
        pygame.quit()
        quit()

    def redraw_screen(self):
        self.screen.fill(self.bg)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    button_w = 100
    button_h = 50
    game.buttons.append(Button((game.screen_w-button_w)//2, (game.screen_h-button_h)//3, button_w, button_h, (200, 0, 0), (255,0,0), 'Play', run_game, game.screen))
    game.buttons.append(Button((game.screen_w-button_w)//2, (game.screen_h-button_h)//1.5, button_w, button_h, (200, 0, 0), (255,0,0), 'Quit', game.quit_game))
    # Temp
    game.buttons.append(Button((game.screen_w-button_w)//2, (game.screen_h-button_h)//2, button_w, button_h, (200, 0, 0), (255,0,0), 'Hiscores', run_hiscore, game.screen, 0))
    
    while game.running:
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    game.running = False
            
            for button in game.buttons:
                if button.hover_over() and pygame.mouse.get_pressed()[0]:
                    button.press()
            game.redraw_screen()

pygame.quit()

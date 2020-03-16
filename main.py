import pygame

from game import run_game

class Button():
    def __init__(self, x:int, y:int, w:int, h:int, color:tuple, highlight_color:tuple, text:str, action:object=None, *action_params):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.highlight_color = highlight_color
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', 22)
        self.action = action
        self.action_params = action_params

    def hover_over(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x + self.w > mouse_x > self.x and self.y + self.h > mouse_y > self.y

    def press(self):
        self.action(*self.action_params)

    def draw(self, screen:pygame.Surface):
        cur_color = self.color if self.hover_over() else self.highlight_color
        pygame.draw.rect(screen, cur_color, (self.x, self.y, self.w, self.h))
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        text = self.font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = ((self.x + self.w // 2), (self.y + self.h // 2))
        screen.blit(text, text_rect)


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
    game.buttons.append(Button((game.screen_w-button_w)//2, (game.screen_h-button_h)//2, button_w, button_h, (200, 0, 0), (255,0,0), 'Hiscores'))
    game.buttons.append(Button((game.screen_w-button_w)//2, (game.screen_h-button_h)//1.5, button_w, button_h, (200, 0, 0), (255,0,0), 'Quit', game.quit_game))
    
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

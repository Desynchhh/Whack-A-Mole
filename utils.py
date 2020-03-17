import pygame

class Interactable():
    def __init__(self, x:int, y:int, w:int, h:int, color:tuple, highlight_color:tuple, text:str):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.highlight_color = highlight_color
        self.text = text
        self.font = pygame.font.Font('freesansbold.ttf', 22)

    def hover_over(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.x + self.w > mouse_x > self.x and self.y + self.h > mouse_y > self.y

    def draw(self, screen:pygame.Surface):
        curr_color = self.color if self.hover_over() else self.highlight_color
        pygame.draw.rect(screen, curr_color, (self.x, self.y, self.w, self.h))
        text = self.font.render(self.text, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (self.x + self.w // 2, self.y + self.h // 2)
        screen.blit(text, text_rect)


class Button(Interactable):
    def __init__(self, x:int, y:int, w:int, h:int, color:tuple, highlight_color:tuple, text:str, action:object=None, *action_params):
        super().__init__(x, y, w, h, color, highlight_color, text)
        self.action = action
        self.action_params = action_params

    def press(self):
        if self.action != None:
            self.action(*self.action_params)

class Input_Field(Interactable):
    def __init__(self, x:int, y:int, w:int, h:int, color:tuple, highlight_color:tuple, text:str=''):
        super().__init__(x, y, w, h, color, highlight_color, text)
        self.active = False
    
    def update_text(self, event):
        if event.key == pygame.K_BACKSPACE:
            if len(self.text) > 0:
                self.text = self.text[:-1]
        elif len(self.text) < 3:
            self.text += event.unicode.upper()

    def draw(self, screen:pygame.Surface):
        if self.active:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))
            text = self.font.render(self.text, True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (self.x + self.w // 2, self.y + self.h // 2)
            screen.blit(text, text_rect)
        else:
            super().draw(screen)

class Text():
    def __init__(self, x:int, y:int, size:int, text:str, color:tuple=(0,0,0)):
        self.x = x
        self.y = y
        self.size = size
        self.text = text
        self.color = color

        self.font = pygame.font.Font('freesansbold.ttf', self.size)

    def draw(self, screen:pygame.Surface):
        text = self.font.render(self.text, True, self.color)
        text_rect = text.get_rect()
        text_rect.x = self.x
        text_rect.y = self.y
        screen.blit(text, text_rect)

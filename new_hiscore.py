import pygame

from utils import Button, Input_Field, Text

clock = pygame.time.Clock()


class Menu():
    def __init__(self, screen:pygame.Surface, score:int):
        self.running = True
        self.bg = (0,130,0)
        self.screen_w = screen.get_width()
        self.screen_h = screen.get_height()

        # Buttons
        self.btn_w = 120
        self.btn_h = 50
        self.btn_ds_x = (self.screen_w - self.btn_w) // 3.3
        self.btn_s_x = (self.screen_w - self.btn_w) // 1.4
        self.btn_y = (self.screen_h - self.btn_h) // 2
        self.btn_dont_save = Button(self.btn_ds_x, self.btn_y, self.btn_w, self.btn_h, (200, 0, 0), (255,0,0), "Don't Save", self.close_hiscore)
        self.btn_save = Button(self.btn_s_x, self.btn_y, self.btn_w, self.btn_h,(0,0,200),(0,0,255), 'Save', self.close_hiscore)
        self.buttons = (self.btn_dont_save, self.btn_save)

        # Input Field
        self.field_w = 150
        self.field_h = 50
        self.field_x = (self.screen_w - self.field_w) // 2
        self.field_y = (self.screen_h - self.field_h) // 3
        self.initials_field = Input_Field(self.field_x, self.field_y, self.field_w, self.field_h, (255,255,255), (200,200,200))

        # Score Text
        self.score = score
        self.score_text = Text(self.screen_w // 3, self.screen_h // 1.7, 22, f'Your score is {self.score}!')

        # Initials Text
        self.initials_text = Text(self.screen_w // 5, self.screen_h // 4.2, 18, 'Enter your initials to save your score')

        self.drawables = (self.btn_dont_save, self.btn_save, self.initials_field, self.score_text, self.initials_text)

    def redraw_screen(self, screen:pygame.Surface):
        screen.fill(self.bg)
        for drawable in self.drawables:
            drawable.draw(screen)
        pygame.display.update()

    def check_buttons_clicked(self):
        for button in self.buttons:
            if button.hover_over():
                button.press()


    def close_hiscore(self):
        self.running = False


def run_hiscore(screen:pygame.Surface, score:int):
    menu = Menu(screen, score)
    # Game Loop
    while menu.running:
        clock.tick(30)
        for event in pygame.event.get():
            # Quit game event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu.check_buttons_clicked()
                    menu.initials_field.active = menu.initials_field.hover_over()
            
            # Enter initials
            if menu.initials_field.active and event.type == pygame.KEYDOWN:
                menu.initials_field.update_text(event)

        menu.redraw_screen(screen)

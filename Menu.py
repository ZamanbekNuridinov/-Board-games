import pygame




pygame.init()

display_width = 1200
display_height = 800

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Collection Classqiue")

pygame.mixer.music.load('background.mp3')
pygame.mixer.music.set_volume(0.01)

button_sound = pygame.mixer.Sound('button.wav')

icon = pygame.image.load('icon2.png')
pygame.display.set_icon(icon)





class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (219, 176, 28)
        self.active_clr = (255, 207, 37)
        self.draw_effects = False
        self.clear_effects = False
        self.rect_h = 10
        self.rect_w = width

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:


            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        self.draw_beautiful_rect(mouse[0], mouse[1], x, y)
        print_text(message=message, x=x+10, y=y+10, font_size = font_size)

    def draw_beautiful_rect(self, ms_x, ms_y, x, y):
        if x <= ms_x <= x + self.width and y <= ms_y <= y + self.height:
            self.draw_effects = True

        if self.draw_effects:
            if ms_x < x or ms_x > x + self.width or ms_y < y or ms_y > y + self.height:
                self.clear_effects = True
                self.draw_effects = False

            if self.rect_h < self.height:
                self.rect_h += (self.height - 10) / 40

        if self.clear_effects and not self.draw_effects:
            if self.rect_h > 10:
                self.rect_h -= (self.height - 10) / 40
            else:
                self.clear_effects = False


        draw_y = y + self.height - self.rect_h
        pygame.draw.rect(display, self.active_clr, (x, draw_y, self.rect_w, self.rect_h))








usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 100

clock = pygame.time.Clock()





def show_menu():
    menu_background = pygame.image.load('Menu1.png')
    menu_background = pygame.transform.scale(menu_background, (1200, 800))

    show = True
                #height     #width
    start_btn = Button(288, 70)
    options_btn = Button(220, 70)
    credits_btn = Button(190, 70)
    quit_btn = Button(130, 70)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_background, (0, 0))
        start_btn.draw(460, 150, 'Start game', start_game, 50)
        options_btn.draw(490, 230, 'Options', None, 50)
        credits_btn.draw(510, 310, 'Credits', None, 50)
        quit_btn.draw(538, 390, 'Quit', quit, 50)
        pygame.display.update()
        clock.tick(60)

        pygame.display.update()
        clock.tick(80)

def start_game():
    game = True
    doska = pygame.image.load('Doska.jpg')
    grey = pygame.image.load('grey.png')
    start_btn = Button(130, 40)
    options_btn = Button(100, 40)
    settings_btn = Button(100, 40)
    quit_btn = Button(70, 40)
    pygame.mixer.music.play(-1)

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()



        clock.tick(80)

        # display.fill(221, 221, 221)




        display.blit(grey, (0, 0))
        display.blit(doska, (200, 50))

        start_btn.draw(30, 30, 'Start game', None, 20)
        options_btn.draw(40, 80, 'Options', None, 20)
        quit_btn.draw(60, 130, 'Quit', quit, 20)
        settings_btn.draw(800, 580, 'Settings', None, 20)
        print_text('Starting Position: ', 800, 100)





        pygame.display.update()
        clock.tick(80)

def credits():
    credits_backgroung = pygame.image.load()



font_color = (252, 252, 252)
def print_text(message, x, y, font_color = (0, 0, 0), font_type = 'DalekPinpointBold.ttf', font_size = 25):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Paused press enter to continue', 160, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)

    pygame.mixer.music.unpause()

show_menu()

while start_game():
    scores = 0
    make_jump = False
    jump_counter = 30
    usr_y = display_height - usr_height - 100
    health = 2


pygame.quit()
quit()



# def run_game():
#     game = True
#     land = pygame.image.load('Land.jpg')
#     pygame.mixer.music.play(-1,)
#     button = Button(110, 50)
#
#
#
#     while game:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             make_jump = True
#
#         if keys[pygame.K_ESCAPE]:
#             pause()
#
#         if make_jump:
#             jump()
#
#         display.blit(land, (0, 0))
#
#
#         button.draw(20, 100, 'wow')
#         draw_array(cactus_arr)
#         move_objects(stone, cloud)
#
#
#         pygame.display.update()
#         clock.tick(80)


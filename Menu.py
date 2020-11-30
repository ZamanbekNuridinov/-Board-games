import pygame
import chessEngine
import chessEngine1

pygame.init()

display_width = 1280
display_height = 800

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Collection Classqiue")

pygame.mixer.music.load('background1.mp3')
pygame.mixer.music.set_volume(0.05)

button_sound = pygame.mixer.Sound('button.wav')

icon = pygame.image.load('icon2.png')
pygame.display.set_icon(icon)

step_sound = pygame.mixer.Sound('chess.wav')
step_sound2 = pygame.mixer.Sound('chess2.wav')

bord = pygame.image.load('board4h.png')
bord= pygame.transform.scale(bord, (570,570))
nikandreos = pygame.image.load('nikandreos.png')
nikandreos= pygame.transform.scale(nikandreos, (400,200))
apollo = pygame.image.load('apollo.png')
apollo= pygame.transform.scale(apollo, (500,250))
artemis= pygame.image.load('artemis.png')
artemis= pygame.transform.scale(artemis, (450,250))






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

    def draw2(self, x, y, message, action=None, font_size=30):
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
        print_text3(message=message, x=x+10, y=y+10, font_size = font_size)

    def draw_beautiful_rect(self, ms_x, ms_y, x, y):
        if x <= ms_x <= x + self.width and y <= ms_y <= y + self.height:
            self.draw_effects = True

        if self.draw_effects:
            if ms_x < x or ms_x > x + self.width or ms_y < y or ms_y > y + self.height:
                self.clear_effects = True
                self.draw_effects = False

            if self.rect_h < self.height:
                self.rect_h += (self.height - 30) / 40

        if self.clear_effects and not self.draw_effects:
            if self.rect_h > 10:
                self.rect_h -= (self.height - 30) / 40
            else:
                self.clear_effects = False


        draw_y = y + self.height - self.rect_h
        pygame.draw.rect(display, self.active_clr, (x, draw_y, self.rect_w, self.rect_h))



clock = pygame.time.Clock()



def show_menu():

    menu_background2 = pygame.image.load('Menu2.jpg')
    pygame.mixer.music.load('background1.mp3')
    pygame.mixer.music.play(-1)

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
        display.blit(menu_background2, (-360, 0))
        start_btn.draw(485, 250, 'Start game', Select, 50)
        credits_btn.draw(530, 330, 'Credits', Creators, 50)
        quit_btn.draw(560, 410, 'Quit', quit, 50)

        pygame.display.update()
        clock.tick(80)
        
def Select():
    pygame.mixer.music.load('background1.mp3')
    pygame.mixer.music.play(-1)

    menu_background2 = pygame.image.load('screen1.jpg')
    

    Select = True

                #height     #width
    Ugolki_btn = Button(288, 70)
    Ugolki2_btn = Button(288, 70)
    Checkers_btn = Button(240, 70)
    Chess_btn = Button(160, 70)
    Chess2_btn = Button(280, 70)
    back_btn = Button(130, 70)
    quit_btn = Button(130, 70)

    while Select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_background2, (-215, -180))
        Ugolki_btn.draw2(485, 380, 'Ugolki 4x3', Ugolkki1, 50)
        Ugolki2_btn.draw2(485, 460, 'Ugolki 3x3', Ugolkki2, 50)
        Checkers_btn.draw2(510, 220, 'Checkers', Checkers ,50)
        Chess2_btn.draw2(495, 300, 'Chess 960', Chess960, 50)
        Chess_btn.draw2(550, 130, 'Chess', Chess, 50)
        back_btn.draw2(565, 510+30, 'Back', show_menu, 50)
        quit_btn.draw2(565, 590+30, 'Quit', quit, 50)

        # Ugolki_btn.draw2(485, 100+30, 'Ugolki 4x3', Ugolkki1, 50)
        # Ugolki2_btn.draw2(485, 190+30, 'Ugolki 3x3', Ugolkki2, 50)
        # Checkers_btn.draw2(510, 350+30, 'Checkers', Checkers ,50)
        # Chess2_btn.draw2(495, 270+30, 'Chess 960', Chess960, 50)
        # Chess_btn.draw2(550, 430+30, 'Chess', Chess, 50)
        # back_btn.draw2(565, 510+30, 'Back', show_menu, 50)
        # quit_btn.draw2(565, 590+30, 'Quit', quit, 50)

        pygame.display.update()
        clock.tick(80)


def Creators():

    Creators = True

    menu_background3 = pygame.image.load('ingame3.jpg')
    
                #height     #width
    text_btn = Button(0, 0)
    BACK_btn = Button(130, 70)
    

    while Creators:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_background3, (-450, -180))
        text_btn.draw2(360, 170, 'Was created by 3 gods', None, 50)
        text_btn.draw2(495, 250, 'Zamanbek', None, 50)
        text_btn.draw2(540, 330, 'Altair', None, 50)
        text_btn.draw2(495, 410, 'Kadyrgali', None ,50)
        BACK_btn.draw2(565, 490, 'BACK', show_menu, 50)
        

        pygame.display.update()
        clock.tick(80)

def Win():
    step_sound4 = pygame.mixer.music.load('WIN.mp3')
    pygame.mixer.music.play(1)

    menu_background3 = pygame.image.load('winimg.png')
    

    Win = True

                #height     #width
  
    text_btn = Button(0, 0)
    menu_btn= Button(155, 70)
    select_btn = Button(170, 70)
    quit_btn = Button(130, 70)

    while Win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_background3, (-215, -180))
        text_btn.draw(450, 170, 'Congratulations', None, 50)
        text_btn.draw(360, 250, 'you received a blessing', None ,50)
        text_btn.draw(450, 330, 'from three gods', None, 50)
        select_btn.draw(570, 410, 'Select', Select, 50)
        menu_btn.draw(575, 490, 'MENU', show_menu, 50)
        quit_btn.draw(585, 570, 'Quit', quit, 50)

        pygame.display.update()
        clock.tick(80)

def Ugolkki1():
    game = True
    newGame=True
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    greyBackground=(203, 206, 203)
    orange=(255, 128, 0)
    yellow=(255, 255, 0)
    grey=(133, 133, 133)
    navy=(0, 0, 128)


    width=65
    height=65
    radius=30
    king_black = pygame.image.load('black222.png')
    king_black= pygame.transform.scale(king_black, (width+35,height+35))
    king_red = pygame.image.load('red.png')
    king_red= pygame.transform.scale(king_red, (width+30,height+30))


    margin=0
    xDistanceFromEdge=240
    yDistanceFromEdge=140
    gameBoard=[[None]*8 for _ in range(8)]  
    done = False
    clock = pygame.time.Clock()

   
    BBB = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[0,1,0],[1,1,0],[2,1,0],[3,1,0],[0,2,0],[1,2,0],[2,2,0],[3,2,0]]
    RRR = [[4,5,0],[5,5,0],[6,5,0],[7,5,0],[4,6,0],[5,6,0],[6,6,0],[7,6,0],[4,7,0],[5,7,0],[6,7,0],[7,7,0]]
    ENDBBB = [[4,5],[5,5],[6,5],[7,5],[4,6],[5,6],[6,6],[7,6],[4,7],[5,7],[6,7],[7,7]]
    ENDRRR = [[0,0],[1,0],[2,0],[3,0],[0,1],[1,1],[2,1],[3,1],[0,2],[1,2],[2,2],[3,2]]

    TTT = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[0,1,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0],[0,2,0],[1,2,0],[2,2,0],[3,2,0],[4,2,0],[5,2,0],[6,2,0],[7,2,0],[0,3,0],[1,3,0],[2,3,0],[3,3,0],[4,3,0],[5,3,0],[6,3,0],[7,3,0],[0,4,0],[1,4,0],[2,4,0],[3,4,0],[4,4,0],[5,4,0],[6,4,0],[7,4,0],[0,5,0],[1,5,0],[2,5,0],[3,5,0],[4,5,0],[5,5,0],[6,5,0],[7,5,0],[0,6,0],[1,6,0],[2,6,0],[3,6,0],[4,6,0],[5,6,0],[6,6,0],[7,6,0],[0,7,0],[1,7,0],[2,7,0],[3,7,0],[4,7,0],[5,7,0],[6,7,0],[7,7,0]]


    #цвет полей
    def square_colour(row, col,colorof1):
        if colorof1==1:
            return yellow
        elif colorof1==2:
            return orange
        # elif colorof1==0:
        #     if (row + col) % 2 == 0:
        #         return white 
        #     else:
        #         return black  
    #Доска
    def boardGui(black,white,yellow):
        for gg in range(len(TTT)):
            boardColumn=TTT[gg][0]
            boardRow=TTT[gg][1]
            Colorof1=TTT[gg][2]
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=((margin+height) * boardRow + margin)+yDistanceFromEdge
            if Colorof1==1 or Colorof1==2:
                currentColour = square_colour(boardRow, boardColumn,Colorof1)
                pygame.draw.rect(display,currentColour,[xCoordinate,yCoordinate, width, height])
            


    def piecesGameBoard(gameBoard):
        if newGame:
            newGameBoard(gameBoard)
    #Шашки

    def newGameBoard(gameBoard):
        # Empty the game board.
        gameBoard[:] = [[None]*8 for _ in range(8)]
        
        for i in range(len(BBB)):
            ShaskaB = BBB[i]
            gameBoard[ShaskaB[0]][ShaskaB[1]]="NormalBlack"
                            
                            
                
        for i in range(len(RRR)):
            ShaskaR = RRR[i]
            gameBoard[ShaskaR[0]][ShaskaR[1]]="NormalRed"
                        
        drawPieces(gameBoard,black,red)
        
    #Скин
    def drawPieces(gameBoard,black,red):
        for x in range(8):
            for y in range(8):
                xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
                yCoordinate=((margin+height) * y + margin+33)+yDistanceFromEdge
            
                if gameBoard[x][y]=="NormalBlack":
                    # pygame.draw.circle(display,grey,(xCoordinate,yCoordinate),radius) 
                    display.blit(king_black, (xCoordinate-50,yCoordinate-50))


                if gameBoard[x][y]=="NormalRed":
                    # pygame.draw.circle(display,red,(xCoordinate,yCoordinate),radius)
                    #pygame.draw.circle(display,white,(xCoordinate,yCoordinate),radius, 1)
                    display.blit(king_red, (xCoordinate-49,yCoordinate-49))
                    
                    
        

    # -------- Main Program Loop -----------
    start=0
    BWIN=0
    RWIN=0
    player2 = True
    player1 = False
    WWIN=0
    #print("Player2 turn")
    # doska = pygame.image.load('board.png')
    # doska = pygame.transform.scale(doska, (512, 512))

    ingame = pygame.image.load('ingame2l.png')
    ingame = pygame.transform.scale(ingame, (1280, 800))
    start_btn = Button(83, 40)


    rules_btn = Button(100, 40)
    back_btn = Button(70, 40)
    quit_btn = Button(70, 40)
    Music_btn = Button(110, 40)
    Music2_btn = Button(110, 40)
 

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and start==0 and player1 == True:
            
                ##print("player1")
                ##print(player1)
            # #print("player2")
            # #print(player2)
                pos = pygame.mouse.get_pos()
                #print(pos)

                # Change the x/y display coordinates to grid coordinates
                column = (pos[0]-xDistanceFromEdge) // (width+margin)
                row = (pos[1]-yDistanceFromEdge) // (height+margin)
                #print(column)
                #print(row)
                for i in range(len(BBB)):
                    ShaskaB = BBB[i]
                    if column==ShaskaB[0] and row==ShaskaB[1]:
                        #print("Player1 chosed")  
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            if Total[0]==column and Total[1]==row:
                                Total[2]=1
                            elif Total[0]==column+1 and Total[1]==row and gameBoard[column+1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-1 and gameBoard[column][row-1]==None:
                                Total[2]=2
                            elif Total[0]==column-1 and Total[1]==row and gameBoard[column-1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+1 and gameBoard[column][row+1]==None:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row and gameBoard[column+2][row]==None and (gameBoard[column+1][row]=="NormalRed" or gameBoard[column+1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row and gameBoard[column-2][row]==None and (gameBoard[column-1][row]=="NormalRed" or gameBoard[column-1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+2 and gameBoard[column][row+2]==None and (gameBoard[column][row+1]=="NormalRed" or gameBoard[column][row+1]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-2 and gameBoard[column][row-2]==None and (gameBoard[column][row-1]=="NormalRed" or gameBoard[column][row-1]=="NormalBlack"):
                                Total[2]=2
                        
                        pygame.mixer.Sound.play(step_sound)
                        start=1


            elif event.type == pygame.MOUSEBUTTONDOWN and start==0 and player2 == True:
                ##print("player1")
                ##print(player1)
                ##print("player2")
            # #print(player2)
                
                pos = pygame.mouse.get_pos()
                ##print(pos)

                # Change the x/y display coordinates to grid coordinates
                column = (pos[0]-xDistanceFromEdge) // (width+margin)
                row = (pos[1]-yDistanceFromEdge) // (height+margin)
                ##print(column)
                ##print(row)
                for i in range(len(RRR)):
                    ShaskaR = RRR[i]
                    if column==ShaskaR[0] and row==ShaskaR[1]:
                        #print("Player2 chosed")
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            if Total[0]==column and Total[1]==row:
                                Total[2]=1
                            elif Total[0]==column+1 and Total[1]==row and gameBoard[column+1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-1 and gameBoard[column][row-1]==None:
                                Total[2]=2
                            elif Total[0]==column-1 and Total[1]==row and gameBoard[column-1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+1 and gameBoard[column][row+1]==None:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row and gameBoard[column+2][row]==None and (gameBoard[column+1][row]=="NormalRed" or gameBoard[column+1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row and gameBoard[column-2][row]==None and (gameBoard[column-1][row]=="NormalRed" or gameBoard[column-1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+2 and gameBoard[column][row+2]==None and (gameBoard[column][row+1]=="NormalRed" or gameBoard[column][row+1]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-2 and gameBoard[column][row-2]==None and (gameBoard[column][row-1]=="NormalRed" or gameBoard[column][row-1]=="NormalBlack"):
                                Total[2]=2
                        
                        pygame.mixer.Sound.play(step_sound)
                        start=1
                        

            elif event.type == pygame.MOUSEBUTTONDOWN and start==1:
                poss = pygame.mouse.get_pos()
                ##print(poss)

                columnn = (poss[0]-xDistanceFromEdge) // (width+margin)
                roww = (poss[1]-yDistanceFromEdge) // (height+margin)
                ##print(columnn)
                ##print(roww)
    #1 игрок
                if player1==True:
                #1 игрок простой ход
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    if (columnn == column+1 and roww == row) or (columnn == column-1 and roww== row):
                        #print("alta")
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player1=False
                                    player2=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                #elif gameBoard[columnn][roww]=="NormalRed" and gameBoard[columnn][roww]=="NormalRed":
                                    ##print("eat")
                                else:
                                    #print("You con not go like that!!!")
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)

                    elif (columnn == column and roww == row+1) or (columnn == column and roww== row-1):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player1=False
                                    player2=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                #elif gameBoard[columnn][roww]=="NormalRed" and gameBoard[columnn][roww]=="NormalRed":
                                    ##print("eat")
                                else:
                                    #print("You con not go like that!!!")
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                    #1 игрок ход 
                    elif (columnn == column+2 and roww == row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                    
                            if column==ShaskaB[0] and row==ShaskaB[1]: 
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                            
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                                


                    elif (columnn == column-2 and roww== row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:   
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                    

                    elif (columnn == column and roww == row+2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                            
                    elif (columnn == column and roww== row -2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalRed") :
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                    

                    else:
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            Total[2]=0
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
    #2 игрок
                elif player2==True:
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    #2 игрок простой ход
                    if (columnn == column+1 and roww == row) or (columnn == column-1 and roww== row):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player2=False
                                    player1=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0


                                else:
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                    elif (columnn == column and roww == row+1) or (columnn == column and roww== row-1):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player2=False
                                    player1=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0


                                else:
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)

                    #2 игрок ход
                    elif (columnn == column+2 and roww == row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2

                            

                    elif (columnn == column-2 and roww== row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2


                    elif (columnn == column and roww == row+2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:   
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2


                            
                    
                    elif (columnn == column and roww== row -2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:   
                                ##print(gameBoard[columnn][roww])
                                start=0
                        
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2



                    else:
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            Total[2]=0
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and start==2: 
                
                pos = pygame.mouse.get_pos()
                ##print(pos)

                # Change the x/y display coordinates to grid coordinates
                columnnn = (pos[0]-xDistanceFromEdge) // (width+margin)
                rowww = (pos[1]-yDistanceFromEdge) // (height+margin)
                ##print(" ")
                ##print(pos_column)
                ##print(pos_row)
                ##print(columnnn)
                ##print(rowww)
                ##print(" ")
                if player1==True:
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    if (columnnn == pos_column+2 and rowww == pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed") or gameBoard[columnnn-1][rowww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:    
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2

                                


                    elif (columnnn == pos_column-2 and rowww== pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed") or gameBoard[columnnn+1][rowww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]: 
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2

                    elif (columnnn == pos_column and rowww == pos_row-2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww+1]=="NormalRed") or gameBoard[columnnn][rowww+1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                            
                    elif (columnnn == pos_column and rowww== pos_row +2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww-1]=="NormalRed") or gameBoard[columnnn][rowww-1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                

                    else:
                        ##print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                        player1=False
                        player2=True
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                





                elif player2==True: 
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    if (columnnn == pos_column+2 and rowww == pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed") or gameBoard[columnnn-1][rowww]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:    
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                            
                            

                    elif (columnnn == pos_column-2 and rowww== pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed") or gameBoard[columnnn+1][rowww]=="NormalBlack")): 
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:     
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2


                    elif (columnnn == pos_column and rowww == pos_row+2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww-1]=="NormalRed") or gameBoard[columnnn][rowww-1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalBlack") :
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2

                            
                    
                    elif (columnnn == pos_column and rowww== pos_row -2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww+1]=="NormalRed") or gameBoard[columnnn][rowww+1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                        
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
    
                    else:
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                        player2=False
                        player1=True
                        start=0 
                        pygame.mixer.Sound.play(step_sound2)
            

        for i in range(len(BBB)):
            ShaskaB = BBB[i]
            for j in range(len(ENDBBB)):
                ShaskaENDB = ENDBBB[j]
                if ShaskaB[0] == ShaskaENDB[0] and ShaskaB[1] == ShaskaENDB[1]:
                    ShaskaB[2]=1
                    break
                else:
                    ShaskaB[2]=0
        for i in range(len(RRR)):
            ShaskaR = RRR[i]
            for j in range(len(ENDRRR)):
                ShaskaENDR = ENDRRR[j]
                if ShaskaR[0] == ShaskaENDR[0] and ShaskaR[1] == ShaskaENDR[1]:
                    ShaskaR[2]=1
                    break
                else:
                    ShaskaR[2]=0
        if WWIN==0:
            for i in range(len(BBB)):
                ShaskaB = BBB[i]
                if ShaskaB[2] == 1:
                    BWIN+=1
            for i in range(len(RRR)):
                ShaskaR = RRR[i]
                if ShaskaR[2] == 1:
                    RWIN+=1
            if BWIN==12:
                #print("1 Player win")
                WWIN=1
                Win()
            
            else:
                BWIN=0
            if RWIN==12:
                #print("2 Player win")
                WWIN=1
                Win()
            else:
                RWIN=0
        display.blit(ingame, (0, 0))
        start_btn.draw(95, 90, 'Select', Select, 20)
        back_btn.draw(100, 140, 'Menu', show_menu, 20)
        Music_btn.draw(xDistanceFromEdge*4+130, yDistanceFromEdge*4-66, 'Music off', Music2, 20)
        Music2_btn.draw(xDistanceFromEdge*4-80, yDistanceFromEdge*4-66, 'Music on', Music, 20)
        quit_btn.draw(100, 190, 'Quit', quit, 20)
        header = pygame.image.load('header-title1.png')
        header= pygame.transform.scale(header, (400,200))
        display.blit(header, (xDistanceFromEdge*3+80, yDistanceFromEdge-70))
        if player1==True:
            print_text('player2 turn', xDistanceFromEdge*3+210, yDistanceFromEdge+70)
        elif player2==True:
            print_text('player1 turn' , xDistanceFromEdge*3+210, yDistanceFromEdge+70)
        


        display.blit(bord, (xDistanceFromEdge-26, yDistanceFromEdge-26))
   
        display.blit(nikandreos, (xDistanceFromEdge-300, yDistanceFromEdge*4-10)) 

        display.blit(apollo, (xDistanceFromEdge*4-300, yDistanceFromEdge*4-55))

        display.blit(artemis, (xDistanceFromEdge*4-80, yDistanceFromEdge*4-55))

        #Доска
        boardGui(black,white,yellow)
        #Шашки
        piecesGameBoard(gameBoard)

    

        clock.tick(60)
        pygame.display.flip()







        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()

def Ugolkki2():
    game = True
    newGame=True
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    greyBackground=(203, 206, 203)
    yellow=(255, 255, 0)
    grey=(133, 133, 133)
    orange=(255, 128, 0)
    navy=(0, 0, 128)


    width=65
    height=65
    radius=30
    king_black = pygame.image.load('black222.png')
    king_black= pygame.transform.scale(king_black, (width+35,height+35))
    king_red = pygame.image.load('red.png')
    king_red= pygame.transform.scale(king_red, (width+30,height+30))

    margin=0
    xDistanceFromEdge=240
    yDistanceFromEdge=140
    gameBoard=[[None]*8 for _ in range(8)]  
    done = False
    clock = pygame.time.Clock()

   
    BBB = [[0,0,0],[1,0,0],[2,0,0],[0,1,0],[1,1,0],[2,1,0],[0,2,0],[1,2,0],[2,2,0]]
    RRR = [[5,5,0],[6,5,0],[7,5,0],[5,6,0],[6,6,0],[7,6,0],[5,7,0],[6,7,0],[7,7,0]]

    ENDBBB = [[5,5],[6,5],[7,5],[5,6],[6,6],[7,6],[5,7],[6,7],[7,7]]
    ENDRRR = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]]

    TTT = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[0,1,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0],[0,2,0],[1,2,0],[2,2,0],[3,2,0],[4,2,0],[5,2,0],[6,2,0],[7,2,0],[0,3,0],[1,3,0],[2,3,0],[3,3,0],[4,3,0],[5,3,0],[6,3,0],[7,3,0],[0,4,0],[1,4,0],[2,4,0],[3,4,0],[4,4,0],[5,4,0],[6,4,0],[7,4,0],[0,5,0],[1,5,0],[2,5,0],[3,5,0],[4,5,0],[5,5,0],[6,5,0],[7,5,0],[0,6,0],[1,6,0],[2,6,0],[3,6,0],[4,6,0],[5,6,0],[6,6,0],[7,6,0],[0,7,0],[1,7,0],[2,7,0],[3,7,0],[4,7,0],[5,7,0],[6,7,0],[7,7,0]]


    #цвет полей
    def square_colour(row, col,colorof1):
        if colorof1==1:
            return yellow
        elif colorof1==2:
            return orange
        # elif colorof1==0:
        #     if (row + col) % 2 == 0:
        #         return white 
        #     else:
        #         return black  
    #Доска
    def boardGui(black,white,yellow):
        for gg in range(len(TTT)):
            boardColumn=TTT[gg][0]
            boardRow=TTT[gg][1]
            Colorof1=TTT[gg][2]
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=((margin+height) * boardRow + margin)+yDistanceFromEdge
            if Colorof1==1 or Colorof1==2:
                currentColour = square_colour(boardRow, boardColumn,Colorof1)
                pygame.draw.rect(display,currentColour,[xCoordinate,yCoordinate, width, height])
            


    def piecesGameBoard(gameBoard):
        if newGame:
            newGameBoard(gameBoard)
    #Шашки

    def newGameBoard(gameBoard):
        # Empty the game board.
        gameBoard[:] = [[None]*8 for _ in range(8)]
        
        for i in range(len(BBB)):
            ShaskaB = BBB[i]
            gameBoard[ShaskaB[0]][ShaskaB[1]]="NormalBlack"
                            
                            
                
        for i in range(len(RRR)):
            ShaskaR = RRR[i]
            gameBoard[ShaskaR[0]][ShaskaR[1]]="NormalRed"
                        
        drawPieces(gameBoard,black,red)
        
    #Скин
    def drawPieces(gameBoard,black,red):
        for x in range(8):
            for y in range(8):
                xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
                yCoordinate=((margin+height) * y + margin+33)+yDistanceFromEdge
            
                if gameBoard[x][y]=="NormalBlack":
                    # pygame.draw.circle(display,grey,(xCoordinate,yCoordinate),radius)
                    display.blit(king_black, (xCoordinate-50,yCoordinate-50))
 

                if gameBoard[x][y]=="NormalRed":
                    # pygame.draw.circle(display,red,(xCoordinate,yCoordinate),radius)
                    #pygame.draw.circle(display,white,(xCoordinate,yCoordinate),radius, 1)
                    display.blit(king_red, (xCoordinate-49,yCoordinate-49))
                    
                    
        

    # -------- Main Program Loop -----------
    start=0
    BWIN=0
    RWIN=0
    player2 = True
    player1 = False
    WWIN=0
    #print("Player2 turn")
    # doska = pygame.image.load('board.png')
    # doska = pygame.transform.scale(doska, (512, 512))

    ingame = pygame.image.load('ingame2l.png')
    ingame = pygame.transform.scale(ingame, (1280, 800))
    start_btn = Button(83, 40)
    back_btn = Button(70, 40)
    quit_btn = Button(70, 40)
    

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and start==0 and player1 == True:
            
                ##print("player1")
                ##print(player1)
            # #print("player2")
            # #print(player2)
                pos = pygame.mouse.get_pos()
                #print(pos)

                # Change the x/y display coordinates to grid coordinates
                column = (pos[0]-xDistanceFromEdge) // (width+margin)
                row = (pos[1]-yDistanceFromEdge) // (height+margin)
                #print(column)
                #print(row)
                for i in range(len(BBB)):
                    ShaskaB = BBB[i]
                    if column==ShaskaB[0] and row==ShaskaB[1]:
                        #print("Player1 chosed")  
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            if Total[0]==column and Total[1]==row:
                                Total[2]=1
                            elif Total[0]==column+1 and Total[1]==row and gameBoard[column+1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-1 and gameBoard[column][row-1]==None:
                                Total[2]=2
                            elif Total[0]==column-1 and Total[1]==row and gameBoard[column-1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+1 and gameBoard[column][row+1]==None:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row and gameBoard[column+2][row]==None and (gameBoard[column+1][row]=="NormalRed" or gameBoard[column+1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row and gameBoard[column-2][row]==None and (gameBoard[column-1][row]=="NormalRed" or gameBoard[column-1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+2 and gameBoard[column][row+2]==None and (gameBoard[column][row+1]=="NormalRed" or gameBoard[column][row+1]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-2 and gameBoard[column][row-2]==None and (gameBoard[column][row-1]=="NormalRed" or gameBoard[column][row-1]=="NormalBlack"):
                                Total[2]=2
                       
                        pygame.mixer.Sound.play(step_sound)
                        start=1


            elif event.type == pygame.MOUSEBUTTONDOWN and start==0 and player2 == True:
                ##print("player1")
                ##print(player1)
                ##print("player2")
            # #print(player2)
                
                pos = pygame.mouse.get_pos()
                ##print(pos)

                # Change the x/y display coordinates to grid coordinates
                column = (pos[0]-xDistanceFromEdge) // (width+margin)
                row = (pos[1]-yDistanceFromEdge) // (height+margin)
                ##print(column)
                ##print(row)
                for i in range(len(RRR)):
                    ShaskaR = RRR[i]
                    if column==ShaskaR[0] and row==ShaskaR[1]:
                        #print("Player2 chosed")
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            if Total[0]==column and Total[1]==row:
                                Total[2]=1
                            elif Total[0]==column+1 and Total[1]==row and gameBoard[column+1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-1 and gameBoard[column][row-1]==None:
                                Total[2]=2
                            elif Total[0]==column-1 and Total[1]==row and gameBoard[column-1][row]==None:
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+1 and gameBoard[column][row+1]==None:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row and gameBoard[column+2][row]==None and (gameBoard[column+1][row]=="NormalRed" or gameBoard[column+1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row and gameBoard[column-2][row]==None and (gameBoard[column-1][row]=="NormalRed" or gameBoard[column-1][row]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row+2 and gameBoard[column][row+2]==None and (gameBoard[column][row+1]=="NormalRed" or gameBoard[column][row+1]=="NormalBlack"):
                                Total[2]=2
                            elif Total[0]==column and Total[1]==row-2 and gameBoard[column][row-2]==None and (gameBoard[column][row-1]=="NormalRed" or gameBoard[column][row-1]=="NormalBlack"):
                                Total[2]=2
                        
                        pygame.mixer.Sound.play(step_sound)
                        start=1
                        

            elif event.type == pygame.MOUSEBUTTONDOWN and start==1:
                poss = pygame.mouse.get_pos()
                ##print(poss)

                columnn = (poss[0]-xDistanceFromEdge) // (width+margin)
                roww = (poss[1]-yDistanceFromEdge) // (height+margin)
                ##print(columnn)
                ##print(roww)
    #1 игрок
                if player1==True:
                #1 игрок простой ход
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    if (columnn == column+1 and roww == row) or (columnn == column-1 and roww== row):
                        #print("alta")
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player1=False
                                    player2=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                #elif gameBoard[columnn][roww]=="NormalRed" and gameBoard[columnn][roww]=="NormalRed":
                                    ##print("eat")
                                else:
                                    #print("You con not go like that!!!")
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)

                    elif (columnn == column and roww == row+1) or (columnn == column and roww== row-1):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player1=False
                                    player2=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                #elif gameBoard[columnn][roww]=="NormalRed" and gameBoard[columnn][roww]=="NormalRed":
                                    ##print("eat")
                                else:
                                    #print("You con not go like that!!!")
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                    #1 игрок ход 
                    elif (columnn == column+2 and roww == row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                    
                            if column==ShaskaB[0] and row==ShaskaB[1]: 
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                            
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                                


                    elif (columnn == column-2 and roww== row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:   
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                
                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                    

                    elif (columnn == column and roww == row+2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                            
                    elif (columnn == column and roww== row -2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalRed") :
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalBlack"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                    

                    else:
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            Total[2]=0
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
    #2 игрок
                elif player2==True:
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    #2 игрок простой ход
                    if (columnn == column+1 and roww == row) or (columnn == column-1 and roww== row):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player2=False
                                    player1=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0


                                else:
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                    elif (columnn == column and roww == row+1) or (columnn == column and roww== row-1):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player2=False
                                    player1=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0


                                else:
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)

                    #2 игрок ход
                    elif (columnn == column+2 and roww == row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2

                            

                    elif (columnn == column-2 and roww== row) and (gameBoard[columnn][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2


                    elif (columnn == column and roww == row+2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:   
                                ##print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww-1]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2


                            
                    
                    elif (columnn == column and roww== row -2) and (gameBoard[columnn][roww]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:   
                                ##print(gameBoard[columnn][roww])
                                start=0
                        
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnn][roww]==None and gameBoard[columnn][roww+1]=="NormalRed"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww and gameBoard[columnn+2][roww]==None and (gameBoard[columnn+1][roww]=="NormalRed" or gameBoard[columnn+1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww and gameBoard[columnn-2][roww]==None and (gameBoard[columnn-1][roww]=="NormalRed" or gameBoard[columnn-1][roww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww+2 and gameBoard[columnn][roww+2]==None and (gameBoard[columnn][roww+1]=="NormalRed" or gameBoard[columnn][roww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn and Total[1]==roww-2 and gameBoard[columnn][roww-2]==None and (gameBoard[columnn][roww-1]=="NormalRed" or gameBoard[columnn][roww-1]=="NormalBlack"):
                                            Total[2]=2



                    else:
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            Total[2]=0
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and start==2: 
                
                pos = pygame.mouse.get_pos()
                ##print(pos)

                # Change the x/y display coordinates to grid coordinates
                columnnn = (pos[0]-xDistanceFromEdge) // (width+margin)
                rowww = (pos[1]-yDistanceFromEdge) // (height+margin)
                ##print(" ")
                ##print(pos_column)
                ##print(pos_row)
                ##print(columnnn)
                ##print(rowww)
                ##print(" ")
                if player1==True:
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    if (columnnn == pos_column+2 and rowww == pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed") or gameBoard[columnnn-1][rowww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:    
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2

                                


                    elif (columnnn == pos_column-2 and rowww== pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed") or gameBoard[columnnn+1][rowww]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]: 
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2

                    elif (columnnn == pos_column and rowww == pos_row-2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww+1]=="NormalRed") or gameBoard[columnnn][rowww+1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                
                            
                    elif (columnnn == pos_column and rowww== pos_row +2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww-1]=="NormalRed") or gameBoard[columnnn][rowww-1]=="NormalBlack")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww                         
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                

                    else:
                        ##print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                        player1=False
                        player2=True
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                





                elif player2==True: 
                    ##print("player1")
                    ##print(player1)
                    ##print("player2")
                    ##print(player2)
                    if (columnnn == pos_column+2 and rowww == pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed") or gameBoard[columnnn-1][rowww]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:    
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                            
                            

                    elif (columnnn == pos_column-2 and rowww== pos_row) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed") or gameBoard[columnnn+1][rowww]=="NormalBlack")): 
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:     
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2


                    elif (columnnn == pos_column and rowww == pos_row+2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww-1]=="NormalRed") or gameBoard[columnnn][rowww-1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalBlack") :
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww-1]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2

                            
                    
                    elif (columnnn == pos_column and rowww== pos_row -2) and ((gameBoard[columnnn][rowww]==None and (gameBoard[columnnn][rowww+1]=="NormalRed") or gameBoard[columnnn][rowww+1]=="NormalBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:   
                                ##print(gameBoard[columnnn][rowww])
                                start=0
                        
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
                                elif (gameBoard[columnnn][rowww]==None and gameBoard[columnnn][rowww+1]=="NormalRed"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww                            
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==pos_column and Total[1]==pos_row:
                                            Total[2]=1
                                        elif Total[0]==columnnn+2 and Total[1]==rowww and gameBoard[columnnn+2][rowww]==None and (gameBoard[columnnn+1][rowww]=="NormalRed" or gameBoard[columnnn+1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn-2 and Total[1]==rowww and gameBoard[columnnn-2][rowww]==None and (gameBoard[columnnn-1][rowww]=="NormalRed" or gameBoard[columnnn-1][rowww]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww+2 and gameBoard[columnnn][rowww+2]==None and (gameBoard[columnnn][rowww+1]=="NormalRed" or gameBoard[columnnn][rowww+1]=="NormalBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnnn and Total[1]==rowww-2 and gameBoard[columnnn][rowww-2]==None and (gameBoard[columnnn][rowww-1]=="NormalRed" or gameBoard[columnnn][rowww-1]=="NormalBlack"):
                                            Total[2]=2
    
                    else:
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                        player2=False
                        player1=True
                        start=0 
                        pygame.mixer.Sound.play(step_sound2)
            

        for i in range(len(BBB)):
            ShaskaB = BBB[i]
            for j in range(len(ENDBBB)):
                ShaskaENDB = ENDBBB[j]
                if ShaskaB[0] == ShaskaENDB[0] and ShaskaB[1] == ShaskaENDB[1]:
                    ShaskaB[2]=1
                    break
                else:
                    ShaskaB[2]=0
        for i in range(len(RRR)):
            ShaskaR = RRR[i]
            for j in range(len(ENDRRR)):
                ShaskaENDR = ENDRRR[j]
                if ShaskaR[0] == ShaskaENDR[0] and ShaskaR[1] == ShaskaENDR[1]:
                    ShaskaR[2]=1
                    break
                else:
                    ShaskaR[2]=0
        if WWIN==0:
            for i in range(len(BBB)):
                ShaskaB = BBB[i]
                if ShaskaB[2] == 1:
                    BWIN+=1
            for i in range(len(RRR)):
                ShaskaR = RRR[i]
                if ShaskaR[2] == 1:
                    RWIN+=1
            if BWIN==12:
                #print("1 Player win")
                WWIN=1
                Win()
            
            else:
                BWIN=0
            if RWIN==12:
                #print("2 Player win")
                WWIN=1
                Win()
            else:
                RWIN=0
        display.blit(ingame, (0, 0))
        start_btn.draw(95, 90, 'Select', Select, 20)
        back_btn.draw(100, 140, 'Menu', show_menu, 20)
        quit_btn.draw(100, 190, 'Quit', quit, 20)
        header = pygame.image.load('header-title1.png')
        header= pygame.transform.scale(header, (400,200))
        display.blit(header, (xDistanceFromEdge*3+80, yDistanceFromEdge-70))
        Music_btn = Button(110, 40)
        Music2_btn = Button(110, 40)
        Music_btn.draw(xDistanceFromEdge*4+130, yDistanceFromEdge*4-66, 'Music off', Music2, 20)
        Music2_btn.draw(xDistanceFromEdge*4-80, yDistanceFromEdge*4-66, 'Music on', Music, 20)
        if player1==True:
            print_text('player2 turn', xDistanceFromEdge*3+210, yDistanceFromEdge+70)
        elif player2==True:
            print_text('player1 turn' , xDistanceFromEdge*3+210, yDistanceFromEdge+70)
                  
      
        display.blit(bord, (xDistanceFromEdge-26, yDistanceFromEdge-26))
   
        display.blit(nikandreos, (xDistanceFromEdge-300, yDistanceFromEdge*4-10)) 

        display.blit(apollo, (xDistanceFromEdge*4-300, yDistanceFromEdge*4-55))

        display.blit(artemis, (xDistanceFromEdge*4-80, yDistanceFromEdge*4-55))

        #Доска
        boardGui(black,white,yellow)
        #Шашки
        piecesGameBoard(gameBoard)


        clock.tick(60)
        pygame.display.flip()







        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()



        # display.fill(221, 221, 221)

def Checkers():
    game = True
    newGame=True
    black=(0,0,0)
    white=(255,255,255)
    red=(255,0,0)
    greyBackground=(203, 206, 203)
    yellow=(255, 255, 0)
    grey=(133, 133, 133)
    orange=(255, 128, 0)
    navy=(0, 0, 128)


    width=65
    height=65
    radius=30
    king_black = pygame.image.load('black222.png')
    king_black= pygame.transform.scale(king_black, (width+35,height+35))
    king_red = pygame.image.load('red.png')
    king_red= pygame.transform.scale(king_red, (width+30,height+30))
    black = pygame.image.load('blackall.png')
    black= pygame.transform.scale(black, (width+35,height+35))
    red = pygame.image.load('images122.png')
    red= pygame.transform.scale(red, (width+30,height+30))

    margin=0
    xDistanceFromEdge=240
    yDistanceFromEdge=140
    gameBoard=[[None]*8 for _ in range(8)]  
    done = False
    clock = pygame.time.Clock()

    BBB = [[1,0,0],[3,0,0],[5,0,0],[7,0,0],[0,1,0],[2,1,0],[4,1,0],[6,1,0],[1,2,0],[3,2,0],[5,2,0],[7,2,0]]
    RRR = [[0,5,0],[2,5,0],[4,5,0],[6,5,0],[1,6,0],[3,6,0],[5,6,0],[7,6,0],[0,7,0],[2,7,0],[4,7,0],[6,7,0]]
    # BBB = [[1,0,1],[3,0,1],[5,0,1],[7,0,1],[0,1,1],[2,1,1],[4,1,1],[6,1,1],[1,2,1],[3,2,1],[5,2,1],[7,2,1]]
    # RRR = [[0,5,1],[2,5,1],[4,5,1],[6,5,1],[1,6,1],[3,6,1],[5,6,1],[7,6,1],[0,7,1],[2,7,1],[4,7,1],[6,7,1]]
    ENDBBB = [[0,7],[2,7],[4,7],[6,7]]
    ENDRRR = [[1,0],[3,0],[5,0],[7,0]]
    TTT = [[0,0,0],[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[0,1,0],[1,1,0],[2,1,0],[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0],[0,2,0],[1,2,0],[2,2,0],[3,2,0],[4,2,0],[5,2,0],[6,2,0],[7,2,0],[0,3,0],[1,3,0],[2,3,0],[3,3,0],[4,3,0],[5,3,0],[6,3,0],[7,3,0],[0,4,0],[1,4,0],[2,4,0],[3,4,0],[4,4,0],[5,4,0],[6,4,0],[7,4,0],[0,5,0],[1,5,0],[2,5,0],[3,5,0],[4,5,0],[5,5,0],[6,5,0],[7,5,0],[0,6,0],[1,6,0],[2,6,0],[3,6,0],[4,6,0],[5,6,0],[6,6,0],[7,6,0],[0,7,0],[1,7,0],[2,7,0],[3,7,0],[4,7,0],[5,7,0],[6,7,0],[7,7,0]]
    # Added helper function.
    def square_colour(row, col,colorof1):
        """ Determine colour of game board square from its position. """ 
        if colorof1==1:
            return yellow 
        elif colorof1==2:
            return orange 
        # elif colorof1==0:
        #     if (row + col) % 2 == 0:
        #         return white 
        #     else:
        #         return black 
    #Доска
    def boardGui(black,white,yellow):
        for gg in range(len(TTT)):
            boardRow=TTT[gg][1]
            boardColumn=TTT[gg][0]
            Colorof1=TTT[gg][2]
            xCoordinate=((margin+width) * boardColumn + margin)+xDistanceFromEdge
            yCoordinate=((margin+height) * boardRow + margin)+yDistanceFromEdge
            if Colorof1==1 or Colorof1==2:
                currentColour = square_colour(boardRow, boardColumn,Colorof1)
                pygame.draw.rect(display,currentColour,[xCoordinate,yCoordinate, width, height])

    def piecesGameBoard(gameBoard):
        if newGame:
            newGameBoard(gameBoard)
    #Шашки

    def newGameBoard(gameBoard):
        # Empty the game board.
        gameBoard[:] = [[None]*8 for _ in range(8)]
    
        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if  ShaskaB[2]==0:
                                gameBoard[ShaskaB[0]][ShaskaB[1]]="NormalBlack"
                            elif ShaskaB[2]==1:
                                gameBoard[ShaskaB[0]][ShaskaB[1]]="KingBlack"
                            

        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if ShaskaR[2]==0:
                                gameBoard[ShaskaR[0]][ShaskaR[1]]="NormalRed"
                            elif ShaskaR[2]==1:
                                gameBoard[ShaskaR[0]][ShaskaR[1]]="KingRed"
                            
        
                            
        

            
                
        #зарисовывает
        drawPieces(gameBoard,black,red)
        

    def drawPieces(gameBoard,black,red):
        for x in range(8):
            for y in range(8):
                xCoordinate=((margin+width) * x + margin+32)+xDistanceFromEdge
                yCoordinate=((margin+height) * y + margin+33)+yDistanceFromEdge
            
                if gameBoard[x][y]=="NormalBlack":
                    display.blit(black, (xCoordinate-50,yCoordinate-50))
                if gameBoard[x][y]=="KingBlack":
                    display.blit(king_black, (xCoordinate-50,yCoordinate-50))

                    #-----put letter k in the middle-----#
                if gameBoard[x][y]=="NormalRed":
                    display.blit(red, (xCoordinate-49,yCoordinate-49))
                if gameBoard[x][y]=="KingRed":
                    display.blit(king_red, (xCoordinate-49,yCoordinate-49))

    # -------- Main Program Loop -----------
    start=0
    WWIN=0
    player2 = True
    player1 = False
    ingame = pygame.image.load('ingame2l.png')
    ingame = pygame.transform.scale(ingame, (1280, 800))
    start_btn = Button(83, 40)
    options_btn = Button(100, 40)
    back_btn = Button(70, 40)
    quit_btn = Button(70, 40)
   
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and start==0 and player1 == True:
                #print("player1")
                #print(player1)
                #print("player2")
                #print(player2)
                pos = pygame.mouse.get_pos()
                #print(pos)

                column = (pos[0]-xDistanceFromEdge) // (width+margin)
                row = (pos[1]-yDistanceFromEdge) // (height+margin)
                #print(column)
                #print(row)
                for i in range(len(BBB)):
                    ShaskaB = BBB[i]
                    if column==ShaskaB[0] and row==ShaskaB[1]:
                        #print("Player1 chosed")  
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            if Total[0]==column and Total[1]==row:
                                Total[2]=1
                            elif Total[0]==column+1 and Total[1]==row+1 and gameBoard[column+1][row+1]==None and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column-1 and Total[1]==row+1 and gameBoard[column-1][row+1]==None and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row+2 and gameBoard[column+2][row+2]==None and (gameBoard[column+1][row+1]=="NormalRed" or gameBoard[column+1][row+1]=="KingRed") and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row+2 and gameBoard[column-2][row+2]==None and (gameBoard[column-1][row+1]=="NormalRed" or gameBoard[column-1][row+1]=="KingRed") and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row-2 and gameBoard[column+2][row-2]==None and (gameBoard[column+1][row-1]=="NormalRed" or gameBoard[column+1][row+1]=="KingRed") and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row-2 and gameBoard[column-2][row-2]==None and (gameBoard[column-1][row-1]=="NormalRed" or gameBoard[column-1][row-1]=="KingRed") and ShaskaB[2]==0:
                                Total[2]=2
                        start=1
                        
                        pygame.mixer.Sound.play(step_sound)

            elif event.type == pygame.MOUSEBUTTONDOWN and start==0 and player2 == True:
                #print("player1")
                #print(player1)
                #print("player2")
                #print(player2)
                pos = pygame.mouse.get_pos()
                #print(pos)
                column = (pos[0]-xDistanceFromEdge) // (width+margin)
                row = (pos[1]-yDistanceFromEdge) // (height+margin)
                #print(column)
                #print(row)
                for i in range(len(RRR)):
                    ShaskaR = RRR[i]
                    if column==ShaskaR[0] and row==ShaskaR[1]:
                        #print("Player2 chosed")
                        for t in range(len(TTT)):
                            Total=TTT[t]
                            if Total[0]==column and Total[1]==row:
                                Total[2]=1
                            elif Total[0]==column+1 and Total[1]==row-1 and gameBoard[column+1][row-1]==None and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column-1 and Total[1]==row-1 and gameBoard[column-1][row-1]==None and ShaskaB[2]==0:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row+2 and gameBoard[column+2][row+2]==None and (gameBoard[column+1][row+1]=="NormalBlack" or gameBoard[column+1][row+1]=="KingBlack") and ShaskaR[2]==0:
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row+2 and gameBoard[column-2][row+2]==None and (gameBoard[column-1][row+1]=="NormalBlack" or gameBoard[column-1][row+1]=="KingBlack") and ShaskaR[2]==0:
                                Total[2]=2
                            elif Total[0]==column+2 and Total[1]==row-2 and gameBoard[column+2][row-2]==None and (gameBoard[column+1][row-1]=="NormalBlack" or gameBoard[column+1][row-1]=="KingBlack") and ShaskaR[2]==0:
                                Total[2]=2
                            elif Total[0]==column-2 and Total[1]==row-2 and gameBoard[column-2][row-2]==None and (gameBoard[column-1][row-1]=="NormalBlack" or gameBoard[column-1][row-1]=="KingBlack") and ShaskaR[2]==0:
                                Total[2]=2
                        start=1
                        
                        pygame.mixer.Sound.play(step_sound)
                        

            elif event.type == pygame.MOUSEBUTTONDOWN and start==1:
                poss = pygame.mouse.get_pos()
                #print(poss)

                columnn = (poss[0]-xDistanceFromEdge) // (width+margin)
                roww = (poss[1]-yDistanceFromEdge) // (height+margin)
                Ctest= (poss[0]-xDistanceFromEdge) // (width+margin)
                Rtest= (poss[1]-yDistanceFromEdge) // (height+margin)
                ChechB=0
                ChechR=0
                for i in range(len(BBB)):
                    ShaskaB = BBB[i]
                    if column==ShaskaB[0] and row==ShaskaB[1]:
                        ChechB=ShaskaB[2]
                        #print("CheckB",ChechB)
                for m in range(len(RRR)):
                    ShaskaR = RRR[m]
                    if column==ShaskaR[0] and row==ShaskaR[1]:
                        ChechR=ShaskaR[2]
                        #print("CheckR",ChechR)
    #1 игрок
                if player1==True and ChechB==0:
                    #print("oodosdfsdfmsdfmsdml")
                #1 игрок простой ход
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    if (columnn == column+1 and roww == row+1) or (columnn == column-1 and roww== row +1):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                #print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    start=0
                                    
                                    pygame.mixer.Sound.play(step_sound2)
                                    player1=False
                                    player2=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                #elif gameBoard[columnn][roww]=="NormalRed" and gameBoard[columnn][roww]=="NormalRed":
                                    #print("eat")
                                else:
                                    #print("You con not go like that!!!")
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                    #1 игрок ход с удаление противника
                    elif (columnn == column+2 and roww == row+2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="KingRed")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                    
                            if column==ShaskaB[0] and row==ShaskaB[1]: 
                                #print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="KingRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnn-1 and ShaskaR[1]==roww-1: 
                                            RRR.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalRed" or gameBoard[columnn+1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalRed" or gameBoard[columnn-1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalRed" or gameBoard[columnn+1][roww-1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalRed" or gameBoard[columnn-1][roww-1]=="KingRed"):
                                            Total[2]=2
                                    #player1=False
                                    #player2=True
                                


                    elif (columnn == column-2 and roww== row +2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="KingRed")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:   
                                #print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="KingRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnn+1 and ShaskaR[1]==roww-1:
                                            RRR.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalRed" or gameBoard[columnn+1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalRed" or gameBoard[columnn-1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalRed" or gameBoard[columnn+1][roww-1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalRed" or gameBoard[columnn-1][roww-1]=="KingRed"):
                                            Total[2]=2
                                    #player1=False
                                    #player2=True

                    elif (columnn == column+2 and roww == row-2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="KingRed")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                #print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="KingRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnn-1 and ShaskaR[1]==roww+1:
                                            RRR.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalRed" or gameBoard[columnn+1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalRed" or gameBoard[columnn-1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalRed" or gameBoard[columnn+1][roww-1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalRed" or gameBoard[columnn-1][roww-1]=="KingRed"):
                                            Total[2]=2
                                    #player1=False
                                    #player2=True
                            
                    elif (columnn == column-2 and roww== row -2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="KingRed")):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if column==ShaskaB[0] and row==ShaskaB[1]:    
                                #print(gameBoard[columnn][roww])
                                start=0
                                
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="NormalRed") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="KingRed"):
                                    ShaskaB[0]=columnn
                                    ShaskaB[1]=roww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnn+1 and ShaskaR[1]==roww+1:
                                            RRR.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalRed" or gameBoard[columnn+1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalRed" or gameBoard[columnn-1][roww+1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalRed" or gameBoard[columnn+1][roww-1]=="KingRed"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalRed" or gameBoard[columnn-1][roww-1]=="KingRed"):
                                            Total[2]=2
                                    #player1=False
                                    #player2=True

                    else:
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0








                elif player1==True and ChechB==1:
                #1 игрок королева простой ход
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    CCheck2=0
                    if (columnn < column and roww < row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1
                                                

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnn < column and roww > row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1
                                                

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            
                                        else:
                                            start=0  
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnn > column and roww < row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1
                                                

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0

                    elif (columnn > column and roww > row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if column==ShaskaB[0] and row==ShaskaB[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1
                                                

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaB[0]=columnn
                                            ShaskaB[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            
                                        else:
                                            start=0  
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    else:
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                        start=0
                        pygame.mixer.Sound.play(step_sound2)










    #2 игрок
                elif player2==True and ChechR==0:
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    #2 игрок простой ход
                    if (columnn == column+1 and roww == row-1) or (columnn == column-1 and roww== row-1):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                #print(gameBoard[columnn][roww])
                                start=0
                                if gameBoard[columnn][roww]==None:
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    player2=False
                                    player1=True
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0


                                else:
                                    start=0
                                    pygame.mixer.Sound.play(step_sound2)
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                    #2 игрок ход с поеданием
                    elif (columnn == column+2 and roww == row-2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="KingBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                #print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww+1]=="KingBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnn-1 and ShaskaB[1]==roww+1:
                                            BBB.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalBlack" or gameBoard[columnn+1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalBlack" or gameBoard[columnn-1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalBlack" or gameBoard[columnn+1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalBlack" or gameBoard[columnn-1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                    #player2=False
                                    #player1=True
                            

                    elif (columnn == column-2 and roww== row -2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="KingBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:    
                                #print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww+1]=="KingBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnn+1 and ShaskaB[1]==roww+1:
                                            BBB.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalBlack" or gameBoard[columnn+1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalBlack" or gameBoard[columnn-1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalBlack" or gameBoard[columnn+1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalBlack" or gameBoard[columnn-1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                    #player2=False
                                    #player1=True

                    elif (columnn == column+2 and roww == row+2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="KingBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:   
                                #print(gameBoard[columnn][roww])
                                start=0
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn-1][roww-1]=="KingBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnn-1 and ShaskaB[1]==roww-1:
                                            BBB.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalBlack" or gameBoard[columnn+1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalBlack" or gameBoard[columnn-1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalBlack" or gameBoard[columnn+1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalBlack" or gameBoard[columnn-1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                    #player2=False
                                    #player1=True
                            
                    
                    elif (columnn == column-2 and roww== row +2) and ((gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="KingBlack")):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if column==ShaskaR[0] and row==ShaskaR[1]:   
                                #print(gameBoard[columnn][roww])
                                start=0
                        
                                if (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="NormalBlack") or (gameBoard[columnn][roww]==None and gameBoard[columnn+1][roww-1]=="KingBlack"):
                                    ShaskaR[0]=columnn
                                    ShaskaR[1]=roww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnn+1 and ShaskaB[1]==roww-1:
                                            BBB.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnn
                                    pos_row=roww
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                                    for t in range(len(TTT)):
                                        Total=TTT[t]
                                        if Total[0]==columnn and Total[1]==roww:
                                            Total[2]=1
                                        elif Total[0]==columnn+2 and Total[1]==roww+2 and gameBoard[columnn+2][roww+2]==None and (gameBoard[columnn+1][roww+1]=="NormalBlack" or gameBoard[columnn+1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww+2 and gameBoard[columnn-2][roww+2]==None and (gameBoard[columnn-1][roww+1]=="NormalBlack" or gameBoard[columnn-1][roww+1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn+2 and Total[1]==roww-2 and gameBoard[columnn+2][roww-2]==None and (gameBoard[columnn+1][roww-1]=="NormalBlack" or gameBoard[columnn+1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                        elif Total[0]==columnn-2 and Total[1]==roww-2 and gameBoard[columnn-2][roww-2]==None and (gameBoard[columnn-1][roww-1]=="NormalBlack" or gameBoard[columnn-1][roww-1]=="KingBlack"):
                                            Total[2]=2
                                    #player2=False
                                    #player1=True


                    else:
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0
                        start=0
                        pygame.mixer.Sound.play(step_sound2)




                elif player2==True and ChechR==1:
                #2 игрок королева простой ход
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    CCheck2=0
                    if (columnn < column and roww < row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1
                                                

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            
                                        else:
                                            start=0  
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnn < column and roww > row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            
                                        else:
                                            start=0  
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnn > column and roww < row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            
                                        else:
                                            start=0  
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0

                    elif (columnn > column and roww > row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if column==ShaskaR[0] and row==ShaskaR[1]:
                    
                                while (Ctest != column and Rtest != row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnn and RRROW[0]==roww and CCCOLUMN[-1]==column and RRROW[-1]==row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnn
                                            pos_row=roww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnn and Total[1]==roww:
                                                    Total[2]=1

                                        elif CCheck==len(CCCOLUMN)-2:
                                            ShaskaR[0]=columnn
                                            ShaskaR[1]=roww
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            
                                        else:
                                            start=0  
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    else:
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    else:
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                
            elif event.type == pygame.MOUSEBUTTONDOWN and start==2: 
                
                pos = pygame.mouse.get_pos()
                #print(pos)

                # Change the x/y display coordinates to grid coordinates
                columnnn = (pos[0]-xDistanceFromEdge) // (width+margin)
                rowww = (pos[1]-yDistanceFromEdge) // (height+margin)
                
                Ctest= (pos[0]-xDistanceFromEdge) // (width+margin)
                Rtest= (pos[1]-yDistanceFromEdge) // (height+margin)
    
                for i in range(len(BBB)):
                    ShaskaB = BBB[i]
                    if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:
                        ChechB=ShaskaB[2]
                for m in range(len(RRR)):
                    ShaskaR = RRR[m]
                    if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:
                        ChechR=ShaskaR[2]

                if player1==True and ChechB==0:
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    if (columnnn == pos_column+2 and rowww == pos_row+2):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:    
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww-1]=="NormalRed") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww-1]=="KingRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnnn-1 and ShaskaR[1]==rowww-1: 
                                            RRR.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalRed" or gameBoard[columnnn+1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalRed" or gameBoard[columnnn-1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalRed" or gameBoard[columnnn+1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalRed" or gameBoard[columnnn-1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                    #player1=False
                                    #player2=True
                                


                    elif (columnnn == pos_column-2 and rowww== pos_row +2):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]: 
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww-1]=="NormalRed") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww-1]=="KingRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnnn+1 and ShaskaR[1]==rowww-1:
                                            RRR.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalRed" or gameBoard[columnnn+1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalRed" or gameBoard[columnnn-1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalRed" or gameBoard[columnnn+1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalRed" or gameBoard[columnnn-1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                    #player1=False
                                    #player2=True

                    elif (columnnn == pos_column+2 and rowww == pos_row-2):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:   
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww+1]=="NormalRed") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww+1]=="KingRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnnn-1 and ShaskaR[1]==rowww+1:
                                            RRR.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalRed" or gameBoard[columnnn+1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalRed" or gameBoard[columnnn-1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalRed" or gameBoard[columnnn+1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalRed" or gameBoard[columnnn-1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                    #player1=False
                                    #player2=True
                            
                    elif (columnnn == pos_column-2 and rowww== pos_row -2):
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                        
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:   
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww+1]=="NormalRed") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww+1]=="KingRed"):
                                    ShaskaB[0]=columnnn
                                    ShaskaB[1]=rowww
                                    for j in range(len(RRR)):                             
                                        ShaskaR = RRR[j]
                                        if ShaskaR[0]==columnnn+1 and ShaskaR[1]==rowww+1:
                                            RRR.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalRed" or gameBoard[columnnn+1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalRed" or gameBoard[columnnn-1][rowww+1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalRed" or gameBoard[columnnn+1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalRed" or gameBoard[columnnn-1][rowww-1]=="KingRed"):
                                                    Total[2]=2
                                    #player1=False
                                    #player2=True

                    else:
                        #print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
                        player1=False
                        player2=True
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                
                
                    

                elif player1==True and ChechB==1:
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    #print("gggggggggggggggg")
                    CCheck2=0
                    if (columnnn < pos_column and rowww < pos_row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        #print("1")
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnnn
                                            ShaskaB[1]=rowww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                        else:
                                            #print("gg")
                                            start=0    
                                            pygame.mixer.Sound.play(step_sound2)
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0

                                    else:
                                        #print("gg")
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        player1=False
                                        player2=True
                                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnnn < pos_column and rowww > pos_row):
                        #print("2")
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if pos_column ==ShaskaB[0] and pos_row==ShaskaB[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnnn
                                            ShaskaB[1]=rowww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1

                                        else:
                                            #print("gg")
                                            start=0   
                                            pygame.mixer.Sound.play(step_sound2)
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                
                                    else:
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnnn > pos_column and rowww < pos_row):
                        #print("3")
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnnn
                                            ShaskaB[1]=rowww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                        else:
                                            start=0   
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                            
                                    else:
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        #print("gg")
                                        player1=False
                                        player2=True
                                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnnn > pos_column and rowww > pos_row):
                        #print("4")
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalRed" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingRed":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaB[0]=columnnn
                                            ShaskaB[1]=rowww

                                            for j in range(len(RRR)):                             
                                                ShaskaR = RRR[j]
                                                if ShaskaR[0]==DeleteC and ShaskaR[1]==DeleteR: 
                                                    RRR.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                        else:
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    
                                    
                                    else:
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player1=False
                                            player2=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    else:
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        #print("end")
                        player1=False
                        player2=True
                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0






                elif player2==True and ChechR==0: 
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    if (columnnn == pos_column+2 and rowww == pos_row-2):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:    
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww+1]=="NormalBlack") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww+1]=="KingBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnnn-1 and ShaskaB[1]==rowww+1:
                                            BBB.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalBlack" or gameBoard[columnnn+1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalBlack" or gameBoard[columnnn-1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalBlack" or gameBoard[columnnn+1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalBlack" or gameBoard[columnnn-1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                    #player2=False
                                    #player1=True
                            

                    elif (columnnn == pos_column-2 and rowww== pos_row -2):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:     
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww+1]=="NormalBlack") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww+1]=="KingBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnnn+1 and ShaskaB[1]==rowww+1:
                                            BBB.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalBlack" or gameBoard[columnnn+1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalBlack" or gameBoard[columnnn-1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalBlack" or gameBoard[columnnn+1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalBlack" or gameBoard[columnnn-1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                    #player2=False
                                    #player1=True

                    elif (columnnn == pos_column+2 and rowww == pos_row+2):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:   
                                #print(gameBoard[columnnn][rowww])
                                start=0
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww-1]=="NormalBlack") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn-1][rowww-1]=="KingBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnnn-1 and ShaskaB[1]==rowww-1:
                                            BBB.pop(j)
                                            break
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalBlack" or gameBoard[columnnn+1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalBlack" or gameBoard[columnnn-1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalBlack" or gameBoard[columnnn+1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalBlack" or gameBoard[columnnn-1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                    #player2=False
                                    #player1=True
                            
                    
                    elif (columnnn == pos_column-2 and rowww== pos_row +2):
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                        
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:   
                                #print(gameBoard[columnnn][rowww])
                                start=0
                        
                                if (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww-1]=="NormalBlack") or (gameBoard[columnnn][rowww]==None and gameBoard[columnnn+1][rowww-1]=="KingBlack"):
                                    ShaskaR[0]=columnnn
                                    ShaskaR[1]=rowww
                                    for j in range(len(BBB)):                             
                                        ShaskaB = BBB[j]
                                        if ShaskaB[0]==columnnn+1 and ShaskaB[1]==rowww-1:
                                            BBB.pop(j)
                                            break
                                    #RRR.pop([columnn+1][roww-1])
                                    start=2
                                    pygame.mixer.Sound.play(step_sound2)
                                    pos_column=columnnn
                                    pos_row=rowww
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                                elif Total[0]==columnnn+2 and Total[1]==rowww+2 and gameBoard[columnnn+2][rowww+2]==None and (gameBoard[columnnn+1][rowww+1]=="NormalBlack" or gameBoard[columnnn+1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww+2 and gameBoard[columnnn-2][rowww+2]==None and (gameBoard[columnnn-1][rowww+1]=="NormalBlack" or gameBoard[columnnn-1][rowww+1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn+2 and Total[1]==rowww-2 and gameBoard[columnnn+2][rowww-2]==None and (gameBoard[columnnn+1][rowww-1]=="NormalBlack" or gameBoard[columnnn+1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                                elif Total[0]==columnnn-2 and Total[1]==rowww-2 and gameBoard[columnnn-2][rowww-2]==None and (gameBoard[columnnn-1][rowww-1]=="NormalBlack" or gameBoard[columnnn-1][rowww-1]=="KingBlack"):
                                                    Total[2]=2
                                    #player2=False
                                    #player1=True    
                    else:
                        player2=False
                        player1=True
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0

                elif player2==True and ChechR==1:
                    #print("player1")
                    #print(player1)
                    #print("player2")
                    #print(player2)
                    #print("gggggggggggggggg")
                    CCheck2=0
                    if (columnnn < pos_column and rowww < pos_row):
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        #print("1")
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnnn
                                            ShaskaR[1]=rowww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                        else:
                                            #print("gg")
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0

                                    else:
                                        #print("gg")
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        player2=False
                                        player1=True
                                        for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnnn < pos_column and rowww > pos_row):
                        #print("2")
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if pos_column ==ShaskaR[0] and pos_row==ShaskaR[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest + 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnnn
                                            ShaskaR[1]=rowww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1

                                        else:
                                            #print("gg")
                                            start=0   
                                            pygame.mixer.Sound.play(step_sound2)
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                
                                    else:
                                            start=0
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    elif (columnnn > pos_column and rowww < pos_row):
                        #print("3")
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest + 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnnn
                                            ShaskaR[1]=rowww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                        else:
                                            start=0   
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                            
                                    else:
                                        start=0
                                        pygame.mixer.Sound.play(step_sound2)
                                        #print("gg")
                                        player2=False
                                        player1=True
                                        for t in range(len(TTT)):
                                            Total=TTT[t]
                                            Total[2]=0
                    elif (columnnn > pos_column and rowww > pos_row):
                        #print("4")
                        CCCOLUMN=[Ctest]
                        RRROW=[Rtest]
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:
                    
                                while (Ctest != pos_column and Rtest != pos_row):
                                    Ctest = Ctest - 1
                                    Rtest = Rtest - 1
                                    CCCOLUMN.append(Ctest)
                                    RRROW.append(Rtest)
                                #print(CCCOLUMN)
                                #print(RRROW)
                                if CCCOLUMN[0]==columnnn and RRROW[0]==rowww and CCCOLUMN[-1]==pos_column and RRROW[-1]==pos_row:
                                    #print("good")
                                    CCheck=0
                                    if (gameBoard[CCCOLUMN[0]][RRROW[0]]==None):
                                        for hh in range(1,len(CCCOLUMN)-1):
                                            if gameBoard[CCCOLUMN[hh]][RRROW[hh]]==None:
                                                CCheck+=1
                                            elif gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="NormalBlack" or gameBoard[CCCOLUMN[hh]][RRROW[hh]]=="KingBlack":
                                                DeleteC=CCCOLUMN[hh]
                                                DeleteR=RRROW[hh]
                                                CCheck2+=1
                                        if CCheck==len(CCCOLUMN)-3 and CCheck2==1:

                                            ShaskaR[0]=columnnn
                                            ShaskaR[1]=rowww

                                            for j in range(len(BBB)):                             
                                                ShaskaB = BBB[j]
                                                if ShaskaB[0]==DeleteC and ShaskaB[1]==DeleteR: 
                                                    BBB.pop(j)
                                                    break
                                            start=2
                                            pygame.mixer.Sound.play(step_sound2)
                                            pos_column=columnnn
                                            pos_row=rowww
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                if Total[0]==columnnn and Total[1]==rowww:
                                                    Total[2]=1
                                        else:
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0

                                    else:
                                            start=0 
                                            pygame.mixer.Sound.play(step_sound2)
                                            #print("gg")
                                            player2=False
                                            player1=True
                                            for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                    else:
                        start=0
                        pygame.mixer.Sound.play(step_sound2)
                        #print("end")
                        player2=False
                        player1=True
                        for t in range(len(TTT)):
                                        Total=TTT[t]
                                        Total[2]=0

            if start==2: 
                if player2==True and ChechR==0:
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1]:
                                gg=1
                                if (pos_column+2<8 and pos_row-2 >-1): 
                                    if (gameBoard[pos_column+2][pos_row-2]==None and gameBoard[pos_column+1][pos_row-1]=="NormalBlack") or (gameBoard[pos_column+2][pos_row-2]==None and gameBoard[pos_column+1][pos_row-1]=="KingBlack"):
                                        #print("111111111")
                                        start=2 
                                        gg=0
                                if (pos_column-2>-1 and pos_row-2 >-1):
                                    if (gameBoard[pos_column-2][pos_row -2]==None and gameBoard[pos_column-1][pos_row -1]=="NormalBlack") or (gameBoard[pos_column-2][pos_row -2]==None and gameBoard[pos_column-1][pos_row -1]=="KingBlack"):
                                        #print("111111111")
                                        start=2
                                        gg=0
                                if (pos_column+2<8 and pos_row+2<8):
                                    if (gameBoard[pos_column+2][pos_row+2]==None and gameBoard[pos_column+1][pos_row+1]=="NormalBlack") or (gameBoard[pos_column+2][pos_row+2]==None and gameBoard[pos_column+1][pos_row+1]=="KingBlack"):    
                                        #print("111111111")
                                        start=2 
                                        gg=0
                                if (pos_column-2>-1 and pos_row+2 <8):
                                    if (gameBoard[pos_column-2][pos_row +2]==None and gameBoard[pos_column-1][pos_row +1]=="NormalBlack") or (gameBoard[pos_column-2][pos_row +2]==None and gameBoard[pos_column-1][pos_row +1]=="KingBlack"):
                                        #print("111111111")
                                        start=2 
                                        gg=0
                                if gg==1:
                                    player2=False
                                    player1=True
                                    start=0
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                elif player1==True and ChechB==0:
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1]:
                                gg=1
                                if (pos_column+2<8 and pos_row-2 >-1): 
                                    if (gameBoard[pos_column+2][pos_row-2]==None and gameBoard[pos_column+1][pos_row-1]=="NormalRed") or (gameBoard[pos_column+2][pos_row-2]==None and gameBoard[pos_column+1][pos_row-1]=="KingRed"):
                                        #print("111111111")
                                        start=2 
                                        gg=0
                                if (pos_column-2>-1 and pos_row-2 >-1):
                                    if (gameBoard[pos_column-2][pos_row -2]==None and gameBoard[pos_column-1][pos_row -1]=="NormalRed") or (gameBoard[pos_column-2][pos_row -2]==None and gameBoard[pos_column-1][pos_row -1]=="KingRed"):
                                        #print("111111111")
                                        start=2
                                        gg=0
                                if (pos_column+2 <8 and pos_row+2<8):
                                    if (gameBoard[pos_column+2][pos_row+2]==None and gameBoard[pos_column+1][pos_row+1]=="NormalRed") or (gameBoard[pos_column+2][pos_row+2]==None and gameBoard[pos_column+1][pos_row+1]=="KingRed"):   
                                        #print("111111111")
                                        start=2 
                                        gg=0
                                if (pos_column-2>-1 and pos_row+2 <8):
                                    if (gameBoard[pos_column-2][pos_row +2]==None and gameBoard[pos_column-1][pos_row +1]=="NormalRed") or (gameBoard[pos_column-2][pos_row +2]==None and gameBoard[pos_column-1][pos_row +1]=="KingRed"):
                                        #print("111111111")
                                        start=2 
                                        gg=0
                                if gg==1:
                                    player1=False
                                    player2=True
                                    start=0 
                                    for t in range(len(TTT)):
                                                Total=TTT[t]
                                                Total[2]=0
                elif player1==True and ChechB==1:
                        for i in range(len(BBB)):
                            ShaskaB = BBB[i]
                            if pos_column==ShaskaB[0] and pos_row==ShaskaB[1] and ShaskaB[2]==1:
                                gg=1
                                for x in range(0,8):
                                    if (pos_column+x<8 and pos_row-x >-1 and pos_column+x-1>-1 and pos_row-x+1<8): 
                                        if (gameBoard[pos_column+x][pos_row-x]==None and gameBoard[pos_column+x-1][pos_row-x+1]=="NormalRed") or (gameBoard[pos_column+x][pos_row-x]==None and gameBoard[pos_column+x-1][pos_row-x+1]=="KingRed"):
                                            #print("111111111")
                                            start=2 
                                            gg=0
                                    if (pos_column-x>-1 and pos_row-x >-1 and pos_column-x+1<8 and pos_row -x+1<8):
                                        if (gameBoard[pos_column-x][pos_row -x]==None and gameBoard[pos_column-x+1][pos_row -x+1]=="NormalRed") or (gameBoard[pos_column-x][pos_row -x]==None and gameBoard[pos_column-x+1][pos_row -x+1]=="KingRed"):
                                            #print("111111111")
                                            start=2
                                            gg=0
                                    if (pos_column+x <8 and pos_row+x<8 and pos_column+x-1>-1 and pos_row+x-1>-1):
                                        if (gameBoard[pos_column+x][pos_row+x]==None and gameBoard[pos_column+x-1][pos_row+x-1]=="NormalRed") or (gameBoard[pos_column+x][pos_row+x]==None and gameBoard[pos_column+x-1][pos_row+x-1]=="KingRed"):   
                                            #print("111111111")
                                            start=2 
                                            gg=0
                                    if (pos_column-x>-1 and pos_row+x <8 and pos_column-x+1<8 and pos_row +x-1>-1):
                                        if (gameBoard[pos_column-x][pos_row +x]==None and gameBoard[pos_column-x+1][pos_row +x-1]=="NormalRed") or (gameBoard[pos_column-x][pos_row +x]==None and gameBoard[pos_column-x+1][pos_row +x-1]=="KingRed"):
                                            #print("111111111")
                                            start=2 
                                            gg=0
                                if gg==1:
                                        player1=False
                                        player2=True
                                        start=0 
                                        for t in range(len(TTT)):
                                                    Total=TTT[t]
                                                    Total[2]=0
                elif player2==True and ChechR==1:
                        for i in range(len(RRR)):
                            ShaskaR = RRR[i]
                            if pos_column==ShaskaR[0] and pos_row==ShaskaR[1] and ShaskaR[2]==1:
                                gg=1
                                for x in range(0,8):
                                    if (pos_column+x<8 and pos_row-x >-1 and pos_column+x-1>-1 and pos_row-x+1<8): 
                                        if (gameBoard[pos_column+x][pos_row-x]==None and gameBoard[pos_column+x-1][pos_row-x+1]=="NormalBlack") or (gameBoard[pos_column+x][pos_row-x]==None and gameBoard[pos_column+x-1][pos_row-x+1]=="KingBlack"):
                                            #print("111111111")
                                            start=2 
                                            gg=0
                                    if (pos_column-x>-1 and pos_row-x >-1 and pos_column-x+1<8 and pos_row -x+1<8):
                                        if (gameBoard[pos_column-x][pos_row -x]==None and gameBoard[pos_column-x+1][pos_row -x+1]=="NormalBlack") or (gameBoard[pos_column-x][pos_row -x]==None and gameBoard[pos_column-x+1][pos_row -x+1]=="KingBlack"):
                                            #print("111111111")
                                            start=2
                                            gg=0
                                    if (pos_column+x <8 and pos_row+x<8 and pos_column+x-1>-1 and pos_row+x-1>-1):
                                        if (gameBoard[pos_column+x][pos_row+x]==None and gameBoard[pos_column+x-1][pos_row+x-1]=="NormalBlack") or (gameBoard[pos_column+x][pos_row+x]==None and gameBoard[pos_column+x-1][pos_row+x-1]=="KingBlack"):   
                                            #print("111111111")
                                            start=2 
                                            gg=0
                                    if (pos_column-x>-1 and pos_row+x <8 and pos_column-x+1<8 and pos_row +x-1>-1):
                                        if (gameBoard[pos_column-x][pos_row +x]==None and gameBoard[pos_column-x+1][pos_row +x-1]=="NormalBlack") or (gameBoard[pos_column-x][pos_row +x]==None and gameBoard[pos_column-x+1][pos_row +x-1]=="KingBlack"):
                                            #print("111111111")
                                            start=2 
                                            gg=0
                                if gg==1:
                                        player2=False
                                        player1=True
                                        start=0 
                                        for t in range(len(TTT)):
                                                    Total=TTT[t]
                                                    Total[2]=0

                

        for i in range(len(BBB)):
            ShaskaB = BBB[i] 
            for j in range(len(ENDBBB)):
                ShaskaENDB = ENDBBB[j] 
                if ShaskaB[0]==ShaskaENDB[0] and ShaskaB[1]==ShaskaENDB[1]:
                    ShaskaB[2]=1
                    #print("king")
        for i in range(len(RRR)):
            ShaskaR = RRR[i] 
            for j in range(len(ENDRRR)):
                ShaskaENDR = ENDRRR[j] 
                if ShaskaR[0]==ShaskaENDR[0] and ShaskaR[1]==ShaskaENDR[1]:
                    ShaskaR[2]=1
                    #print("king")
        if WWIN==0:
            if BBB == []:
                #print("Red wins")
                WWIN=1
                Win()
            if RRR == []:
                WWIN=1
                Win()



        display.blit(ingame, (0, 0))
        start_btn.draw(95, 90, 'Select', Select, 20)
        back_btn.draw(100, 140, 'Menu', show_menu, 20)
        quit_btn.draw(100, 190, 'Quit', quit, 20)
        header = pygame.image.load('header-title1.png')
        header= pygame.transform.scale(header, (400,200))
        display.blit(header, (xDistanceFromEdge*3+80, yDistanceFromEdge-70))
        Music_btn = Button(110, 40)
        Music2_btn = Button(110, 40)
        Music_btn.draw(xDistanceFromEdge*4+130, yDistanceFromEdge*4-66, 'Music off', Music2, 20)
        Music2_btn.draw(xDistanceFromEdge*4-80, yDistanceFromEdge*4-66, 'Music on', Music, 20)
        if player1==True:
            print_text('player2 turn', xDistanceFromEdge*3+210, yDistanceFromEdge+70)
        elif player2==True:
            print_text('player1 turn' , xDistanceFromEdge*3+210, yDistanceFromEdge+70)
                    

        
        display.blit(bord, (xDistanceFromEdge-26, yDistanceFromEdge-26))
   
        display.blit(nikandreos, (xDistanceFromEdge-300, yDistanceFromEdge*4-10)) 

        display.blit(apollo, (xDistanceFromEdge*4-300, yDistanceFromEdge*4-55))

        display.blit(artemis, (xDistanceFromEdge*4-80, yDistanceFromEdge*4-55))

        #Доска
        boardGui(black,white,yellow)
        #Шашки
        piecesGameBoard(gameBoard)

    

        clock.tick(60)
        pygame.display.flip()







        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()

def Chess():
    size = (1280,800)
    fps = 60
    xDistanceFromEdge=240
    yDistanceFromEdge=140
    display = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    done = False

    ingame = pygame.image.load('ingame2l.png')
    ingame = pygame.transform.scale(ingame, (1280, 800))
    start_btn = Button(83, 40)
    options_btn = Button(100, 40)
    back_btn = Button(70, 40)
    quit_btn = Button(70, 40)

    board_size = 560
    fig_size = 64
    
    board = pygame.image.load("board4h.png")
    bishop_w = pygame.image.load("img/white_bishop.png")
    rook_w = pygame.image.load("img/white_rook.png")
    king_w = pygame.image.load("img/white_king.png")
    queen_w = pygame.image.load("img/white_queen.png")
    knight_w = pygame.image.load("img/white_knight.png")
    pawn_w = pygame.image.load("img/white_pawn.png")
    bishop_b = pygame.image.load("img/black_bishop.png")
    rook_b = pygame.image.load("img/black_rook.png")
    king_b = pygame.image.load("img/black_king.png")
    queen_b = pygame.image.load("img/black_queen.png")
    knight_b = pygame.image.load("img/black_knight.png")
    pawn_b = pygame.image.load("img/black_pawn.png")
    move = pygame.image.load("img/circle.png")

    board = pygame.transform.scale(board, (board_size,board_size))
    bishop_w = pygame.transform.scale(bishop_w, (fig_size,fig_size))
    rook_w = pygame.transform.scale(rook_w, (fig_size,fig_size))
    king_w = pygame.transform.scale(king_w, (fig_size,fig_size))
    queen_w = pygame.transform.scale(queen_w, (fig_size,fig_size))
    knight_w = pygame.transform.scale(knight_w, (fig_size,fig_size))
    pawn_w = pygame.transform.scale(pawn_w, (fig_size,fig_size))
    bishop_b = pygame.transform.scale(bishop_b, (fig_size,fig_size))
    rook_b = pygame.transform.scale(rook_b, (fig_size,fig_size))
    king_b = pygame.transform.scale(king_b, (fig_size,fig_size))
    queen_b = pygame.transform.scale(queen_b, (fig_size,fig_size))
    knight_b = pygame.transform.scale(knight_b, (fig_size,fig_size))
    pawn_b = pygame.transform.scale(pawn_b, (fig_size,fig_size))
    move = pygame.transform.scale(move, (fig_size-44,fig_size-44))

    x=64
    move_cnt_w=0
    move_cnt_b=0
    gs = chessEngine.GameState()
    selected = []
    playerClicks = []
    display.fill((211,211,211))
    margin_left=160
    margin_top=50
    check=0

    while not done:
        display.blit(ingame, (0, 0))
        start_btn.draw(95, 90, 'Select', Select, 20)
        back_btn.draw(100, 140, 'Menu', show_menu, 20)
        quit_btn.draw(100, 190, 'Quit', quit, 20)
        header = pygame.image.load('header-title1.png')
        header= pygame.transform.scale(header, (400,200))
        display.blit(header, (xDistanceFromEdge*3+80, yDistanceFromEdge-70))
        
        if gs.white_to_move==True:
            print_text('player1 turn', xDistanceFromEdge*3+210, yDistanceFromEdge+70)
        elif gs.white_to_move==False:
            print_text('player2 turn' , xDistanceFromEdge*3+210, yDistanceFromEdge+70)
                    

        display.blit(board,(margin_left+x,margin_top+x))

        display.blit(nikandreos, (xDistanceFromEdge-300, yDistanceFromEdge*4-10)) 

        display.blit(apollo, (xDistanceFromEdge*4-300, yDistanceFromEdge*4-55))

        display.blit(artemis, (xDistanceFromEdge*4-80, yDistanceFromEdge*4-55))
        Music_btn = Button(110, 40)
        Music2_btn = Button(110, 40)
        Music_btn.draw(xDistanceFromEdge*4+130, yDistanceFromEdge*4-66, 'Music off', Music2, 20)
        Music2_btn.draw(xDistanceFromEdge*4-80, yDistanceFromEdge*4-66, 'Music on', Music, 20)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1,y1 = event.pos
                row = ((x1-margin_left-28)//x)
                col = ((y1-margin_top-28)//x)
                if selected == [col,row]:
                    selected = []
                    playerClicks = []
                    for i in range(len(gs.map)):
                            for j in range(len(gs.map[i])):
                                if gs.map[i][j]=="M":
                                    gs.map[i][j]=""
                else:
                    selected = [col,row]
                    playerClicks.append(selected)
                if len(playerClicks) == 1:
                    if gs.white_to_move == True:
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]!="" and gs.map[playerClicks[0][0]][playerClicks[0][1]].isupper(): 
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="P":
                            gs.getPawnWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="R":
                            gs.getRookWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="B":
                            gs.getBishopWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="Q":
                            gs.getQueenWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="K":
                            gs.getKnightWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="G":
                            gs.getKingWay(playerClicks[0][0],playerClicks[0][1])
                    else:
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]!="" and gs.map[playerClicks[0][0]][playerClicks[0][1]].islower(): 
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="p":
                            gs.getPawnWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="r":
                            gs.getRookWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="b":
                            gs.getBishopWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="q":
                            gs.getQueenWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="k":
                            gs.getKnightWay(playerClicks[0][0],playerClicks[0][1])
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="g":
                            gs.getKingWay(playerClicks[0][0],playerClicks[0][1])
                if len(playerClicks) == 2:
                    if gs.map[playerClicks[0][0]][playerClicks[0][1]]!="":
                        for i in range(len(gs.map)):
                            for j in range(len(gs.map[i])):
                                if gs.map[i][j]=="M":
                                    gs.map[i][j]=""
                        if gs.white_to_move == True :
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]!="" and gs.map[playerClicks[0][0]][playerClicks[0][1]].isupper(): 
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="P":
                                gs.getPawnMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="R":
                                move_cnt_w+=1
                                gs.getRookMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="B":
                                gs.getBishopMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="Q":
                                gs.getQueenMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="K":
                                gs.getKnightMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="G":
                                move_cnt_w+=1
                                gs.getKingMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1],move_cnt_w)
                        if gs.white_to_move == False:
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]!="" and gs.map[playerClicks[0][0]][playerClicks[0][1]].islower(): 
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="p":
                                gs.getPawnMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="r":
                                move_cnt_b+=1
                                gs.getRookMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="b":
                                gs.getBishopMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="q":
                                gs.getQueenMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="k":
                                gs.getKnightMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="g":
                                move_cnt_b+=1
                                gs.getKingMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1],move_cnt_b)
                    else:
                        selected = []
                        playerClicks = []
                if len(playerClicks) >= 2:
                    selected = []
                    playerClicks = []
        for i in range(len(gs.map)):
            for j in range(len(gs.map[i])):
                if gs.map[i][j]=="r":
                    display.blit(rook_b,(j*x+margin_left+24,i*x+margin_top+24))   
                if gs.map[i][j]=="k":
                    display.blit(knight_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="b":
                    display.blit(bishop_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="q":
                    display.blit(queen_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="g":
                    display.blit(king_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="p":
                    display.blit(pawn_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="R":
                    display.blit(rook_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="K":
                    display.blit(knight_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="B":
                    display.blit(bishop_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="Q":
                    display.blit(queen_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="G":
                    display.blit(king_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="P":
                    display.blit(pawn_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="M":
                    display.blit(move,(j*x+22+margin_left+24,i*x+22+margin_top+24))
                if (gs.map[i][j]=="G" or gs.map[i][j]=="g"):
                    check+=1
        if check%2==1:
            Win()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()

def Chess960():
    size = (1280,800)
    fps = 60
    xDistanceFromEdge=240
    yDistanceFromEdge=140
    display = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    done = False

    ingame = pygame.image.load('ingame2l.png')
    ingame = pygame.transform.scale(ingame, (1280, 800))
    start_btn = Button(83, 40)
    options_btn = Button(100, 40)
    back_btn = Button(70, 40)
    quit_btn = Button(70, 40)

    board_size = 560
    fig_size = 64
    
    board = pygame.image.load("board4h.png")
    bishop_w = pygame.image.load("img/white_bishop.png")
    rook_w = pygame.image.load("img/white_rook.png")
    king_w = pygame.image.load("img/white_king.png")
    queen_w = pygame.image.load("img/white_queen.png")
    knight_w = pygame.image.load("img/white_knight.png")
    pawn_w = pygame.image.load("img/white_pawn.png")
    bishop_b = pygame.image.load("img/black_bishop.png")
    rook_b = pygame.image.load("img/black_rook.png")
    king_b = pygame.image.load("img/black_king.png")
    queen_b = pygame.image.load("img/black_queen.png")
    knight_b = pygame.image.load("img/black_knight.png")
    pawn_b = pygame.image.load("img/black_pawn.png")
    move = pygame.image.load("img/circle.png")

    board = pygame.transform.scale(board, (board_size,board_size))
    bishop_w = pygame.transform.scale(bishop_w, (fig_size,fig_size))
    rook_w = pygame.transform.scale(rook_w, (fig_size,fig_size))
    king_w = pygame.transform.scale(king_w, (fig_size,fig_size))
    queen_w = pygame.transform.scale(queen_w, (fig_size,fig_size))
    knight_w = pygame.transform.scale(knight_w, (fig_size,fig_size))
    pawn_w = pygame.transform.scale(pawn_w, (fig_size,fig_size))
    bishop_b = pygame.transform.scale(bishop_b, (fig_size,fig_size))
    rook_b = pygame.transform.scale(rook_b, (fig_size,fig_size))
    king_b = pygame.transform.scale(king_b, (fig_size,fig_size))
    queen_b = pygame.transform.scale(queen_b, (fig_size,fig_size))
    knight_b = pygame.transform.scale(knight_b, (fig_size,fig_size))
    pawn_b = pygame.transform.scale(pawn_b, (fig_size,fig_size))
    move = pygame.transform.scale(move, (fig_size-44,fig_size-44))

    x=64
    move_cnt_w=0
    move_cnt_b=0
    gs = chessEngine1.GameState()
    selected = []
    playerClicks = []
    display.fill((211,211,211))
    margin_left=160
    margin_top=50
    check=0

    while not done:
        display.blit(ingame, (0, 0))
        start_btn.draw(95, 90, 'Select', Select, 20)
        back_btn.draw(100, 140, 'Menu', show_menu, 20)
        quit_btn.draw(100, 190, 'Quit', quit, 20)
        header = pygame.image.load('header-title1.png')
        header= pygame.transform.scale(header, (400,200))
        display.blit(header, (xDistanceFromEdge*3+80, yDistanceFromEdge-70))
        
        if gs.white_to_move==True:
            print_text('player1 turn', xDistanceFromEdge*3+210, yDistanceFromEdge+70)
        elif gs.white_to_move==False:
            print_text('player2 turn' , xDistanceFromEdge*3+210, yDistanceFromEdge+70)
                    

        display.blit(board,(margin_left+x,margin_top+x))

        display.blit(nikandreos, (xDistanceFromEdge-300, yDistanceFromEdge*4-10)) 

        display.blit(apollo, (xDistanceFromEdge*4-300, yDistanceFromEdge*4-55))

        display.blit(artemis, (xDistanceFromEdge*4-80, yDistanceFromEdge*4-55))
        Music_btn = Button(110, 40)
        Music2_btn = Button(110, 40)
        Music_btn.draw(xDistanceFromEdge*4+130, yDistanceFromEdge*4-66, 'Music off', Music2, 20)
        Music2_btn.draw(xDistanceFromEdge*4-80, yDistanceFromEdge*4-66, 'Music on', Music, 20)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1,y1 = event.pos
                row = ((x1-margin_left-28)//x)
                col = ((y1-margin_top-28)//x)
                if selected == [col,row]:
                    selected = []
                    playerClicks = []
                    for i in range(len(gs.map)):
                            for j in range(len(gs.map[i])):
                                if gs.map[i][j]=="M":
                                    gs.map[i][j]=""
                else:
                    selected = [col,row]
                    playerClicks.append(selected)
                if len(playerClicks) == 1:
                    if gs.white_to_move == True:
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="P":
                            gs.getPawnWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="R":
                            gs.getRookWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="B":
                            gs.getBishopWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="Q":
                            gs.getQueenWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="K":
                            gs.getKnightWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="G":
                            gs.getKingWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                    else:
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="p":
                            gs.getPawnWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="r":
                            gs.getRookWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="b":
                            gs.getBishopWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="q":
                            gs.getQueenWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="k":
                            gs.getKnightWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                        if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="g":
                            gs.getKingWay(playerClicks[0][0],playerClicks[0][1])
                            pygame.mixer.Sound.play(step_sound)
                if len(playerClicks) == 2:
                    if gs.map[playerClicks[0][0]][playerClicks[0][1]]!="":
                        for i in range(len(gs.map)):
                            for j in range(len(gs.map[i])):
                                if gs.map[i][j]=="M":
                                    gs.map[i][j]=""
                        if gs.white_to_move == True :
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="P":
                                gs.getPawnMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="R":
                                move_cnt_w+=1
                                gs.getRookMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="B":
                                gs.getBishopMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="Q":
                                gs.getQueenMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="K":
                                gs.getKnightMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="G":
                                move_cnt_w+=1
                                gs.getKingMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1],move_cnt_w)
                                pygame.mixer.Sound.play(step_sound2)
                        if gs.white_to_move == False:
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="p":
                                gs.getPawnMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="r":
                                move_cnt_b+=1
                                gs.getRookMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="b":
                                gs.getBishopMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="q":
                                gs.getQueenMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="k":
                                gs.getKnightMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1])
                                pygame.mixer.Sound.play(step_sound2)
                            if gs.map[playerClicks[0][0]][playerClicks[0][1]]=="g":
                                move_cnt_b+=1
                                gs.getKingMoves(playerClicks[0][0],playerClicks[0][1],playerClicks[1][0],playerClicks[1][1],move_cnt_b)
                                pygame.mixer.Sound.play(step_sound2)
                    else:
                        selected = []
                        playerClicks = []
                if len(playerClicks) >= 2:
                    selected = []
                    playerClicks = []
        for i in range(len(gs.map)):
            for j in range(len(gs.map[i])):
                if gs.map[i][j]=="r":
                    display.blit(rook_b,(j*x+margin_left+24,i*x+margin_top+24))   
                if gs.map[i][j]=="k":
                    display.blit(knight_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="b":
                    display.blit(bishop_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="q":
                    display.blit(queen_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="g":
                    display.blit(king_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="p":
                    display.blit(pawn_b,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="R":
                    display.blit(rook_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="K":
                    display.blit(knight_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="B":
                    display.blit(bishop_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="Q":
                    display.blit(queen_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="G":
                    display.blit(king_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="P":
                    display.blit(pawn_w,(j*x+margin_left+24,i*x+margin_top+24))
                if gs.map[i][j]=="M":
                    display.blit(move,(j*x+22+margin_left+24,i*x+22+margin_top+24))
                if (gs.map[i][j]=="G" or gs.map[i][j]=="g"):
                    check+=1
        if check%2==1:
            Win()
        keys = pygame.key.get_pressed()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pause()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()




def print_text(message, x, y, font_color = (252, 252, 252), font_type = 'DalekPinpointBold.ttf', font_size = 25):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
def print_text2(message, x, y, font_color = (255, 207, 37), font_type = 'DalekPinpointBold.ttf', font_size = 50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
def print_text3(message, x, y, font_color = (0, 0, 0), font_type = 'DalekPinpointBold.ttf', font_size = 50):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))

def Music():
    pygame.mixer.music.play(-1)
def Music2():
    pygame.mixer.music.pause()


def pause():
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text2('Paused press enter to continue', 290, 370)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)

    pygame.mixer.music.unpause()

show_menu()

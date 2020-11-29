import pygame 
import chessEngine

size = (1024,768)
fps = 60
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
done = False

board_size = 560
fig_size = 64
   
board = pygame.image.load("board1.png")
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
screen.fill((211,211,211))
margin_left=240
margin_top=140
check=0

while not done:
    Win=False
    screen.blit(board,(margin_left+x,margin_top+x))
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
                screen.blit(rook_b,(j*x+margin_left+24,i*x+margin_top+24))   
            if gs.map[i][j]=="k":
                screen.blit(knight_b,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="b":
                screen.blit(bishop_b,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="q":
                screen.blit(queen_b,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="g":
                screen.blit(king_b,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="p":
                screen.blit(pawn_b,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="R":
                screen.blit(rook_w,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="K":
                screen.blit(knight_w,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="B":
                screen.blit(bishop_w,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="Q":
                screen.blit(queen_w,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="G":
                screen.blit(king_w,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="P":
                screen.blit(pawn_w,(j*x+margin_left+24,i*x+margin_top+24))
            if gs.map[i][j]=="M":
                screen.blit(move,(j*x+22+margin_left+24,i*x+22+margin_top+24))
            # if (gs.map[i][j]=="G" or gs.map[i][j]=="g") and i<:
            #     check+=1
   
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
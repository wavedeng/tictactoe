import pygame as pg
import os,time
import ai
from pygame.locals import *
import random


BOARD_W = 600
BOARD_H = 600
TILE_W = BOARD_W/3
TILE_H = BOARD_H/3


pg.init()
pg.font.init()
WINDOW = pg.display.set_mode((BOARD_W,BOARD_H))
pg.display.set_caption("美丽的井字棋")

WINDOW.fill((0,0,0))

NUMBER_FONT = pg.font.Font("C:\Windows\Fonts\STXIHEI.TTF",60)
FILL_SOUND = pg.mixer.Sound("./assets/audios/punch.wav")

AI = True


def main():
    clock = pg.time.Clock()
    now_turn = False

    board = initBoard()
    # mouse_pos = None
    active_pile = None

    finished = False
    winner = None

    first = True



    while True:
        clock.tick(30)
        left_click = False
        right_click = False

        if finished:
            board = initBoard()
            finished = False
            now_turn = False
            first = True

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                quit()
                break
            
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = event.pos 

                if(event.button == 1):
                    if finished:
                        board = initBoard()
                        finished = False
                        first = True
                        now_turn = False
                    else:
                        left_click = True
                elif(event.button == 3):
                    right_click = True


        if(now_turn and left_click):
            suc = fillTile("O",mouse_pos,board)
            if suc:
                now_turn = not now_turn
        elif(not now_turn and right_click):
            suc = fillTile("X",mouse_pos,board)
            if suc:
                now_turn = not now_turn

        if(AI):
            if first:
                ai_x = random.randint(0,2)
                ai_y = random.randint(0,2)
                first = False
                print("executed")
            else:
                ai_x,ai_y = ai.next_move(board,now_turn)
            if(ai_x != None):
                if now_turn:
                    board[ai_y][ai_x] = "O"
                else:
                    board[ai_y][ai_x] = "X"

                now_turn = not now_turn            


        winner = checkWin(board)

        if winner:
            finished = True

        WINDOW.fill((0,0,0))

        if(finished):
            drawWin(winner)
        else:
            drawBoard(board)

        pg.display.update()

def checkWin(board):
    for i in range(3):
        if(board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '.'):
            return board[i][0]
    
    for i in range(3):
        if(board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '.'):
            return board[0][i]

    if(board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0]!='.'):
        return board[0][0]
    
    if(board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1]!='.'):
        return board[1][1]

    full = True

    for y in range(len(board)):
        for x in range(len(board[y])):
            if(board[y][x]=='.'):
                full = False

    if(full):
        return "没人"
    else:
        return None



def fillTile(char,pos,board):
    x,y = getTileFromPos(pos)
    if(board[y][x]=='.'):
        board[y][x] = char
        pg.mixer.Sound.play(FILL_SOUND)
        return True
    else:
        return False


def drawText(text,x,y,font,color):
    text = font.render(text,True,color)
    rect = text.get_rect()
    rect.centerx = x
    rect.centery = y
    WINDOW.blit(text,rect)


def drawWin(winner):
    drawText(winner+" 赢了!!",BOARD_W/2,BOARD_H/2,NUMBER_FONT,(255,255,255))

def drawBoard(board):
    for i in range(2):
        pg.draw.line(WINDOW,(255,255,255),(TILE_W*(i+1),0),(TILE_W*(i+1),BOARD_H),4)

    for i in range(2):
        pg.draw.line(WINDOW,(255,255,255),(0,TILE_H*(i+1)),(BOARD_W,TILE_H*(i+1)),4)

    span_offset = 60

    for y in range(len(board)):
        for x in range(len(board[y])):
            char = board[y][x]

            if(char == "X"):
                pg.draw.line(WINDOW,(255,255,255),(TILE_W*x+span_offset,TILE_H*y+span_offset),(TILE_W*(x+1)-span_offset,TILE_H*(y+1)-span_offset),7)
                pg.draw.line(WINDOW,(255,255,255),(TILE_W*x+span_offset,TILE_H*(y+1)-span_offset),(TILE_W*(x+1)-span_offset,TILE_H*y+span_offset),7)
            elif(char == "O"):
                pg.draw.circle(WINDOW,(255,255,255),(int(TILE_W*x+TILE_W/2),int(TILE_H*y + TILE_H/2)),50,4)


def getTileFromPos(pos):
    x = pos[0]
    y = pos[1]

    tile_x = 0
    tile_y = 0

    for i in range(3):
        if(x<(i+1)*TILE_W):
            tile_x = i
            break

    for i in range(3):
        if(y<(i+1)*TILE_H):
            tile_y = i
            break
    return tile_x,tile_y



def initBoard():
    return [
        ['.','.','.'],
        ['.','.','.'],
        ['.','.','.']
    ]


if __name__ == "__main__":
    main()
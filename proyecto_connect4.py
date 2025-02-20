import numpy as np
import pygame
import sys
import math


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED= (255, 0, 0)
BLUE= (0, 0, 255)
YELLOW=(255, 255, 0)

Row_count=6
Column_count=7

def create_board():
    board= np.zeros((Row_count, Column_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(Row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))
    
def win(board, piece):
     # buscar localizacion horizontal ganadora
     for c in range(Column_count -3):
         for r in range (Row_count):
             if board[r][c] == piece and board [r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                 return True
    # buscar localizacion vertical ganadora
     for c in range(Column_count):
         for r in range (Row_count -3):
             if board[r][c] == piece and board [r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                 return True
    # buscar posicion en diagonal positiva
     for c in range(Column_count-3):
         for r in range (Row_count -3):
             if board[r][c] == piece and board [r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                 return True
             
    # buscar posicion en diagonal negativa
     for c in range(Column_count-3):
         for r in range (3, Row_count):
             if board[r][c] == piece and board [r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                 return True

def draw_board(board):
    for c in range (Column_count):
        for r in range (Row_count):
            pygame.draw.rect(screen,GREEN, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c] ==0:
                pygame.draw.circle(screen, BLACK,(int (c*SQUARESIZE+SQUARESIZE/2),int( r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, BLUE,(int (c*SQUARESIZE+SQUARESIZE/2),height - int( r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, RED,(int (c*SQUARESIZE+SQUARESIZE/2), height - int( r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()        

board= create_board()
print_board (board)

game_over= False

turn= 0

pygame.init()

SQUARESIZE = 100

width= Column_count * SQUARESIZE
height= (Row_count+1) * SQUARESIZE

size= (width, height)

RADIUS= int(SQUARESIZE/2 - 5)

screen= pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            
            #Preguntar jugador1
            if turn ==0:
                posx= event.pos[0]
                col= int(math.floor(posx/SQUARESIZE))
                #col = int(input("Escoge posicion jugador 1 (0-6):"))
                
                if is_valid_location(board, col):
                    row=get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                    
                    if win (board, 1):
                        print("Has perdido jugador 2, PRINGAOOO!!")
                        game_over = True
                
            #preguntar jugador 2
            else:
                posx= event.pos[0]
                col= int(math.floor(posx/SQUARESIZE))
                #col = int(input("Escoge posicion jugador 2 (0-6):"))
                
                if is_valid_location(board, col):
                    row=get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                    
                    if win (board, 1):
                        print("Has perdido jugador 1, PRINGAOOO!!")
                        game_over = True
            
            print_board(board)
            draw_board (board)
            
            turn +=1
            turn = turn % 2
    

        
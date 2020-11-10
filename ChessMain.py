"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object
"""
# import os
# import sys
# os.chdir(sys.path[0])
# thank adam ^^^^
import os

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 400
# CAN CHANGE TO 512
DIMENSION = 8
# Dimensions of a chess board are 8x8
SQ_Size = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called once in the main 
'''


def loadImages():
    # could do "IMAGES['wp'] = p.image.load("images/wp.png")"
    # this for all 16 pieces but would be very redundant
    # do the following instead
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(os.path.join('images', piece + '.png')), (SQ_Size, SQ_Size))
    # Note: we can access an image by saying 'IMAGES['wp']'
    # Needs directory + filename - not just filename --> filepath then piecename


'''
The main driver for our code. This will handle user input and updating the graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    # initializes GameState (in Chess Engine.py) - initialize construction of pieces and creates the 3 variables
    print(gs.board)
    loadImages()  # only do this once, b4 the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()


'''
Responsible for all graphics within a current game state
'''


def drawGameState(screen, gs):
    drawBoard(screen)  # draws squares on board
    # add in piece highlighting or move suggestions
    drawPieces(screen, gs.board)  # draw pieces on top of the squares
    # order matters here - draw board before pieces. If you draw them the other way - creates board on top of pieces
    # - you wont see pieces


'''
Draw the square on the board.
'''
'''
Top left square on a board is always light
'''


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_Size, r * SQ_Size, SQ_Size, SQ_Size))


# Draw the pieces on the board using the current GameState.board

def drawPieces(screen, board):
    pass


if __name__ == "__main__":
    main()

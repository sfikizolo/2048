import pygame
from GeneratePieces import initializeVariables
pygame.init()


def pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color =initializeVariables.colors['light text']
            else:
                value_color =initializeVariables.colors['dark text']
            if value <= 2048:
                color =initializeVariables.colors[value]
            else:
                color = initializeVariables.colors['other']
            pygame.draw.rect(initializeVariables.screen,color , [j * 145 + 20, i * 145  +20,125,125],0,5)
            if value > 0 :
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 58 - (6*value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 145 + 75,i * 145 + 75))
                initializeVariables.screen.blit(value_text,text_rect)
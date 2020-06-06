import pygame

from snake_game import colors

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 10

def draw_block(screen, color, position):
    # position 위치에 color 색깔의 블록을 그린다.
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

def draw_background(screen):
    # 배경 그리기
    rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, colors.WHITE, rect)
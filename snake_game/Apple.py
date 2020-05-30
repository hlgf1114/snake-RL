from snake_game import colors
from snake_game import Util

class Apple:
    color = colors.RED

    def __init__(self, position=(5, 5)):
        # 사과의 위치
        self.position = position

    def draw(self, screen):
        # 사과를 화면에 그린다
        Util.draw_block(screen, self.color, self.position)
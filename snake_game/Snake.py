from snake_game import colors
from snake_game import Util

class Snake:
    color = colors.GREEN

    def __init__(self):

        # 뱀의 위치
        self.positions = [(9,6),(9,7),(9,8)]
        self.direction = 'west' # 뱀의 방향

    def draw(self, screen):
        # 뱀 그리기
        for position in self.positions:
            Util.draw_block(screen, self.color, position)

    def crawl(self):
        # 뱀이 현재 방향으로 한 칸 기어간다.
        head_position = self.positions[0]

        y, x = head_position
        if self.direction == 'north':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'south':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'west':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'east':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def turn(self, direction):
        if self.direction == 'north' and direction == 'south':
            self.direction = self.direction
        elif self.direction == 'south' and direction == 'north':
            self.direction = self.direction
        elif self.direction == 'west' and direction == 'east':
            self.direction = self.direction
        elif self.direction == 'east' and direction == 'west':
            self.direction = self.direction
        else:
            self.direction = direction

    def grow(self):
        # 뱀이 자라나게 한다
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'north':
            self.positions.append((y - 1, x))
        elif self.direction == 'south':
            self.positions.append((y + 1, x))
        elif self.direction == 'west':
            self.positions.append((y, x - 1))
        elif self.direction == 'east':
            self.positions.append((y, x + 1))
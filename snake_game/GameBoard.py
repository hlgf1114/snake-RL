from snake_game import Apple
from snake_game import Snake
from snake_game import Collision
from snake_game import Util

import random

class GameBoard:
    # 게임판 너비
    width = 20
    # 게임판 높이
    height = 20

    def __init__(self):
        self.snake = Snake.Snake()
        self.apple = Apple.Apple()
        self.REWARD_NOTHING = -1
        self.REWARD_GET_APPLE = 5
        self.REWARD_COLLIDE = -10
        self.wall = Util.SCREEN_HEIGHT / Util.BLOCK_SIZE

    def initialization(self):
        del self.snake
        del self.apple
        self.snake = Snake.Snake()
        self.apple = Apple.Apple()

    def draw(self, screen):
        # 화면에 게임판의 구성요소를 그린다.
        self.apple.draw(screen)
        self.snake.draw(screen)

    def put_new_apple(self):
        self.apple = Apple.Apple((random.randint(0, 19), random.randint(0, 19)))
        for position in self.snake.positions:
            if self.apple.position == position:
                self.put_new_apple()
                break

    def process_turn(self):

        reward = self.REWARD_NOTHING
        done = False

        # 뱀 기어가기
        self.snake.crawl()

        # 뱀이 자신과 충돌 했을 경우
        if self.snake.positions[0] in self.snake.positions[1:]:
            # 뱀 충돌 예외
            done = True
            reward = self.REWARD_COLLIDE
            return done, reward

        # 뱀이 밖으로 나갔을 경우
        if self.snake.positions[0][0] >= self.wall or self.snake.positions[0][1] >= self.wall or \
                self.snake.positions[0][0] < 0 or self.snake.positions[0][1] < 0:
            done = True
            reward = self.REWARD_COLLIDE
            return done, reward

        # 뱀의 머리와 사과가 닿았다면
        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()
            self.put_new_apple()
            reward = self.REWARD_GET_APPLE
            return done, reward

        return done, reward

import pygame
from datetime import datetime
from datetime import timedelta

from snake_game import Util
from snake_game import GameBoard
from snake_game import colors
from snake_game import Collision


class Environment:

    DIRECTION_ON_KEY = {
        pygame.K_UP: 'north',
        pygame.K_DOWN: 'south',
        pygame.K_LEFT: 'west',
        pygame.K_RIGHT: 'east',
    }

    DIRECTION_ON_KEY_AGENT = {
        0 : 'north',
        1 : 'south',
        2 : 'west',
        3 : 'east',
    }

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Util.SCREEN_WIDTH, Util.SCREEN_HEIGHT))
        self.last_turn_time = datetime.now()
        self.TURN_INTERVAL = timedelta(seconds=1)  # ❶ 게임 진행 간격을 0.3초로 정의한다
        self.game_board = GameBoard.GameBoard()
        # 보상
        self.REWARD_NOTHING = -1
        self.REWARD_GET_APPLE = 5
        self.REWARD_COLLIDE = -10

        self.step = 0
        self.max_step = 1000

        self.reward = self.REWARD_NOTHING
        self.done = False

    def init(self):
        self.reward = self.REWARD_NOTHING
        self.done = False
        self.step = 0
        # 게임 초기화
        self.game_board.initialization()
        return pygame.surfarray.array3d(pygame.display.get_surface())

    def update(self):
        pygame.display.update()

    def move(self, action):

        if self.step > self.max_step:
            self.state = pygame.surfarray.array3d(pygame.display.get_surface())
            self.done = True
            self.reward = self.REWARD_COLLIDE
            return self.state, self.reward, self.done

        #if self.TURN_INTERVAL < datetime.now() - self.last_turn_time:
        #   return self.state, self.reward
        
        # 컴퓨터가 알아서 해줌
        pygame.event.pump()

        self.reward = self.REWARD_NOTHING
        self.done = False

        # 발생할 이벤트 목록을 읽어들인다
        # 이벤트 목록을 순회하며 각 이벤트를 처리한다
        self.game_board.snake.turn(self.DIRECTION_ON_KEY_AGENT[action])
        
        # 시간이 지나면 움직임
        #if self.TURN_INTERVAL < datetime.now() - self.last_turn_time:

        self.done, self.reward = self.game_board.process_turn()
        self.last_turn_time = datetime.now()

        Util.draw_background(self.screen)
        self.game_board.draw(self.screen)
        self.update()
        # 반환값 주기
        self.state = pygame.surfarray.array3d(pygame.display.get_surface())
        self.step += 1
        return self.state, self.reward, self.done
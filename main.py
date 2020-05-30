from snake_game import game
import img
import agent
import pygame
import time
import img
import numpy as np

def main():

    env = game.Environment()
    network = agent.Agent()
    
    # 게임 초기화
    state = env.init()
    state = img.img_resize(state)

    max_step = 1000001
    total_episodes = 50000
    episode = 0
    total_reward = 0
    total_step = 0

    win_count = 0
    loose_count = 0

    while episode < total_episodes:
        step = 0
        while step <= max_step:

            # 행동 선택
            action = network.select_action(state)

            # 그에 맞는 다음 상태와 보상 및 끝
            next_state, reward, done = env.move(np.argmax(action))
            next_state = img.img_resize(next_state)

            # 트레이닝
            network.train_dqn(state, action, next_state, env, reward)

            if total_step % 10000 == 0:
                network.model_save('snake')

            if total_step % 100 == 0:
                network.copy_network()

            env.update()

            step += 1
            total_step += 1
            total_reward += reward
            state = next_state

if __name__ == '__main__':
    main()
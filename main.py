from snake_game import game
import img
import agent
import stacking
import pygame
import random
import time
import img
import numpy as np
def main():

    env = game.Environment()
    network = agent.Agent()
    stack = stacking.Stack()

    max_step = 100
    total_episodes = 50000
    episode = 0
    total_reward = 0
    total_step = 0

    win_count = 0
    loose_count = 0

    init_num = 0

    while episode < total_episodes:
        # 게임 초기화
        state = env.init()
        state = img.img_resize(state)
        # 스택 넣어줌
        for i in range(stack.stackingNum * stack.stakingSkip):
            stack.state_set.append(state)

        while True:


            stacked_state = stack.skip_and_stack_frame(state)
            # 행동 선택
            action = network.select_action(stacked_state)

            # 그에 맞는 다음 상태와 보상 및 끝
            next_state, reward, done = env.move(np.argmax(action))
            next_state = img.img_resize(next_state)
            next_stacked_state = stack.skip_and_stack_frame(next_state)

            # 트레이닝
            network.train_dqn(stacked_state, action, next_stacked_state, done, reward)

            if total_step % 2000 == 0:
                network.model_save('snake')

            if total_step % 5 == 0:
                network.copy_network()

            init_num += 1
            total_step += 1
            total_reward += reward
            stacked_state = next_stacked_state
            if done:
                break



            #if total_step % 20 == 0:
            #    print("episode = {} total_step = {} total_reward = {} epsilon = {}".format(episode, total_step, total_reward, network.epsilon))
        print("episode = {} total_step = {} total_reward = {} epsilon = {}".format(episode, total_step, total_reward,
                                                                                   network.epsilon))
        episode += 1
if __name__ == '__main__':
    main()
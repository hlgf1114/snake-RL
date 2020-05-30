from keras.models import Sequential
from keras.optimizers import SGD
from keras.layers import Dense, Flatten, Conv2D
import numpy as np
import random
import tensorflow as tf

import os


class Agent:

    def __init__(self):

        self.epsilon = 1
        self.final_epsilon = 0
        self.learning_rate = 0.1
        self.gamma = 0.9

        # 두 개의 신경망을 생성
        self.main_network = self.make_network()
        self.target_network = self.make_network()

        # 메인 신경망의 가중치를 타깃 신경망의 가중치로 복사
        self.copy_network()

    def model_save(self, name):

        self.copy_network()
        if not (os.path.isdir('model')):
            os.mkdir('model')
        self.model.save_weights('model/' + name + '_model.h5')
        print('model ' + name + ' saved.')

    def model_load(self, name):
        self.model.load_weights('model/' + name + '_model.h5')
        print(name + ' model weights loaded')

        # 신경망 생성

    def custom_loss_function(self, y_actual, y_predicted):
        loss = tf.reduce_mean(tf.square(y_predicted - y_actual))
        return loss

    def make_network(self):
        self.model = Sequential()
        self.model.add(Conv2D(16, (8, 8), padding='same', activation='relu', input_shape=(80, 80, 1)))
        self.model.add(Conv2D(32, (4, 4), padding='same', activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(128))
        self.model.add(Dense(32))
        self.model.add(Dense(4))
        print(self.model.summary())

        self.model.compile(optimizer='adam', loss=self.custom_loss_function, metrics=['mse'])
        return self.model

    def copy_network(self):
        self.target_network.set_weights(self.main_network.get_weights())

    def select_action(self, state):

        action = np.zeros(4)

        # 무작위 행동
        if random.random() < self.epsilon:
            # 원 핫 인코딩
            action_index = random.randint(0, 3)
            action[action_index] = 1
        # 예측
        else:
            state = np.array([state], dtype=np.float32).astype(np.float32)
            q_values = self.main_network.predict(state)
            action_index = np.argmax(q_values)
            action[action_index] = 1

        # 엡실론 프로세스
        if self.epsilon > self.final_epsilon:
            self.epsilon -= self.epsilon / 5000
        else:
            self.epsilon = self.final_epsilon

        return action

    def train_dqn(self, state_backup, action_backup, new_state, env, reward):

        x = np.array([state_backup], dtype=np.float32).astype(np.float32)
        q_values = self.main_network.predict(x)[0]

        # 게임이 종료됐을 때
        if env.done == True:
            q_values[np.argmax(action_backup)] += self.learning_rate * (reward - q_values[np.argmax(action_backup)])
            y = np.array([q_values], dtype=np.float32).astype(np.float32)
            self.main_network.fit(x, y, epochs=1, verbose=0)
        else:
            next_x = np.array([new_state], dtype=np.float32).astype(np.float32)
            next_q_values = self.target_network.predict(next_x)
            maxQ = np.max(next_q_values)
            q_values[np.argmax(action_backup)] += self.learning_rate * (reward + self.gamma * maxQ - q_values[np.argmax(action_backup)])

            # 생성된 오차 수정 데이터로 학습
            y = np.array([q_values], dtype=np.float32).astype(np.float32)
            self.main_network.fit(x, y, epochs=1, verbose=0)


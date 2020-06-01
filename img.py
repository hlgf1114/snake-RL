import numpy as np
import cv2
def img_resize(state):

    state_out = cv2.resize(state, (20, 20))
    state_out = cv2.cvtColor(state_out, cv2.COLOR_BGR2GRAY)
    state_out = np.reshape(state_out, (20, 20))
    state_out = np.reshape(state_out, (20, 20, 1))

    normalized =  (state_out - (255.0/2)) / (255.0/2)

    return normalized
import numpy as np
import cv2
import matplotlib.pyplot as plt
def img_resize(state):

    state_out = cv2.resize(state, (20, 20))
    state_out = cv2.cvtColor(state_out, cv2.COLOR_BGR2GRAY)

    normalized =  (state_out - (255.0/2)) / (255.0/2)
    return normalized
import numpy as np
import copy

def update(initial_checkerboard):
    tjw = copy.deepcopy(initial_checkerboard)
    temp = 0
    for i in range(3):
        for j in range(3):
            temp += 1
            tjw[i][j] = 0
    print(tjw)
    print(tjw)

initial_checkerboard = np.zeros((3, 3), dtype=int) #记录初始的棋盘状态
update(initial_checkerboard)

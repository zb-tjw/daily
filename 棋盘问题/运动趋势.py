import numpy as np

def find_element_around_zero(qipan, position):
    around_element = {} # 用游戏中的ASDW这四个符号代表左下右上

    if (position[0] == 0 and position[1] == 0):
        around_element['A'] = 0
        around_element['W'] = 0
        around_element['D'] = qipan[0][1]
        around_element['S'] = qipan[1][0]
    elif (position[0] == 0 and position[1] != 0):
        around_element['A'] = 0
        around_element['W'] = 0
        around_element['D'] = qipan[0][1]
        around_element['S'] = qipan[1][0]

    return around_element

def create_checkerboard(checkerboard):
    order = 0
    for i in range(3):
        for j in range(3):
            order += 1
            element = int(input("请输入第{}个数：".format(order)))
            checkerboard[i][j] = element


"""
两个棋盘做对比，自动得出棋子的运动趋势，来满足程序的健壮性，
可以满足不同情况，无需手动指定每个元素的运动趋势
"""
checkerboard = np.zeros((3, 3), dtype=int)#用作移动的棋盘
fianl_checkerboard = np.zeros((3, 3), dtype=int) #记录最终的棋盘状态

print("空棋盘如下：")
print(checkerboard)

print("请输入初始状态棋盘数据：")
create_checkerboard(checkerboard)

print("初始棋盘状态如下：")
print(checkerboard)

print("请输入终止状态棋盘数据：")
create_checkerboard(fianl_checkerboard)

print("最终棋盘状态如下：")
print(fianl_checkerboard)

"""
因numpy数据类型受限，所以运动趋势在外部自己创建
"""
sports_trend = {}
empty_position = []
for i in range(3):
    for j in range(3):
        key = checkerboard[i][j]
        if (checkerboard[i][j] == 0):
            empty_position = [i, j]
            continue
        position = np.argwhere(fianl_checkerboard == key)
        # 这里是获取到终止状态的位置
        horizontal_position = position[0][1]
        vertical_position = position[0][0]
        # print(key,position,end="\n")
        # print(horizontal_position,svertical_position,end="\n")
        tend = [0,0]
        if i < vertical_position:
            tend[0] = -1
        if i > vertical_position:
            tend[0] = 1

        if j < horizontal_position:
            tend[1] = 1
        if j > horizontal_position:
            tend[1] = -1
        sports_trend[key] = tend

# print(empty_position)
# print(sports_trend)

#######################################################
# 以上是前期准备工作
# 根据棋盘的起始和终止状态求出每个元素的初始运动趋势
#######################################################

around_element = find_element_around_zero(checkerboard, empty_position)
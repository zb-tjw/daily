import numpy as np
import copy

"""
1. 空洞用数字0表示，其他各个位置用1...8表示
2. 同一层deep都一样，所以直接不考虑
3. 注意深浅拷贝问题
4. 注意闭包问题
5. 注意stack不是栈，是队列queue，temp是step代表步数，懒得改了
6.是用那个规则：输入初始和最终棋盘元素，横着从左到右挨着输入，空洞为0，其他为1...8
"""

final_checkerboard = np.zeros((3, 3), dtype=int)  # 记录最终的棋盘状态
min_element_number = 0
total_stack = []
final_stack = []
mid_stack = []
temp = 0

def create_checkerboard(checkerboard):
    order = 0
    for i in range(3):
        for j in range(3):
            order += 1
            element = int(input("请输入第{}个数：".format(order)))
            checkerboard[i][j] = element

def move_checkerboard(before_state):
    # result = [] # 用来存储符合条件，有进一步扩展的棋盘
    global mid_stack

    # 首先确定空洞的位置
    position = np.argwhere(before_state == 0)
    first_position = position[0][0]
    second_position = position[0][1]

    # print(first_position) # 打印检测空洞位置是否正确拿到
    # print(second_position)

    if first_position == 0:
        if second_position == 0:
            zuoyi(before_state, first_position, second_position, mid_stack)
            shangyi(before_state, first_position, second_position, mid_stack)
        elif second_position == 2:
            youyi(before_state, first_position, second_position, mid_stack)
            shangyi(before_state, first_position, second_position, mid_stack)
        else:
            youyi(before_state, first_position, second_position, mid_stack)
            zuoyi(before_state, first_position, second_position, mid_stack)
            shangyi(before_state, first_position, second_position, mid_stack)
    elif first_position == 2:
        if second_position == 0:
            xiayi(before_state, first_position, second_position, mid_stack)
            zuoyi(before_state, first_position, second_position, mid_stack)
        elif second_position == 2:
            youyi(before_state, first_position, second_position, mid_stack)
            xiayi(before_state, first_position, second_position, mid_stack)
        else:
            youyi(before_state, first_position, second_position, mid_stack)
            xiayi(before_state, first_position, second_position, mid_stack)
            zuoyi(before_state, first_position, second_position, mid_stack)
    else:
        if second_position == 0:
            zuoyi(before_state, first_position, second_position, mid_stack)
            xiayi(before_state, first_position, second_position, mid_stack)
            shangyi(before_state, first_position, second_position, mid_stack)
        elif second_position == 2:
            xiayi(before_state, first_position, second_position, mid_stack)
            youyi(before_state, first_position, second_position, mid_stack)
            shangyi(before_state, first_position, second_position, mid_stack)
        else:
            youyi(before_state, first_position, second_position, mid_stack)
            xiayi(before_state, first_position, second_position, mid_stack)
            zuoyi(before_state, first_position, second_position, mid_stack)
            shangyi(before_state, first_position, second_position, mid_stack)

    return mid_stack

def equal_all_position(first_checkerboard):
    for t in total_stack:
        num = 0
        for i in range(3):
            for j in range(3):
                if first_checkerboard[i][j] == t[i][j]:
                    num += 1
        if num == 9:
            return 0
        else:
            pass

        return 1


def shangyi(checkerboard, first_position, second_position, stack):
    after_state = copy.deepcopy(checkerboard)
    after_state[first_position][second_position] = after_state[first_position + 1][second_position]  # 数字上移
    after_state[first_position + 1][second_position] = 0
    tap = equal_all_position(after_state)
    if tap:
        number = statistics(after_state)
        ruzhan(after_state, stack, number)

def xiayi(checkerboard, first_position, second_position, stack):
    after_state = copy.deepcopy(checkerboard)
    after_state[first_position][second_position] = after_state[first_position -1][second_position]  # 数字下移
    after_state[first_position - 1][second_position] = 0
    tap = equal_all_position(after_state)
    if tap:
        number = statistics(after_state)
        ruzhan(after_state, stack, number)

def zuoyi(checkerboard, first_position, second_position, stack):
    after_state = copy.deepcopy(checkerboard)
    after_state[first_position][second_position] = after_state[first_position][second_position + 1]  # 数字左移
    after_state[first_position][second_position + 1] = 0
    tap = equal_all_position(after_state)
    if tap:
        number = statistics(after_state)
        ruzhan(after_state, stack, number)

def youyi(checkerboard, first_position, second_position, stack):
    after_state = copy.deepcopy(checkerboard)
    after_state[first_position][second_position] = after_state[first_position][second_position - 1]  # 数字右移
    after_state[first_position][second_position - 1] = 0
    tap = equal_all_position(after_state)
    if tap:
        number = statistics(after_state)
        ruzhan(after_state, stack, number)

def ruzhan(checkerboard, stack, number):
    global min_element_number
    print("len(stack)=",len(stack))
    print("min_element_number=",min_element_number)
    if len(stack) == 0:
        stack.append(checkerboard)
        total_stack.append(checkerboard)
        min_element_number = number
        print(checkerboard)
    else:
        if number > min_element_number:
            print(checkerboard)
            print("未插入")
            pass
        elif number == min_element_number:
            stack.append(checkerboard)
            total_stack.append(checkerboard)
            min_element_number = number
            print(checkerboard)
        elif number < min_element_number:
            stack = []
            stack.append(checkerboard)
            total_stack.append(checkerboard)
            min_element_number = number
            print(checkerboard)

    print("number=",number)
    print("====================")
    return stack

# 用来统计当前棋盘有多少个元素不在目标位置
def statistics(checkboard):
    number = 0

    for i in range(3):
        for j in range(3):
            if checkboard[i][j] == final_checkerboard[i][j]:
                number += 1

    if number == 9:
        print("最终结果为：")
        print(checkboard)
        exit()
    return 9 - number

def iterator_all_elements(final_stack):
    temp_stack = []

    global temp
    for i in final_stack:
        checkerboard_list = move_checkerboard(i)
        total_stack.append(checkerboard_list)
        if temp >= 2:

            pass
        for j in checkerboard_list:
            temp_stack.append(j)

    return temp_stack

def main():
    initial_checkerboard = np.zeros((3, 3), dtype=int) #记录初始的棋盘状态

    print("空棋盘如下：")
    print(initial_checkerboard)

    print("请输入初始状态棋盘数据：")
    create_checkerboard(initial_checkerboard)

    print("初始棋盘状态如下：")
    print(initial_checkerboard)

    print("请输入终止状态棋盘数据：")
    create_checkerboard(final_checkerboard)

    print("最终棋盘状态如下：")
    print(final_checkerboard)
    print("-------------------")

    # number = statistics(initial_checkerboard)
    # if number == 0:
    #     print("初始状态即为最终状态，无需移动棋盘，棋盘信息如下：")
    #     print(initial_checkerboard)
    #     exit()

    statistics(initial_checkerboard)

    global final_stack
    global min_element_number
    global mid_stack
    mid_checkerboard = copy.deepcopy(initial_checkerboard)
    final_stack.append(mid_checkerboard)
    total_stack.append(mid_checkerboard)
    global temp
    while(len(final_stack) != 0 and temp < 2):
        temp += 1
        mid_stack = iterator_all_elements(final_stack)
        min_element_number = 0
        final_stack = copy.deepcopy(mid_stack)
        mid_stack = []
        print(final_stack)
        print("///////////////////////")

    # final_stack = iterator_all_elements(final_stack)
    # print(final_stack)


if __name__ == '__main__':
    main()
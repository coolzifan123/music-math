from map import mapindex
import numpy as np


huanlesong = ['3', '3', '4', '5', '5', '4', '3', '2', '1', '1', '2', '3',
              '3', '2', '2', '3', '3', '4', '5', '5', '4', '3', '2',
              '1', '1', '2', '3', '2', '1', '1', 'm7', 'm7', '1', 'm6',
              'm7', '1', '2', '1', 'm6', 'm7', '1', '2', '3', '2', '1', '2', 'm5', '1',
              '1', '1', '1', '1', '1', '1', '1', '1', 'm6', 'm5', 'm5', 'm5', '1', 'm7', '1', '1',
              '1', '1', '2', '3', '3', '2', '1', 'm7', 'm5', 'm5', 'm5', '1', '1', 'm7', 'm7',
              '1', '1', '2', '3', '3', '2', '1', 'm7', 'm5', 'm5', 'm5', '1', '1', 'm6', 'm7', '1', '1',
              'm5', 'm5', 'm5', 'm3', 'm5', 'm5', 'm5', 'm3', 'm5', 'm5', 'm6b', 'm5', 'm6', 'm6b', 'm5b', 'm5', 'm5',
              'm5', 'm5', 'm6', 'm7b', 'm7b', 'm6', 'm5', 'm6', 'm4', 'm5', 'm5', 'm4', 'm5', 'm5', 'm4', 'm3', 'm4',
              'm4', 'm5', 'm6', 'm7', '1', '1']
# 输入为一个list
def get_markov_matrix(puzi):
    matrix = np.zeros((36, 36))
    for i in range(len(puzi) - 1):
        index_1 = mapindex[puzi[i]]
        index_2 = mapindex[puzi[i+1]]
        matrix[index_1][index_2] += 1

    for i in range(36):
        if matrix[i].sum() == 0:
            continue
        matrix[i] = matrix[i]/matrix[i].sum()

    return matrix


# 输入为多个谱子
def get_markov_matrix_list(puzis):
    matrix = np.zeros((36, 36))
    for puzi in puzis:
        for i in range(len(puzi) - 1):
            index_1 = mapindex[puzi[i]]
            index_2 = mapindex[puzi[i+1]]
            matrix[index_1][index_2] += 1

    for i in range(36):
        if matrix[i].sum() == 0:
            continue
        matrix[i] = matrix[i]/matrix[i].sum()

    return matrix

#输入为初始音符， 转移矩阵，长度
def get_markov_index_list(init_index, matrix, num):
    if matrix[init_index].sum() == 0:
        return None
    index = [i for i in range(36)]
    res_list = []
    seed = init_index
    for i in range(num):
        res = np.random.choice(index, 1, p=matrix[seed])
        res_list.append(res[0])

    return np.array(res_list)

matrix = get_markov_matrix(huanlesong)
# print(matrix)
OdeToJoy_res = get_markov_index_list(12, matrix, 40)


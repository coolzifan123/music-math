import numpy as np
from codes.map import mapindex
import itertools
from sklearn import preprocessing
import pygame
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


# 基础的操作是随机音符长度
def sample_time():
   time_sq = np.array([0.125,0.25,0.5,0.75,1,1.25,1.5,1.75,2])
   # 时长概率分布可以调整
   prob = np.array([0.1, 0.15, 0.3, 0.1,0.15,0.05,0.05,0.05,0.05])
   timelen = np.random.choice(a=time_sq, p=prob)
   return timelen


# 高阶马尔可夫链类
class HighOrderMarkov(object):
    """
    高阶马尔科夫链
    """

    def __init__(self, puzis, n_states, order):
        """
        puzis: 输入单个或多个乐谱
        n_states: 状态数量
        order: 马尔科夫模型的阶数
        """
        self.number_of_states = n_states
        self.order = order
        self.puzis = puzis

        # 生成n阶所有可能状态
        self.possible_states = {
            j: i for i, j in
            enumerate(itertools.product(range(self.number_of_states), repeat=self.order))
        }

        # 初始化n阶转移概率矩阵
        self.transition_matrix = np.zeros(
            (len(self.possible_states), self.number_of_states)
        )

    def map_to_index(self):
        """
        将单个或多个乐谱转化为对应的序号
        """
        try:
            puzis_index = []
            for puzi in self.puzis:
                puzi_index = [mapindex[i] for i in puzi]
                puzis_index.append(puzi_index)
        except KeyError:  # 单个乐谱的情况
            puzis_index = []
            puzis_index.append([mapindex[i] for i in self.puzis])
        finally:
            return puzis_index

    def normalize_transitions(self):
        """
        对状态转移矩阵的每一行归一化
        """
        self.transition_matrix = preprocessing.normalize(
            self.transition_matrix, norm="l1"
        )

    def update_transition_matrix(self, states_sequence, normalize=True):
        """
        输入单个状态序列(单个谱子), 更新状态转移矩阵
        """
        visited_states = [
            states_sequence[i: i + self.order]
            for i in range(len(states_sequence) - self.order + 1)
        ]

        for state_index, state in enumerate(visited_states):
            try:
                self.transition_matrix[
                    self.possible_states[tuple(state)],
                    states_sequence[state_index + self.order]
                ] += 1
            except IndexError:
                pass

        if normalize:
            self.normalize_transitions()

    def fit(self):
        """
        输入单个或多个乐谱序列, 更新状态转移矩阵
        """
        state_sequences = self.map_to_index()
        for sequence in state_sequences:
            self.update_transition_matrix(sequence, normalize=False)
        self.normalize_transitions()

    def generate_markov_chains(self, init_index, num_steps):
        """
        根据初始状态随机生成高阶马尔科夫链
        init_state: 初始状态
        num_steps: 生成链的长度
        """
        if self.transition_matrix[self.possible_states[tuple(init_index)]].sum() == 0:
            return None
        index = [i for i in range(self.number_of_states)]
        output_chain = init_index.copy()
        for i in range(num_steps - self.order):
            seed = output_chain[i: i + self.order]
            next_index = np.random.choice(index, 1, p=self.transition_matrix[self.possible_states[tuple(seed)]])
            output_chain.append(next_index[0])
        return np.array(output_chain)

# 用python播放mid文件函数，也可以用播放器播放
def play_midi(file):
   freq = 44100
   bitsize = -16
   channels = 2
   buffer = 1024
   pygame.mixer.init(freq, bitsize, channels, buffer)
   pygame.mixer.music.set_volume(1)
   clock = pygame.time.Clock()
   try:
       pygame.mixer.music.load(file)
   except:
       import traceback
       print(traceback.format_exc())
   pygame.mixer.music.play()
   while pygame.mixer.music.get_busy():
       clock.tick(30)
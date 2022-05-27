from mido import Message, MidiFile, MidiTrack
from codes.map import mapindext,map0,mapt
import numpy as np
bpm = 60   # 节拍暂时设置为60
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# 考虑时值的欢乐颂谱子
huanlesong = ['3','3','4','5',    '5','4','3','2',    '1','1','2','3'    ,'32','20','21',   '3','3','4','5',    '5','4','3','2',    '1','1','2','3',    '22','10','11'   ,'2','2','3','1'
    ,'2','30','40','3','1'      ,'2','30','40','3','2'     ,'1','2','m5','3',     '3','3','4','5',      '5','4','3','2'   ,'1','1','2','3'   ,'22','10','11']


def get_markov_matrix(puzi):
   matrix = np.zeros((14, 14))
   for i in range(len(puzi) - 1):
      index_1 = mapindext[puzi[i]]
      index_2 = mapindext[puzi[i + 1]]
      matrix[index_1][index_2] += 1  # 生成转移矩阵

   for i in range(10):
      if matrix[i].sum() == 0:
         continue
      matrix[i] = matrix[i] / matrix[i].sum()

   return matrix


# 输入为初始音符， 转移矩阵，长度
def get_markov_index_list(init_index, matrix, num):
   if matrix[init_index].sum() == 0:
      return None
   index = [i for i in range(14)]
   res_list = []
   seed = init_index
   for i in range(num):
      res = np.random.choice(index, 1, p=matrix[seed])
      res_list.append(res[0])

   return np.array(res_list)

# 第一个为音符，第二个为音符长度
def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
   meta_time = 60 * 60 * 10 / bpm
   base_note = 60
   # track.append(Message('program_change', channel=0, program=42, time=0))
   track.append(Message('note_on', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   track.append(Message('note_off', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(meta_time*length), channel=channel))


# 用于含时值播放一个音符序列
def playSequence(track,sequence):
   length = len(sequence)
   for i in range(length):
      play_note(mapt[str(sequence[i])],3/map0[str(sequence[i])], track)

if __name__=='__main__':

   matrix = get_markov_matrix(huanlesong)
   # print(matrix)
   OdeToJoy_res = get_markov_index_list(6, matrix, 60)
   #OdeToJoy(track)'
   playSequence(track, OdeToJoy_res)
   mid.save('interval.mid')


from mido import Message, MidiFile, MidiTrack
from codes.map import mapindex
import numpy as np
from codes.utils import sample_time,HighOrderMarkov
from codes.puzi import huanlesong,lihuayoukaifang,molihua
bpm = 60   # 节拍暂时设置为60
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


# 第一个为音符，第二个为音符长度
def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
   meta_time = 60 * 60 * 10 / bpm
   base_note = 60
   # track.append(Message('program_change', channel=0, program=42, time=0))
   track.append(Message('note_on', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   track.append(Message('note_off', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(meta_time*length), channel=channel))


# 用于播放一个音符序列
def playSequence(track,sequence):
   length = len(sequence)
   for i in range(length):
      play_note(sequence[i], sample_time(), track)

if __name__=='__main__':
   """
   HighOrderMarkov()输入的三个变量分别为: 乐谱、状态个数、阶数
   """
   high_order_markov = HighOrderMarkov(molihua, 36, 2)
   high_order_markov.fit()

   """
   以init_index为开头随机生成步长为num_steps的序列
   无论一阶还是高阶, init_index都要以列表形式传入
   """
   init_index = [12, 12]
   # print(high_order_markov.transition_matrix)
   OdeToJoy_res = high_order_markov.generate_markov_chains(init_index, num_steps=40)

   #OdeToJoy(track)'
   playSequence(track, OdeToJoy_res)
   mid.save('high_order_stochastic.mid')


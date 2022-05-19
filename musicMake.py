from mido import Message, MidiFile, MidiTrack
from map import mapindex
import numpy as np
from puzi import OdeToJoy_res
bpm = 60   # 节拍暂时设置为60
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# 基础的操作是随机音符长度
def sample_time():
   time_sq = np.array([0.125,0.25,0.5,0.75,1,1.25,1.5,1.75,2])
   # 时长概率分布可以调整
   prob = np.array([0.1, 0.15, 0.3, 0.1,0.15,0.05,0.05,0.05,0.05])
   timelen = np.random.choice(a=time_sq, p=prob)
   return timelen

# 第一个为音符，第二个为音符长度
def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
   meta_time = 60 * 60 * 10 / bpm
   base_note = 60
   # track.append(Message('program_change', channel=0, program=42, time=0))
   track.append(Message('note_on', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   track.append(Message('note_off', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

# 以欢乐颂的一小段作为例子
def OdeToJoy(track):
   play_note(mapindex['3'], 0.5, track)
   play_note(mapindex['3'], 0.5, track)
   play_note(mapindex['4'], 0.5, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['4'], 0.5, track)
   play_note(mapindex['3'], 0.5, track)
   play_note(mapindex['2'], 0.5, track)
   play_note(mapindex['1'], 0.5, track)
   play_note(mapindex['1'], 0.5, track)
   play_note(mapindex['2'], 0.5, track)
   play_note(mapindex['3'], 0.5, track)
   play_note(mapindex['3'], 0.75, track)
   play_note(mapindex['2'], 0.25, track)
   play_note(mapindex['2'], 1.0, track)

# 用于播放一个音符序列
def playSequence(track,sequence):
   length = len(sequence)
   for i in range(length):
      play_note(sequence[i], sample_time(), track)

#OdeToJoy(track)'
playSequence(track,OdeToJoy_res)
mid.save('stochastic.mid')


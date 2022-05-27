from mido import Message, MidiFile, MidiTrack
from codes.map import mapindex
import numpy as np
from codes.utils import get_markov_index_list,get_markov_matrix,get_markov_matrix_list,sample_time
from codes.puzi import huanlesong,molihua
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

# 以茉莉花一小段为例
def molihua1(track):
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['2'], 0.25, track)
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['5'], 0.25, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['l1'], 0.25, track)
   play_note(mapindex['l1'], 0.25, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['5'], 0.25, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['5'], 1.0, track)
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['2'], 0.25, track)
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['5'], 0.25, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['l1'], 0.25, track)
   play_note(mapindex['l1'], 0.25, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['5'], 0.25, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['5'], 1.0, track)
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['5'], 0.25, track)
   play_note(mapindex['6'], 0.5, track)
   play_note(mapindex['6'], 0.25, track)
   play_note(mapindex['5'], 0.25, track)
   play_note(mapindex['5'], 1.0, track)
   play_note(mapindex['3'], 0.5, track)
   play_note(mapindex['2'], 0.25, track)
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['5'], 0.5, track)
   play_note(mapindex['3'], 0.25, track)
   play_note(mapindex['2'], 0.25, track)
   play_note(mapindex['1'], 0.5, track)
   play_note(mapindex['1'], 0.25, track)
   play_note(mapindex['2'], 0.25, track)
   play_note(mapindex['1'], 1.0, track)


# 用于播放一个音符序列
def playSequence(track,sequence):
   length = len(sequence)
   for i in range(length):
      play_note(sequence[i], sample_time(), track)
if __name__=='__main__':
   matrix = get_markov_matrix(molihua)
   np.savetxt('sample.csv', matrix, delimiter=",")
   OdeToJoy_res = get_markov_index_list(12, matrix, 40)
   playSequence(track,OdeToJoy_res)
   # molihua1(track)
   mid.save('molihua.mid')


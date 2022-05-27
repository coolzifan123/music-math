from mido import Message, MidiFile, MidiTrack
from codes.map import mapindex
import numpy as np
from codes.utils import get_markov_index_list,get_markov_matrix,get_markov_matrix_list,sample_time
from codes.puzi import jianpu
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
   to_combine = [jianpu[0], jianpu[2]]
   matrix = get_markov_matrix_list(jianpu)
   # print(matrix)
   seq = get_markov_index_list(14, matrix, 40)
   #OdeToJoy(track)'
   playSequence(track, seq)
   mid.save('stochastic.mid')


from mido import Message, MidiFile, MidiTrack
from puzi import note_dist
bpm = 60   # 节拍暂时设置为60
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
#    meta_time = 60 * 60 * 10 / bpm
#    major_notes = [0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1
#                   ]
#    base_note = 60
#    # track.append(Message('program_change', channel=0, program=42, time=0))
#    track.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
#    track.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
   meta_time = 60 * 60 * 10 / bpm
   base_note = 60
   # track.append(Message('program_change', channel=0, program=42, time=0))
   track.append(Message('note_on', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   track.append(Message('note_off', note=base_note + base_num*11 + note, velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

# 以欢乐颂的一小段作为例子
def OdeToJoy(track):
   play_note(note_dist['3'], 0.5, track)
   play_note(note_dist['3'], 0.5, track)
   play_note(note_dist['4'], 0.5, track)
   play_note(note_dist['5'], 0.5, track)
   play_note(note_dist['5'], 0.5, track)
   play_note(note_dist['4'], 0.5, track)
   play_note(note_dist['3'], 0.5, track)
   play_note(note_dist['2'], 0.5, track)
   play_note(note_dist['1'], 0.5, track)
   play_note(note_dist['1'], 0.5, track)
   play_note(note_dist['2'], 0.5, track)
   play_note(note_dist['3'], 0.5, track)
   play_note(note_dist['3'], 0.75, track)
   play_note(note_dist['2'], 0.25, track)
   play_note(note_dist['2'], 1.0, track)

# 接下来是两个示例函数
def verse(track):
   play_note(1, 0.5, track)       # 小
   play_note(2, 0.5, track)       # 时
   play_note(1, 1.5, track)       # 候
   play_note(7, 0.25, track, -1)  # 妈
   play_note(6, 0.25, track, -1)  # 妈

   play_note(5, 0.5, track, -1, channel=1)  # 对
   play_note(3, 0.5, track, channel=1)      # 我
   play_note(3, 2, track, channel=1)        # 讲

   play_note(3, 0.5, track)           # 大
   play_note(4, 0.5, track)
   play_note(3, 1.5, track)           # 海
   play_note(2, 0.25, track)          # 就
   play_note(1, 0.25, track)          # 是

   play_note(6, 0.5, track, -1, channel=1)  # 我
   play_note(2, 0.5, track, channel=1)      # 故
   play_note(2, 2, track, channel=1)        # 乡

   play_note(7, 0.5, track, -1)  # 海
   play_note(1, 0.5, track)
   play_note(7, 1.5, track, -1)  # 边
   play_note(6, 0.25, track, -1)
   play_note(5, 0.25, track, -1)

   play_note(5, 0.5, track, -1, channel=1)  # 出
   play_note(2, 0.5, track, channel=1)
   play_note(2, 2, track, channel=1)        # 生

   play_note(4, 1.5, track)       # 海
   play_note(3, 0.5, track)       # 里
   play_note(1, 0.5, track)       # 成
   play_note(6, 0.5, track, -1)

   play_note(1, 3, track)         # 长


def chorus(track, num):
   play_note(5, 0.5, track)  # 大
   play_note(6, 0.5, track)
   play_note(5, 1.5, track)  # 海
   play_note(3, 0.5, track)  # 啊

   play_note(5, 0.5, track, channel=1)  # 大
   play_note(6, 0.5, track, channel=1)
   play_note(5, 2, track, channel=1)    # 海

   play_note(6, 0.5, track)  # 是（就）
   play_note(5, 0.5, track)  # 我（像）
   play_note(4, 0.5, track)  # 生（妈）
   if num == 1:
       play_note(1, 0.25, track, channel=1) # 活
       play_note(1, 0.25, track, channel=1) # 的
   if num == 2:
       play_note(1, 0.5, track, channel=1)  # (妈)
   play_note(6, 0.5, track, channel=1)      # 地（一）
   play_note(5, 0.5, track, channel=1)

   play_note(5, 3, track, channel=1)        # 方（样）

   play_note(3, 0.5, track)  # 海（走）
   play_note(4, 0.5, track)  # 风（遍）
   play_note(3, 1.5, track)  # 吹（天）
   play_note(2, 0.25, track) # (涯)
   play_note(1, 0.25, track)

   play_note(6, 0.5, track, -1, channel=1)  # 海（海）
   play_note(2, 0.5, track, channel=1)      # 浪
   play_note(2, 2, track, channel=1)        # 涌（角）

   play_note(4, 0.5, track)              # 随（总）
   play_note(5, 0.5, track)              # 我（在）
   play_note(4, 0.5, track)              # 漂（我）
   play_note(3, 0.5, track)              # 流（的）
   play_note(1, 0.5, track, channel=1)   # 四（身）
   play_note(6, 0.5, track, -1, channel=1)

   play_note(1, 3, track, channel=1)     # 方（旁）

#verse(track)
OdeToJoy(track)
mid.save('OdeToJoy.midi')


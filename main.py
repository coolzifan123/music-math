import json

import numpy as np

from scipy.io.wavfile import write

import matplotlib.pyplot as plt

#----------------------定义合成器---------------------
def synthesizer(freq, duration, amp=1.0, sampling_freq=44100):

    t = np.linspace(0, duration, duration * sampling_freq)

    audio = amp * np.sin(2 * np.pi * freq * t)

    return audio.astype(np.int16)

if __name__=='__main__':

    tone_map_file = 'music.json'

    with open(tone_map_file, 'r') as f:

        tone_freq_map = json.loads(f.read())

        input_tone='G'

        duration = 2     # seconds

        amplitude = 10000

        sampling_freq = 44100    # Hz

# Tone-duration sequence

tone_seq = [('D', 1), ('G',1), ('C',1), ('A',1),

('B',1),('F',1),('A',1),('Gsharp',4),

('B',1),('F',1),('G',1),('Csharp',1),

('Dsharp',1),('Csharp',1),('Gsharp',1),('Asharp', 2),

('D', 1), ('G',1), ('C',1), ('A',1),

('B',3),('F',1),('G',1),('Csharp',1),

('Dsharp',3),('E',1),('Fsharp',1),('Asharp', 5)]

#-------------------------------------------------------------

tone_seq1 = [('E', 2), ('C',1), ('D',1), ('E',1),

('D',1),('C',1),('B',1),('A',1),

('C',0),('E',0),('Asharp',0),('G',0),

('G',0),('Asharp',1),('G',1),('F', 2),

('G', 1), ('Asharp',2), ('E',2),('E', 2),

('C',1), ('D',1), ('E',1),('D',1),('C',1),('B',1),

('A',1), ('A',1), ('B',3),('F',1),('G',1),('Asharp',1),

('Dsharp',3),('E',1),('Fsharp',1),('Asharp', 5)]

#---------------------------------------------------------------

# Construct the audio signal based on the chord sequence

output = np.array([])

for item in tone_seq:

    input_tone = item[0]

    duration = item[1]

    synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)

    output = np.append(output, synthesized_tone, axis=0)

#===============================================================

# Write to the output file

write('music1.wav', sampling_freq, output)

for item in tone_seq1:

    input_tone = item[0]

    duration = item[1]

    synthesized_tone = synthesizer(tone_freq_map[input_tone], duration, amplitude, sampling_freq)

    output = np.append(output, synthesized_tone, axis=0)

write('music2.wav', sampling_freq, output)

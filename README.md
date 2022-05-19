# 随便写
## 已完成
* 从简谱乐谱自动生成一阶马尔可夫矩阵。
* 实现python钢琴奏乐和作曲。
* 实现从一阶马尔可夫矩阵生成随机音乐。

## requirements
* python 3+
* numpy
* mido
* pygame

mido最重要


## 使用说明
直接运行musicMake.py可以得到一个mid文件（windows播放器就可以播放）

### map.py
内含音符到对应的索引，以一个半音作为间隔，例如m1代表C3，m2b代表bD3，1代表C4，l1代表C5，使用数字便于使用简谱作为输入。

### puzi.py
get_markov_matrix： 函数输入为乐谱，乐谱参照《欢乐颂》（huanlesong），输出为一阶马尔可夫转移矩阵.

get_markov_matrix_list: 输入为乐谱的list，输出为一阶马尔可夫转移矩阵。

get_markov_index_list：输入为起始音符索引转移矩阵和生成音乐的长度，输出为对应长度的生成的音乐索引序列，

### musicMake.py
sample_time: 可以随机采样时间，概率分布可以手动修改。

play_note：用于演奏一个音符，输入为音符对应索引，音符时长和track，使用方法具体见《欢乐颂》。

playSequence： 输入为track和音符序列，可以给track增加音符。

### 其他
PLAY.py可以用python播放指定的mid文件

OdeToJoy.mid是生成的欢乐颂样本，stochastic.mid是目前对应的随机音乐。





# HDMI-Video-Server-Based-On-PYNQ

switch没法直接用hdmi输出到电脑屏幕上就很烦，又不想买采集卡，于是有了这个想法。

这是用pynq读入hdmi视频信号后放到socket 服务端上，然后电脑通过网络来看视频信息。只要电脑能连局域网都能行！

理论上将只要pynq和电脑处于同一个局域网下，就能够在电脑上查看连入pynq的hdmi输出视频。
以后没有hdmi显示设备的时候可以拿电脑先看一下了。
还可以用pynq同时进行服务器视频输出和hdmi out。

## 内容介绍

带test的两个是我尝试socket功能时候用的，就互发一句会。

把ServerMain.ipynb和ServerOnPYNQ.py放在pynq的同一目录下并运行ServerMain.ipynb

然后pc上运行ClientOnPc.py就可以了。

如果静态ip或者端口不一样还可以修改一下。

baseOverlay用的自带的所以不必担心。
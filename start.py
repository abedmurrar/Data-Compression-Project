import lzw
import os
import plotly.plotly as py
import plotly.graph_objs as go
print "LZW"
inputf = lzw.readbytes('uncompressed.txt')
compressed = lzw.compress(inputf)
lzw.writebytes('compressed.lzw', compressed)
ratio = os.stat('uncompressed.txt').st_size/float(os.stat('compressed.lzw').st_size)
print "Compression Ratio : " ,ratio

os.system("python ./arithmetic/adaptive-arithmetic-compress.py uncompressed.txt compressed.bin")
ratio2 = os.stat('uncompressed.txt').st_size/float(os.stat('compressed.bin').st_size)
print "Adaptive Arithmetic coding"
print "Compression Ratio : " ,ratio2

labels = ['Lempel-Ziv','arithmetic']
values = [ratio,ratio2]
trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='abedmurrar15')
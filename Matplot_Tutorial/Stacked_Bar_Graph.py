# こちらはstacked barとerror barを使うサンプルです。
import numpy as np
import matplotlib.pyplot as plt

N = 5
menMeans = (20, 35, 30, 25, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N) # the x locations for the groups
width = 0.35 # the width of the bars: can also be len(x) sequence

# matplotlib.pyplot.bar
# - Make a bar plot.
# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
# # Parameters
#   x : sequence of scalars
#   height : scalar or sequence of scalars
#   width : scalar of array-like, optional
#   bottom : scalar or array-like, optional
#   align : {'center', 'edge'}, optional, default: 'center'
#           ・'center': Center the base on the x positions.
#           ・'edge': Align the left edges of the bars with the x positions.
p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

# matplotlib.pyplot.ylabel
# -	Set the label for the y-axis.
# matplotlib.pyplot.ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)
# # Parameters
#   label : str
plt.ylabel('Scores')

# matplotlib.pyplot.title
# - Set a title for the axes.
# matplotlib.pyplot.title(label, fontdict=None, loc='center', pad=None, **kwargs)
# # Parameters
#   label : str
plt.title('Scores by group and gender')

# matplotlib.pyplot.xticks
# - Get or set the current tick locations and labels of the x-axis.
# matplotlib.pyplot.xticks(ticks=None, labels=None, **kwargs)
# # Parameters
#   ticks : array_like
#   labels : array_like, optional
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))

# matplotlib.pyplot.yticks
# - Get or set the current tick locations and labels of the y-axis.
# matplotlib.pyplot.yticks(ticks=None, labels=None, **kwargs)
# # Parameters
#   ticks : array_like
#   labels : array_like, optional
#   **kwargs : Text properties can be used to control the appearance of the labels.
plt.yticks(np.arange(0, 81, 10))

# matplotlib.pyplot.legend
# - Place a legend on the axes.
# 長いので https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend
# を参考
# legend関数が要する引数は
# ・p1、p2二つのリストの一番目の要素
# ・p1のグラフ名、p2のグラフ名
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

# matplotlib.pyplot.show
# - Display a figure.
plt.show()
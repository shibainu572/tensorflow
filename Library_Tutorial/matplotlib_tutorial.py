# # matplotlib

# Matplotlibは、プログラミング言語Pythonおよびその科学計算ライブラリNumPyのためのグラフ描画ライブラリである
# オブジェクト指向のAPIを提供しており、様々な種類のグラフを描画する能力をもつ。
# 描画できるのは主に2次元のプロットだが、3次元プロットの機能も追加されてきている。
# 描画したグラフを学習形式の画像（各種ベクトル画像形式も含む）として保存することもできるし、wxPython, Qt, GTKといった一般的なGUIツールキット製のアプリケーションにグラフの描画機能を組み込むこともできる。
# MATLABの対話環境のようなものを提供するpylabというインタフェースも持っている。
# Matplotlibは、BSDスタイルのライセンスの下で配布されている。

# # プロット例
# 折れ線グラフ

# mayplolibとnumpyライブライを追加
import matplotlib.pyplot as plt
import numpy as np
# ヒストグラムで使うライブラリ追加
from numpy.random import normal,rand

# # 折れ線グラフ
# 指定された間隔で等間隔の数値を返します。
a = np.linspace(0, 10, 100)
# 0から10まで100この数字を生み出す。
# [ 0.          0.1010101   0.2020202・・・9.6969697   9.7979798   9.8989899  10.        ]
b = np.exp(-a)
plt.plot(a, b)
plt.show()

# # ヒストグラム
x = normal(size=200)
plt.hist(x, bins=30)
plt.show()
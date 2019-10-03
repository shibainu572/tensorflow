# # Numpyのndarrayのインスタンス変数shapeの意味

# NumPyで計算をするためのクラスndarrayは、多次元配列や行列を扱うためのデータ構造です。
# 内部実装では、データ型によってサイズの異なる連続した１次元のメモリ領域が確保されます。
# ndarrayのインスタンス変数shapeは、１次元のメモリ領域のどこに指定した多次元配列の要素があるのかを知る手掛かりになります。

# # ndarray.shape

# ndarrayのshapeは、各次元ごとの要素数を示します。
# 使い方はPythonインスタンスと同様arr.shapeとしてプロパティにアクセスするだけです。

import numpy as np

a = np.array([5, 3, 8, 9])

print("ndarray.shapeの出力")
print(a)
print(a.shape)
print("")

# reshape関数で変換すると、shapeは指定した引数に合わせて変更されます。
# ndarray内部の実装では配列の要素はshapeしか変更されません。
# 単に形状の情報だけ変化されているので高速に実行することができます。

# 変更後のshapeは、要素数が同じであればreshapeで指定した引数と同じものに変換されているはずです。

a = np.array([5, 3, 8, 9, 10, 11, 12, 13, 14, 10])

b = a.reshape((5, 2))

print("ndarray.reshapeの出力")
print("b : ", b)
print("b.shape : ", b.shape)
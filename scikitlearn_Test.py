# scikit-learn ライブラリの読み込み
from sklearn import datasets

#手書き文字セットを読み込む
digits = datasets.load_digits()

#どのようなデータか、確認してみる
import matplotlib.pyplot as plt
plt.matshow(digits.images[3], cmap="Greys")
plt.show()

#結果として3の画像が表示される　
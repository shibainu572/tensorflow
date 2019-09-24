# scikit-learn ライブラリの読み込み
from sklearn import datasets

# 手書き文字セットを読み込む
digits = datasets.load_digits()

# 画像データとテストデータの準備
# データセットには、「手書き数字の画像データ」と、それに対する「数字」が含まれます。
# データを訓練データとテストデータに分け、訓練データで学習した結果を、テストデータで検証します。

# 画像データを配列にしたもの(numpy.ndarray型)
x = digits.data

# 画像データに対する数字(numpy.ndarray型)。ラベルと言う
y = digits.target

# 訓練データとテストデータに分ける
# 訓練データ　: 愚数行
x_train, y_train = x[0::2], y[0::2]
# テストデータ : 奇数行
x_test, y_test = x[1::2], y[1::2]

#画像データ配列(愚数)
print("x-train : ", x_train)

#画像データに対する数字(愚数)
print("y-train : ", y_train)

#画像データ配列(奇数)
print("x-test : ", x_test)

#画像データに対する数字(奇数)
print("y-test : ", y_test)
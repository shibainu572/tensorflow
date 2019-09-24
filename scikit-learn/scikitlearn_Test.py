# scikit-learn ライブラリの読み込み
from sklearn import datasets
# 学習器の作成。SVMというアルゴリズムを選択
from sklearn import svm
clf = svm.SVC(gamma=0.001)

# 手書き文字セットを読み込む
digits = datasets.load_digits()

# 画像データを配列にしたもの(numpy.ndarray型)
x = digits.data

# 画像データに対する数字(numpy.ndarray型)。ラベルと言う
y = digits.target

# 訓練データとテストデータに分ける
# 訓練データ　: 愚数行
x_train, y_train = x[0::2], y[0::2]
# テストデータ : 奇数行
x_test, y_test = x[1::2], y[1::2]

# 訓練データとラベルで学習
clf.fit(x_train, y_train)
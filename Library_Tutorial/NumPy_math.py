# このページでは、三角関数や指数関数、対数関数など、基本的な数学関連の関数の使い方を解説します。
import numpy as np

# # 三角関数
print("三角関数")
# sin(0)
print("np.sin(0) : ", np.sin(0))
# sin([0, 1])
print("np.sin([0, 1]) : ", np.sin([0, 1]))
# cos(1)
print("np.cos(1) : ", np.cos(1))
# cos([0,1])
print("np.cos([0, 1]) : ", np.cos([0, 1]))
# tan(1)
print("np.tan(1) : ", np.tan(1))
# tan([0, 1])
print("np.tan([0, 1]) : ", np.tan([0, 1]))

# # 逆三角関数
print("")
print("逆三角関数")
# arcsin(1)
print("np.arcsin(1) : ", np.arcsin(1))
# arcsin([-1, 0, 1])
print("np.arcsin([-1, 0, 1]) : ", np.arcsin([-1, 0, 1]))
# arccos(1)
print("np.arccos(1) : ", np.arccos(1))
# arccos([-1, 0, 1])
print("np.arccos([-1, 0, 1]) : ", np.arccos([-1, 0, 1]))
# arctan(1)
print("np.arctan(1) : ", np.arctan(1))
# arctan([-1, 0, 1])
print("np.arctan([-1, 0, 1]) : ",np.arctan([-1, 0, 1]))

# # ラジアン ⇔ 度 の変換
print("")
print("ラジアン ⇔ 度 の変換")
# 度からラジアンへ(np.radians)
print("np.radians(0) : ", np.radians(0))
print("np.radians([np.rad2deg(1), 0, 90]) : ", np.radians([np.rad2deg(1), 0, 90]))
# 度からラジアンへ(np.deg2rad)
print("np.deg2rad(0) : ", np.deg2rad(0))
print("np.deg2rad([np.rad2deg(1), 0, 90]) : ", np.deg2rad([np.rad2deg(1), 0, 90]))
# ラジアンから度へ
print("np.rad2deg(0) : ", np.rad2deg(0))
print("np.rad2deg([np.deg2rad(180), 1, 0.5]) : ", np.rad2deg([np.deg2rad(180), 1, 0.5]))

# # 指数関数、対数関数
print("")
print("指数関数、対数関数")
# e(0)
print("np.exp(0) : ", np.exp(0))
# e(1)
print("np.exp(1) : ", np.exp(1))

# NumPyには、対数関数として以下が定義されています。
# ・eが底(Log_e(x))のnp.log(x)
# ・2が底(Log_2(x))のnp.log2(x)
# ・10が底(Log_10(x))のnp.log10(x)
# なお、定数eは、np.eとして定義されています。
# サンプルコード

# eを出力
print(np.e)
# eが底の指数関数 (Log_e(x))
np.log(1)
np.log([1, np.e, np.e ** 2, 0])

# 2が底の指数関数 (Log_2(x))
np.log2(2)
np.log2([1, np.e, np.e ** 2, 0])

# 10が底の指数関数 (Log_10(x))
np.log10(1000)
np.log10(1e+10)
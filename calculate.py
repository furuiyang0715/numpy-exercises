mport numpy as np

a = np.array([2, 6, 5])
b = np.array([1, 2, 3])

# 除法运算
# 在python3中 divide和true_divide效果相同 返回除法的浮点数结果不做截断
true_divide_res = np.true_divide(a, b)
divide_res = np.divide(a, b)

# / 相当于调用 true_divide
true_divide_res2 = a/b

# floor_divide函数总是返回整数结果
floor_res = np.floor_divide(a, b)

# // 相当于调用 floor_divide
floor_res2 = a//b

# 模运算
# remainder函数逐个返回两个数组中元素相除之后的余数
d = np.arange(-4, 4)
remainder_res = np.remainder(d, 2)

# mod 函数的功能同remainder函数完全相同
mod_res = np.mod(d, 2)

# % 的功能与之前两个完全一样
print(d % 2)

# fmod 所得余数的正负由被除数决定 与除数的正负无关
fmod_res = np.fmod(d, 2)

# 乘法运算
# multiply
mul_res = np.multiply(a, b)




## Number 数字类型
import math
import cmath
import random
a = 1.2
b = int(a)
print(b)
print(float(b))

print("=====================数学函数以下================================")
## math cmath模块引入
## 返回绝对值
print("abs(-10)",abs(-10))
## 上入整数
print("math.ceil(4.1)",math.ceil(4.1))
## 下舍整数
print("math.floor(4.9)",math.floor(4.9))
## 反余弦弧度值，-1到1之间的数值
print(math.acos(-1))
print("=====================随机函数以下================================")
print(random.choice(range(10))) ## 随机0到9选一个整数
print(random.random()) ## [0.1)


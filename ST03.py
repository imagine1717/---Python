# 运算符

print("===========================算数运算符以下================================")
# 算术运算符 +、-、*、/、%、**（幂）、//(取整数)
a = 21
b = 10
c = 0
c = a + b  # 加
print("+ c值为：", c)
c = a - b  # 减
print("- c值为：", c)
c = a * b  # 乘
print("* c值为：", c)
c = a / b  # 除
print("/ c值为：", c)
c = a % b  # 模
print("% c值为：", c)
a = 2
b = 3
c = a**b  # 幂
print("** c值为：", c)
a = 10
b = 5
c = a//b  # 取整数
print("// c值为：", c)

print("===========================比较运算符以下================================")
if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a < b:
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if a > b:
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

a = 5
b = 20

if a <= b:
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于 b")

if b >= a:
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")

print("===========================赋值运算符以下================================")
c = a + b
print("1 - c 的值为：", c)
c += a  # 加赋值
print("2 - c 的值为：", c)
c -= a  # 减赋值
print("3 - c 的值为：", c)
c *= a  # 乘赋值
print("4 - c 的值为：", c)
c /= a  # 除赋值
print("5 - c 的值为：", c)
c = 2
c %= a  # 模赋值
print("6 - c 的值为：", c)
c **= a  # 幂赋值
print("7 - c 的值为：", c)
c //= a  # 取整数 赋值
print("8 - c 的值为：", c)
print("===========================位运算符以下================================")
c = a & b  # 位与
print("1 - c 的值为：", c)
c = a | b  # 位或
print("2 - c 的值为：", c)
c = a ^ b  # 异或
print("3 - c 的值为：", c)
c = ~a  # 取反
print("4 - c 的值为：", c)
c = a << 2  # 左位移
print("5 - c 的值为：", c)
c = a >> 2  # 右位移
print("6 - c 的值为：", c)
print("===========================逻辑运算符以下================================")
if(a and b):  # 与
    print("1 - 变量a 和 b 都为 true")
else:
    print("1 - 变量a 和 b 有一个不为 true")

if(a or b):  # 或
    print("2 - 变量a 和 b 都为 true ,或其中一个变量为 true")
else:
    print("2 - 变量a 和 b 都不为 true")

a = 0
if a and b:
    print("3 - 变量a 和 b 都为 true")
else:
    print("3 - 变量a 和 b 有一个不为 true")
if a or b:
    print("4 - 变量a 和 b 都为 true ,或其中一个变量为 true")
else:
    print("4 - 变量a 和 b 都不为 true")

if not(a or b):  # not 非
    print("5 - 变量a 和 b 都为 false ,或其中一个变量为 false")
else:
    print("5 - 变量a 和 b 都不为 true")
print("===========================成员运算符以下================================")

list = [1, 2, 3, 4, 5, 6]
if (a in list):  # in 如果在指定列表找到相同元素返回true，否则返回false
    print("1 - 变量a 在给定的列表中 list中")
else:
    print("1 - 变量a 不在给定的列表中 list中")

if (b not in list):  # not in 指定列表中没有找到相同元素返回true，否则返回false
    print("2 - 变量b 不在给定的列表中 list中")
else:
    print("2 - 变量b 在给定的列表中 list中")
a = 2
if (a in list):
    print("3 - 变量a 在给定的列表中 list中")
else:
    print("3 - 变量a 不在给定的列表中 list中")


print("===========================身份运算符以下================================")
# is 判断两个变量是不是同一个对象引用
# is not 判断两个变量是不是引用不同对象

a = 20
b = 20
if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (a is not b):
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")

a = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等。
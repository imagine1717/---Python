# 变量类型，Python不需要我们指定类型，只需要赋值，它会自动转换你赋值的类型。弱类型语言
# 和javaScript一样
counter = 100 # 整数类型
miles = 10.0 # 浮点类型
name = "Python" # 字符串类型

print(counter)
print(miles)
print(name)
print("============================List 列表=================================\n")
# 列表，类型 数字、字符、复合等等
list = ['Python编程思想',100,2.32,'W',20.2]
newList = [123,'W']
print(list) # 完整输出列表所有元素
print(list[0]) # 0获取第一个元素
print(list[1:3]) # 输出第二个元素和第三个元素
print(list[2:]) # 从第三个元素开始输出之后所有元素
print(newList * 2) # 输出两次
print(list + newList) # 合并输出
print("=============================Tuple 元组================================\n")

# 元组,只能赋值一次，就是说只读列表
tuple = ('Python编程思想',100,2.32,'W',20.2)
newTuple = (123,'W')
print(tuple) # 完整输出元素所有元素
print(tuple[0]) # 0获取第一个元素
print(tuple[1:3]) # 输出第二个元素和第三个元素
print(tuple[2:]) # 从第三个元素开始输出之后所有元素
print(newTuple * 2) # 输出两次
print(tuple + newTuple) # 合并输出

print("==============================Dict 字典===============================\n")
# 字典 
# 字典可以通过key取值，k,v数据结构
dict = {}
dict['one'] = "第一个元素"
dict[2] = "第二个元素"
newDict = {'name':'Python','code':333,'dept':'sales'}
print(dict['one'])
print(dict[2])
print(newDict)
print(newDict.keys())
print(newDict.values())
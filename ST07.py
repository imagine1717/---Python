## 列表(list)
## 列表赋值
list2 = ['python2','python3','java8','java15',3,8,15]
print(list2) ## 输出所有元素
print('list2[0]: ',list2[0]) # 输出第一个元素
print('list2[1:5]: ',list2[1:5]) # 输出2,4元素

# 定义一个空元素然后赋值
list3 = []
list3.append('baidu')
list3.append('tencent')
list3.append('alibaba')
print(list3)

# 删除列表元素
list4 = ['python','python2','python3']
print(list4) ## 输出所有元素
del list4[1] # 删除第二个元素
print(list4) # 输出所有元素
print(list4[1]) ## 输出第二个元素

# len(list) 获取列表长度
print("len(list4): ",len(list4))
# 组合元素
print("list2 + list4 : ",list2 + list4)
# * 重复元素
print("list4 * 2",list4 * 2)
# 3 in 列表,判断元素是否存在列表中
print("\'python3\' in list4",'python3' in list4) 
# for x in 列表,迭代元素
for index in list4 : print(index)


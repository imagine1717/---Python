# 循环语句
count = 0
print("=====================================while循环======================================")
# while 循环
while(count < 9):  # 判断后执行
    print("The count is:", count)
    count = count + 1
print("Good Bye!")
print("=====================================循环中使用continue、break======================================")
# continue 跳出本次进入下次
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue  # 进入下次循环
    print(i)
# break 终止循环
while 1:
    print(i)
    i += 1
    if i > 10:
        break
print("=====================================循环使用else======================================")
# 循环使用 else
while count < 5:
    print(count, " is less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

print("=====================================for循环======================================")

for letter in 'Python':
    print("当前字母：", letter)
lans = ['Python', 'Java', 'JavaScript']
for lan in lans:
    print("当前编程语言：", lan)
print("Goog Bye!")

print("=====================================for循环 序列索引迭代======================================")

fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print("当前水果：", fruits[index])
print("Goog Bye!")
print("=====================================for循环 使用else 语句======================================")
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d 等于 %d * %d " % (num, i, j))
            break
    else:
        print(num, '是一个奇数')
print("=====================================使用双重while 打印 2 ~ 100的素数======================================")
num = 2
while(num < 100) :
    j = 2
    while (j <= (num/j)):
        if not(num%j):break
        j = j + 1
    if(j > num / j): print(num, '是素数')
    num = num + 1

print("Good Bye!")

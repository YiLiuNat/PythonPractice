#coding=utf-8
print "-------------------while loop-------------------"
count = 0
while (count < 9):
    print 'The count is:', count
    count += 1

print "Yahaha"

#continue与break
#continue用于跳过该次循环，break用于推出循环


# 该循环会无限输出双数
# i = 1
# while 1 < 10:
#     i += 1
#     if i%2 > 0: #除2无法除净 有余数时
#         continue #跳过有余数的单数 只输出双数
#     print i

j = 1
while 1: #就是while true
    print j
    j += 1
    if j > 9:
        break #当j>9跳出循环
print'End'

print "-------------------for loop-------------------"
for letter in 'Python':
    print '当前字母：', letter

fruits = ['banana','apple','mango']
for fruit in fruits:
    print '当前水果：',fruit

print 'End'

print "-----------------通过序列索引迭代----------------"
people = ['Tom','Anna','Wilson']
for index in range(len(people)):
    print '当前人物：', people[index]

print 'End'

print "--------------------循环嵌套--------------------"
x = 2
while(x < 50):
    y = 2
    while(y <= (x/y)):
        if not(x%y): break #没有余数时退出循环（not不为零的数为false）
        y = y + 1
    if (y > x/y): print x, " 是质数"
    x = x + 1
print "End"
print not(0)

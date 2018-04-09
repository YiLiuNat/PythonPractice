#coding=utf-8
#成员运算符
#除了普通的+-*/运算符外，python还支持成员运算符

#in运算符，如果在指定的序列中找到值就返回true，否则false
#not in 则与之相反
print "----------------------in/not in----------------------"
a = 10
b = 15
list = [10, 20, 30, 40, 50];

if (a in list):
    print "变量a在列表中"
else:
    print "变量a不在列表中"

if (b not in list):
    print "变量b不在列表中"
else:
    print "变量b在列表中"

#修改变量 a 的值
a = 2
if (a in list):
    print "更改后的变量a在列表中"
else:
    print "更改后的变量a不在列表中"


print "----------------------is/not is----------------------"
#is预算符与==的区别：is判断两个变量引用对象是否为一个，==判断两个值是否相等
x = 20
y = 20

if (x is y):
    print "x与y有相同的标识"
else:
    print "x与y没有相同的标识"
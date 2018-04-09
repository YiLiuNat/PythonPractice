#coding=utf-8
#数组
list = ['Tom', 123, 2.01, 'Jerry', 20.8]
tinylist = [123, 'john']

print list
print list[0]
print list[1:3]
print list[2:]
print tinylist*2
print list + tinylist


#元组 tuple，另一个数据类型 用()表示，不能二次赋值 只读
tuple = ('Tom', 123, 2.01, 'Jerry', 20.0)
tinytuple = (12, 'john')
#tuple[2] = 1000 #元组中为非法应用 因为元组是不允许更新的
list[2] = 1000 #列表中是合法应用


#Python字典
#据结构类型，列表是有序的对象集合，字典是无序对象集合
#区别在于，字典当中的元素是通过键来存取的，而不是通过偏移存取
#字典用{}标识，字典由索引(key)和它对应的值value组成
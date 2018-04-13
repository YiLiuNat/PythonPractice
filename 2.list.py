#coding=utf-8
#数组
list = ['Tom', 123, 2.01, 'Jerry', 20.8]
tinylist = [123, 'john']

print '----------------------数组----------------------'
print list
print list[0]
print list[1:3]
print list[-2]
print list[2:]
print tinylist*2
print list + tinylist

#元组 tuple，另一个数据类型 用()表示，不能二次赋值 只读
tuple = ('Tom', 123, 2.01, 'Jerry', 20.0)
tinytuple = (12, 'john')
#tuple[2] = 1000 #元组中为非法应用 因为元组是不允许更新的
list[2] = 1000 #列表中是合法应用

#Python字典
#除列表外最灵活的据结构类型，列表是有序的对象集合，字典是无序对象集合
#区别在于，字典当中的元素是通过键来存取的，而不是通过偏移存取
#字典用{}标识，字典由索引(key)和它对应的值value组成
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'john', 'code':6734, 'dept':'sales'}
#冒号前为键，冒号后为值

print '----------------------字典----------------------'
print dict['one']       #输出键为'one'的值
print dict[2]           #输出键为 2 的值
print tinydict          #输出完整的字典tindict
print tinydict.keys()   #输出所有键
print tinydict.values() #输出所有值

print '--------------------字符串更新-------------------'
var1 = 'Hello world!'
print "这是原字符串 :-", var1
print "更新字符串 :-", var1[0:6] + '这是更新后的字符!'


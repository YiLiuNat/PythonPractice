#coding=utf-8
# 函数代码块以def关键词开头，后接函数名称和圆括号
# 传入参数和自变量放括号中间
# 函数第一行可加入文档字符串用于函数说明
# 函数内容以冒号开始
# return 结束函数，选择性的返回一个值给调用方

# 语法
# def function_name (parameters):
#   "函数说明"
#   function_suite
#   return [expression]

def printme(str):
    "打印传入的字符串再加个嘻嘻嘻"
    print str + "嘻嘻嘻"
    return

printme("我要调用函数！");

print "-------------------------------"
def printinfo(name, age):
    "打印传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;

printinfo (age = 50, name = "yoki");
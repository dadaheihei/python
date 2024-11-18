#先把书上的例子抄过来
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else :
        print(car.title())
#看例子就知道几乎与C语言相似，但是还是有差别的，if后面没有括号加了一个冒号
#判断字符串是否相等时候，会判断大小写，当然，如果没必要判断也可以，利用upper 或者 lower方法全部变成大写或者小写就好了
if cars[2]!='Bmw':    #当然，不相等也是！=
    print(cars[2])
#下面是比较数值，当然，所有运算符都和C语言一个样子，懒得写了
#下面是多个条件的检查，个人认为不如C语言。在python中，都要满足是   and关键字，而不是&，同样，满足一个即可也不是  ||，而是or关键字
if cars[1]=='audi' and cars[3]=='toyota':
    print('sleep',end='')
if cars[1]!='audi' or cars[3]=='toyota':
    print('fish')
#判断特定值是否包含在列表中
#1.判断包含在列表中
if 'bmw' in cars:
    print('in')
if 'bmw' not in cars:
    print('not in')
#其实以上运算都算是bool 表达式
#一种新语句，兄弟们，学到新东西了！#对不起，突然发现也不是新东西
#if-elif-else语句
if 'bmw' not in cars:
    print('lipu')
elif 'audi' not in cars:   #也就是相当于C语言中的   else if语句    当然，可以无限叠加
    print('de')
else :
    print('dada')   #最终也只会输出三个语句中的一个
#处理列表
#判断是否为空
plainlist=[]
if plainlist:
    print('not plain')
else:
    print('plain')
#使用多个列表 正好有两个列表，那就直接用，懒得在写新的列表了
for car in cars:
    if car in plainlist:
        print(car+' in .')
    else:
        print(car+' not in .')


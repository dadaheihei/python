#简单看了一眼，好像和结构体C语言有点相似，再仔细看看
#还是，先抄一下书上的例子
alien={'color':'green','number':5}
print(alien['color'],end=' ')
print(alien['number'])
#虽然这看起来和C语言换汤不换药，但是接下来你就知道了
#第一个特殊功能：临时创建键-值对
print(alien)
alien['size']='100 meters'
print(alien)     #这样的操作就会在原来的字典中加上一个size参数，而且不会删除原来的参数，当然，同理，也可以创建一个空的字典，后面慢慢加参数
#当然，和C语言一样，也可以修改
alien['color']='yellow'
print(alien)
#可以加那就可以删除，同样使用del语句
del alien['size']
print(alien)
#遍历字典
for a,b in alien.items():#如左面所示，可以定义两个变量分别对应键与值，然后调用items()方法从而达到输出的目的
    print(a,end=': ')
    print(b)
#遍历字典中的所有键，这个就比较灵活
#1.
for k in alien:#这样就会默认遍历键
    print(k)
#2.
for k in alien.keys():#当然，这样更有辨识度，
    print(k)
#遍历字典中的所有键，并且排序
for k in sorted(alien.keys()):
    print(k)
#遍历字典中的所有值，这个就不能灵活了，必须调用values方法
for v in alien.values():
    print(v)
#键不会重复，但是键可能会重复，比如成绩单字典，去掉重复，需要调用set()方法
for v in set(alien.values()):
    print(v)
#嵌套
#1.创建一个字典列表，但是每一个都要自己去重复定义，好麻烦
alien1={'color':'green','number':1}
alien2={'color':'green','number':2}
alien3={'color':'green','number':3}
aliens=[alien1,alien2,alien3]
for one_alien in aliens:
    print(one_alien)
#2.使用range()自动生成外星人
aliens_2=[]
for alien_number in range(0,30):
    new_alien={'color':'green','number':alien_number}
    aliens_2.append(new_alien)
print(aliens_2)
#在字典中存贮列表
pizza={
    'size':'10cun',    #不要忘记逗号！！！！！！
    'toppings':['mushrooms','cheese']
}
print(pizza['toppings'][1])
#在字典中存储字典
user={
    'name':{
        'first':'Alice',
        'second':'Bob'
    },
    'number':{
        'first':1,
        'second':2
    }
}
print(user['name']['first'])
print(user['number']['first'])






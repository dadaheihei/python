#定义函数
def dada():
    """打印dada"""#文档字符串，描述函数的用途，用三重双引号构成，python使用它们来生成有关程序中函数的文档
    print('dada')
#def后面的所有缩进行是函数体
dada()
#向函数传参才是函数真正有用的用途
def lipu(username):
    """问候用户"""
    print('lala ' +username+'!')

lipu('Alice')
#形参与实参（该来的总归要来了）
#别的不说了，就是说一下，传参的时候顺序要好好看看
#在这有一个比C语言高级的地方，可以设置形参的默认值，以至于传参的时候不传也可以
def pet(pet_name,name='dog'):
    """显示宠物的信息"""
    print('I have a '+name+',his name is '+pet_name)

pet('Wang Ziming')
pet(pet_name='wangziming')#可以以两种方式传参，但是前提是没有默认值的在前面,虽然没有默认值的不允许在前面（baga）
pet('peter','cat')#传了就改了，不传就默认
pet('lalala')#下一次不传，依旧默认
def pets(pet_name='lala',name='dog'):
    """显示宠物的信息"""
    print('I have a '+name+',his name is '+pet_name)

pet(pet_name='Wang Ziming')#我又发现，即使两个都有默认值，我只修改后面的参数，也会报错

#设置返回值
def cars(num):
    """返回车库里的一辆车"""
    car=['bmw','audi','daniu']
    return car[num]

print(cars(1))
#设置可选实参，就是在函数定义的时候把一个变量默认值设为空字符，这样函数使用就会很灵活
def musician(first_name,last_name,age=''):
    print(first_name+' '+last_name+' is a great musicain.')
    if age:
        print('and he is '+str(age)+'years old.')   #不要忘记，打印字符串的时候不允许中间有数字，需要先强制类型转换

musician('Tom','White')
musician('Jone','Smith',27)
#像其他传递列表，字典啥的没有什么特殊，就不实验了，接下来进行是否会改变的实验
def multy(num):
    num+=1
    print(num)

num=1
multy(num)
print(num)#果然，一个输出2，一个输出1，那么我们接着试试列表

def list(names):
    names.pop()
    print(names)
names=['1','2','3','4','5']
list(names)
print(names)#果然，输出是一个样子，都改变了，和C语言底层上没有什么差别
            #但是别忘了列表还有副本这么一个东西
list(names[:])
print(names)    #这样子输出就不一样了，呕吼

#牛的来了，传递任意数量的实参,其实实际上是传进去一个元组
def niude(*name):
    print(name)

niude('dada')
niude('da ','da ')
#当然因为这个东西不知道自己要多少东西，所以一次只能有一个元组，并且要放在最后面
#下面更加硬核，传字典
def dic(first ,last,**dictionary):
    dic={}
    dic['first']=first
    dic['last']=last
    for key,value in dictionary.items():
        dic[key]=value
    print(dic)
dic('lala','dada',lipu='sleepfish')#注意这个东东是怎么传进去的
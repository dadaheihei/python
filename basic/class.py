#1.创建和使用类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self ,name ,age):#类中的函数称为方法，而__init__(是两个下划线哦)则是一个特殊的方法，当你使用这个类的时候，python会自动运行它，并且两个下划线不可缺失
        """初始化属性name和age"""#_init_中有三个实参，分别是self name age，self必不可少，每一个与实例相关联的函数，都会自动传递参数self，当我们使用的时候，不需要手动去传·，只需要传后两个实参就好
        self.name=name
        self.age=age
        self.master='dada'#设定属性默认值

    def sit (self):
        """sit """
        print(f"{self.name} is now sitting")

    def roll(self):
        """roll"""
        print(f"{self.name} is now rolling")

    def format(self):
        """format output"""
        fname=f"{self.master} {self.name} {self.age}"
        return fname

    def change_master(self,message):
        self.master=message

class fur:
    def __init__(self,color='white',length=100):
        self.color=color
        self.length=length
    def describe_fur(self):
        print(f"{self.color},{self.length}")
#根据类创造实例
my_dog=Dog('white',6)
print("my dog's name is {mydog.name}")
print("my dog's age is {mydog.age}")
my_dog.sit()
my_dog.roll()
#修改属性默认值
print(my_dog.master)
my_dog.master='lala'
print(my_dog.master)
my_dog.change_master('tutu')
print(my_dog.master)
#格式化输出
print(my_dog.format())
#继承
class son_dog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)#super()是一个特殊的函数，让你能过调用父类的方法，这行代码就是能让你调用Dog父类的__init__()方法
        self.number=0#子类独有的属性
        self.fur=fur()#将实例用作属性
    def format(self):#可以通过修改父类的某一个方法来让这个方法更有普适性
        fname=f"{self.master} {self.name} {self.age} {self.number}"
        return fname
my_son_dog=son_dog('Bob',7)
my_son_dog.master="titi"
print(my_son_dog.format())#说明子类可以使用父类的方法
fur_d=fur('black')
fur_d.describe_fur()
my_son_dog.fur.describe_fur()

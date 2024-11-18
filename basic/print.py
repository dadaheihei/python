#定义一个变量,并且定义之后的变量是可以修改的，这和C语言是相似的
#IMPORTANCE 变量名只能包含数字、字母、下划线，并且，数字不能打头，变量名不可以包含空格，切记不要把关键字用作变量名

message='Hello world!'
print(message)
message+=' python'
print (message)

#下一个问题，我们将谈及字符串:在python中，引号内部的东西都是字符串，而这个引号不仅可以是双引号，也可以是单引号，so你可以在字符串中添加双引号或者单引号
#修改字符串的大小写
#1:title()方法    会使字符串中所有的单词首字母大写

message='i am a little pig'
print(message.title()) #python中使用方法用'.'运算符

# #2.upper()和lower()方法   将字符串中所有的字母大写或者小写

print(message.upper())
print(message.lower())
#合并（拼接）字符串,即加号运算符'+'
print(message+','+'you are a big pig'+' !')
#python中也有'\n'  '\t' heC语言相似，所以这里就不加以试验了
#删除空白  包括删除前空格，后空格，前后的空格
name=' python '
print(name.lstrip())    #删除前空格#但是这种删除是暂时的，想要永久删除，就要存回到变量中
print(name.rstrip())    #删除后空格
print(name.strip())     #删除所有空格
#正常情况下，print函数会自动换行，但是如果不想换行，可以设置end条件
print('baga',end='')
print('yalu')   #这样就可以输出完整版的bagayalu，当然，想要在中间加入什么有趣的东西，亦可以填在end的‘’里面

#需要注意的是，如果要在代码字符串中使用单引号或双引号，需要使用另一种引号将其括起来，例如：
#python -c "print('Hello, \"world\"!')"    这是命令行语句
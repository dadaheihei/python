##简单看了一眼，还是和C语言相差不大
# number=range(0,10)
# i=0
# while i<10 and number[i]%2>=0:   #这个东东有顺序的，第一个表达式有问题会报错，有毛病吧，比如这个东东把前后换位置就会报错[angry]
#     print(number[i])
#     i+=1    #python中没有++  --运算符 [angry]
# #退出循环依旧可以使用break，结束这一次循环继续下一次循环依然可以使用continue
# while 1:
#     message=input()
#     if message=='again':
#         continue
#     if message=='quit':
#         break
#while循环处理字典和列表
#处理列表
user=['alice','bob','eric']
confirmed_user=[]
i=0
num=len(user)
while i<num:
    confirmed_user.append(user.pop())
    print(user)
    print(confirmed_user)
    i+=1
#也可以通过remove方法来删除全部长得一样的元素
pets=['1','2','1','3']
while '1' in pets:
    pets.remove('1')
    print(pets)
#处理字典
#使用用户输入来充填字典
dada={}
lipu=1
while lipu==1:
    name=input("please input your name: ")
    value=input("do you think dada is a good boy: ")
    dada[name]=value
    if input("is there another person ? ")=='no':
        break
for k,v in dada.items():
    print(k+' : '+v)










#注，所有IMP代表重点或提醒

#python用'[]'来表示列表，并用逗号来分隔其中的元素
person=['Green','White','Brown']
print(person)  #当然这样打印的还会有问题，就是让他会连带着把‘【】’和引号一起打出来，，就像打印字符串一样

#访问列表元素，其实就是类似于C语言，这里不多加阐述
print(person[0].upper())
#但是python为访问最后一个列表元素提供了一个特殊语法。通过将索引指定为-1，可以访问最后一个元素

#讲到列表，就不得不提及修改，添加和删除元素
print(person[0])
person[0]='Da Yu'
print(person[0])  #和C语言本质上没有区别，正常修改就好了

#重点是添加，这也就相当于一个可变数组，也就是类似C++中的vector
#1：在列表末尾添加元素，    append()方法
person.append('David')
print(person)
#2:插入元素    insert(num,'XXX')    在num位置上插入什么东东
print(person.insert(0,'Da Da'))

#删除元素
#del语句    如果知道想要删除元素的下标，那么可以使用del语句    IMP是语句，不是方法
del person[1]
print(person)
#pop()方法   相当于C语言栈的操作，弹出栈顶元素，而这个是弹出列表末尾，并且会返回这个被删除的元素
popped_person=person.pop()
print(person)
print(popped_person)
#当然pop()可以做更多更好的事情，比如删除指定位置的元素
popped_person2=person.pop(1)
print(popped_person2)
#remove()方法 删除元素的值,使用的方法如下，如果已经不存在数据了，他将会直接输出None，但是如果找不到，他就会报错，并且remove只会删除第一个被发现的相同字符
print(person.remove('Brown'))
print(person.remove(person[0]))

person=['Green','white','Brown']
#组织列表
#1：排序，使用方法sort（）对列表进行永久性的排序，按照字母顺序排列，也就是ASCLL码排列,大写在上，小写在下
person.sort()
print(person)
#如果想要逆序排列，则传参 reverse=True
person.sort(reverse=True)
print(person) ##sort()方法不可以在print内部使用
#临时排序   sorted() 可以在print语句中使用，临时临时，排完就变回原样
print(sorted(person))
print(person) 
#倒着输出列表，没有任何排序作用，单纯倒着来，并且永久性   reverse()
person.reverse()
print(person)
#确定列表的长度   len() 返回数字，即列表元素个数
print(len(person))
#循环
for aperson in person:
    print(aperson)
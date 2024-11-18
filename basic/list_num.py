#循环
#1.for循环
nums=[1,2,3,4,5,6,7,8]
for num in nums:   #':'不要忘记哦
    print(num)
    n=num-1        #这串代码的含义是依次在nums列表中取出一个元素存入num中，不要忘记print的特点，自带换行功能
    print('The'+str(n)+'number is '+str(num))

#range()函数     range(num1,num2)会生成从num1到num2-1这几个数字
for num in range(1,5):
    print(num)
#list()函数   会将range()函数生成的列表存储在一个变量名字中
numbers=range(1,5)
print(numbers)
#range()函数还可以指定步长    range(num1,num2,num_a_step)
numbers=range(2,11,2)
print(numbers)
#使用range()函数几乎可以生成一切有规律的数集
squares=[]
for num in range(3,18,3):
    square=num**2   #在python中，乘方是'**'而不是'*'
    squares.appened(square)
print(squares)
#一个更加简洁的方法
for num in range(3,18,3):
    squares.appened(num**2)
#求数字队列的最大值最小值以及总和    min()  max()  sum()
print(min(nums))
print(max(nums))
print(sum(nums))
#列表解析（我也是第一次听说这个词语，有点奇怪）书上讲将for循环和创建新元素的代码合二为一，并自动附加新元素
list_num=[ value**2 for value in range(1,11)]  #不可以交换位置
print(list_num)

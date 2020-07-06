"""1 2 3 4组成的所有三位数，且不出现重复
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if(i != j) & (i != k) & (j != k):
                print('%d' % i, '%d' % j, '%d' % k)
"""

# class Person():
#
#     def __init__(self, name):
#         self.first_name = name
#
#     @property
#     def name(self):
#         return self.first_name
#
#     @name.setter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise TypeError("name must be string")
#         self.first_name = name
#
#     @name.deleter
#     def name(self):
#         raise AttributeError("can not delete attribute")
#
#
# if __name__ == "__main__":
#     p = Person("abc")
#     print(p.name)
#     p.name = "zhouzhou"
#     print(p.name)
#     del p.name


# def test():
#     a = ['word', 2, 3]
#     b = a
#     print(b)
#     data = [3, [55, 44], (7, 8, 9)]
#     data[1].append(33)
#     print(data[1])
#     data[2] += (10, 11)
#     print(data[2])
#
#
# if __name__ == "__main__":
#     test()

# def consumer():
#     r = ''
#     while True:
#         n = yield r  # 执行的中断点 可以拆分为两步理解 yield r  --->  n = r
#         if not n:    # 在Python中，None、空列表[]、空字典{}、空元组()、0等一系列代表空和无的对象会被转换成False
#             return
#         print('[消费者] 正在消费:{0}'.format(n))
#         r = '200 人民币'
#
#
# def produce(c):
#     c.send(None)  # 启动消费者（生成器）——实际上是函数调用，只不过生成器不是直接象函数那般调用的
#     # c.__next__()
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[生产者] 正在生产:{0}'.format(n))
#         r = c.send(n)  # 给消费者传入值——实际上也是函数调用
#         print('[生产者] 消费者返回:{0}'.format(r))
#         print('-------------------------------------------------')
#     c.close()
#
#
# c = consumer()  # 构造一个生成器
# produce(c)

# class Get_try():
#     def __init__(self, value):
#         self.value = value
#
#     def __getattr__(self, item):
#         self.value = item
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#
# if __name__ == "__main__":
#     g = Get_try("abc")
#     g.value1      # 相当于调用__getattr__（self，item = value1），运行后，g.value = value1
#     print(g.value)
#     g.value2 = 3  # 相当于调用__setattr__（self，key = value2, value = 3 ）
#     print(g.__dict__)

# import re
# website = 'http://www.inter.com/messageInfo?id=35' \
#           'https://www.inter.cn/messageInfo?id=35' \
#           'http://123456.com/messageInfo?id=35'
# website = re.findall(r'(?<=://)[a-zA-Z\.0-9]+(?=\/)', website)
# print(website)

# import os
# from shutil import copyfile
#
#
# def walk_dir(file):
#     for root, dirs, files in os.walk(file):
#         # root 表示当前正在访问的文件夹路径
#         # dirs 表示该文件夹下的子目录名list
#         # files 表示该文件夹下的文件list
#         if not os.path.exists('E:/log'):
#             os.makedirs("E:/log", mode=0o777)
#         for name in files:
#             print("这里遍历的是文件：")
#             print(name)
#             if name.endswith(".txt"):
#                 copyfile(os.path.join(root, name), "E:/log/")
#             # print(os.path.join(name))
#         for name in dirs:
#             print("这里遍历的是文件夹：")
#             print(name)
#             # print(os.path.join(name))
#
#
# walk_dir('D:/test_result')

# def add(n, i):
#     return n+i
#
#
# def test():
#     for i in range(4):
#         yield i
#
#
# g = test()
#
# for n in [1,10,5]:
#     g = (add(n, i) for i in g)
#
# print(list(g))


# dictList = '0123456780'
# print(dictList.index('x'))  #报错substring not found


# 字符串www.baidu.com,输出com.baidu.www
# str = 'www.baidu.com'
# temp = str.split('.')
# str = '{}.{}.{}'.format(temp[2], temp[1], temp[0])
# print(str)

# n = int(input("请输入一个数字:\n"))
#
#
# def demo(n):
#     sum = 0
#     if n == 0 | n == 1:
#         sum = 1
#     else:
#         sum = n * demo(n - 1)
#     return sum
#
#
# print("%d 的阶乘为 %d"%(n, demo(n)))


# str = "ABCDEFG"
# for i in str:
#     print(i)
#
# list1 = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7]
# print(list1)
# print(list(set(list1)))
#
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list1)
# print(list2)
# print(list({}.fromkeys(list1).keys()))


L = [1, 2, 3, 4, 5]
print(L[1:-1])
s = ''
for i in L:
    s = s + str(i)

print(s)
print(type(s))


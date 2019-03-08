# def power(x, n = 2):
# 	s = 1
# 	while n > 0:
# 		s = s * x
# 		n = n - 1
# 	return s

# def enroll(name, gender, age=6, city="Beijing"):
# 	print("name:", name)
# 	print("gender:", gender)
# 	print("age:", age)
# 	print("city:", city)


# def calc(*numbers):  #这是可变参数
# 	sum = 0
# 	for n in numbers:
# 		sum = sum + int(n)*int(n)
# 	return sum

#def person(name, age, **kw):
#	print("name:", name, "age:", age, "other:", kw)

# def person(name, age, **kw):   #这是命令关键字参数
# 	print(name, age, kw)


# def person(name, age, *, city, job):   #这是强制关键字参数，除非有默认值，否则不可以不传
# 	print(name, age)

# def findMinAndMax(L):
# 	if L!=[]:
# 		(min, max)=(L[0], L[0])
# 		for number in L:
# 			if number < min:
# 				min = number
# 			if number > max:
# 				max = number
# 		return(min, max) 
# 	else:
# 		return (None, None)

# def add(x, y , f):
# 	return f(x)+f(y)

#print(power(5, 3))
#enroll("lp", "男")
#enroll("lp", "男", 22, "cq")
#calc([1, 2, 3])
#l = [1,2,3]
#print(calc(1,2,3,4))
#print(calc(*l))
#person("lp", 22)
#person("lp", 22, city="cq")
#extra = {'city': "cq", "job" : "engineer"}
#person("lp", 22)
#person("lp", 22, city = 'cq', job = 'engineer')
#person("lp", 22, **extra)
#print(findMinAndMax(list(range(100))))
#print(add(-1,2,abs))
#print(list(map(str, [1,2,3,4,5])))
#print(list(map(findMinAndMax, [(1,2),(2,3),(3,4,5)])))

# from functools import reduce

# DIGIST = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}


# def str2int(s):

# 	def fn(x, y):
# 		return x*10 + y
# 	def char2num(s):
# 		return DIGIST[s]
# 	return reduce(fn, map(char2num, s))

# #print(str2int("123456"))

# def normalize(name):
# 	return name.capitalize()
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# #print(L2)


# def prod(L):
# 	def product(x, y):
# 		return x * y
# 	return reduce (product, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


#利用过滤器求素数
#1.定义一个生成器，生成一个无限序列
# def _odd_iter():
# 	n = 1
# 	while True:
# 		n = n + 2
# 		yield n

# #2.定义一个筛选器
# def _not_divisible(n):
# 	return lambda x: x % n > 0

# #3.定义一个生成器，不断的返回下一个素数
# def primes():
# 	yield 2
# 	it = _odd_iter() #初始化数列
# 	while True:
# 		n = next(it)
# 		yield n
# 		it = filter(_not_divisible(n), it)

# # for n in primes():
# # 	if n < 1000:
# # 		print(n)
# # 	else:
# # 		break

# def is_palindrome(n):
# 	n = str(n)
# 	return n == n[-1::-1]


# 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# print("abc"[-1::-1])


# print(sorted([36,5,-12,9,-21]))
# print(sorted([36,5,-12,9,-21], key = abs))
# print(sorted([36,5,-12,9,-21], key = abs, reverse = True))

# def createCounter():
# 	s = [0]
# 	def counter():
# 		s[0] = s[0] + 1
# 		return s[0]
# 	return counter

# # 测试:
# # counterA = createCounter()
# # print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# # counterB = createCounter()
# # if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
# #     print('测试通过!')
# # else:
# #     print('测试失败!')

# #L = list(filter(lambda n: n%2==1, range(1, 20)))
# #print(L)

# def log(func):
# 	def wrapper(*args, **kw):
# 		print('call %s():' % func.__name__)
# 		return func(*args, **kw)
# 	return wrapper

# @log
# def now():
# 	print("2019-2-13")

#增加参数
# def log(text):
# 	def decorator(func):
#		@functools.wraps(func)	#作用是将now()函数的属性复制到warpper
# 		def wrapper(*args, **kw):
# 			print('%s %s:' % (text, func.__name__))
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator

# @log('execute')
# def now():
# 	print ('2019-02-13')

# import time, functools
# def metric(fn):
# 	@functools.wraps(fn)
# 	def wrapper(*args, **kw):
# 		t1 = time.time()
# 		r = fn(*args, **kw)
# 		print('%s executed in %s ms' % (fn.__name__, 1000*(time.time() - t1))
# 		return r
# 	return wrapper

# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# import functools
# int2 = functools.partial(int, base=2)
# print(int2("1000000"))

# max2 = functools.partial(max, 10)
# #max2(5,6,7) ==> max2(10,5,6,7)
# print(max2(5))

# class Student(object):  #object为父类对象
# 	def __init__(self, name, score, age):
# 		self.name = name
# 		self.score = score
# 		self.__age = age   #加上__变为私有属性
# 	def print_score(self):
# 		print('%s: %s' % (self.name, self.score))

# bart = Student("lp", 70, 22)
# print(bart.name, bart.score)
# bart.print_score()

# type(1123)  #判断类型
# dir('ABC')  #获取一个对象的所有属性和方法
# #getattr()、setattr()、hasattr()可以用于获取设置和判断对象的属性

# #对于对象可以随时创建任意的属性，如：
# my = Student("lp", 80, 22)
# my.height = 176
# #如要设置类的属性，则
# class Teacher(object):
# 	name = 'Teacher'

# 	@property  #加上@property是属性直接变成get_birth()
# 	def birth(self):
# 		return self._birth

# 	@birth.setter
# 	def birth(self, value):
# 		self._birth = value
	
#这种情况下声明创建的对象可以拥有该属性，

#class Dog(Mammal, Runnable) #支持多重继承

#__str__ 相当于toString()
#__iter__ 相当于迭代器 

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))  #Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
#     def __str__(self):
#         return self._path
#     __repr__ = __str__

# print(Chain().status.user.timeline.list)

# from enum import Enum, unique

# Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
# for name, member in Month.__members__.items():    #value属性则是自动赋给成员的int常量，默认从1开始计数。
# 	print(name, '=>', member, ',',member.value)


# @unique
# class Weekday(Enum): #枚举派生出自定义类，@unique保证没有重复值
# 	Sun = 0
# 	Mon = 1
# 	Tue = 2
# 	Wed = 3
# 	Thu = 4
# 	Fri = 5
# 	Sat = 6
# print(Weekday.Mon)
# print(Weekday['Tue'])
# print(Weekday.Wed.value)
# print(Weekday(1))

# with open('E:\\python\\python_test\\abc.txt', 'r') as fr:
# 	print(fr.read())

# with open('E:\\python\\python_test\\abc.txt', 'r', encoding='gbk', errors = 'ignore') as fr:
# 	print(fr.read())

# with open('E:\\python\\python_test\\abc.txt', 'a') as fw:   #w模式是覆盖，a模式是追加
# 	fw.write("\nsdadadadada")

# with open('E:\\python\\python_test\\abc.txt', 'r', encoding='gbk', errors = 'ignore') as fr: 
# 	print(fr.read())


# from io import StringIO
# f = StringIO()
# f.write("Hello")
# f.write(" ")
# f.write("World!")

# print(f.getvalue())

# from io import BytesIO
# f = BytesIO()
# f.write("中文".encode('utf-8'))
# print(f.getvalue())

import os

#print(os.name) 查看系统类型
#print(os.uname())  windows上不可用 查看详细信息
#print(os.environ)  查看环境变量

#print(os.path.abspath('.'))  查看当前目录的绝对路径
#path = os.path.join(os.path.abspath('.'), 'test')  创建新目录先获取当前路径，然后join拼接出目录的绝对路径
#os.mkdir(path)   创建目录
#os.rmdir(path)   删除目录
#print(os.path.split('E:\\python\\python_test\\abc.txt')[0]) 将文件的绝对路径拆分为目录和文件名
#os.path.splitext('E:\\python\\python_test\\abc.txt') 拆分为文件和扩展名
#os.rename('abc.txt', 'def.txt') 修改文件名
#os.remove("def.txt") 删除文件名
# with open('abc.txt', 'a+') as f:    可以直接创建
# 	f.write("sdasdad")

# import pickle
# d = dict(name = 'lp', age = 22)

# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f= open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# import json
# # json.dumps(d)

# class Student(object):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def __str__(self):
# 		return self.name + str(self.age)

# def student2dict(std):
# 	return {
# 		'name': std.name,
# 		'age': std.age
# 	}

# s = Student('lp', 22)
# print(json.dumps(s, default = student2dict))
# print(json.dumps(s, default = lambda obj: obj.__dict__))

# #json转为对象

# def dict2Student(d):
# 	return Student(d['name'], d['age'])
# json_str = '{"name": "lp", "age": 22}'
# print(json.loads(json_str, object_hook=dict2Student))

#windows 无法使用fork创建进程
#使用multiprocessing 模块提供的Process类来创建
from multiprocessing import Process
import os

# def run_proc(name):
# 	print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Process(target=run_proc, args=('test', ))
# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')

# from multiprocessing import Pool
# import time, random

# def long_time_task(name):
# 	print('Run task %s (%s)' % (name, os.getpid()))
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds' % (name, (end-start)))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	p = Pool(4)
# 	for i in range(5):
# 		p.apply_async(long_time_task, args = (i,))
# 	print('Waiting for all subprocess done...')
# 	p.close()
# 	p.join()
# 	print('All subprocess done')



from multiprocessing import Process, Queue
import os, time, random

def write(q):
	print("Process to write: %s" % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

def read(q):
	print('Process to read: %s' % os.getpid())
	while True:
		value = q.get(True)
		print('Get %s from queue.' % value)

if __name__=='__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()



#coding:utf-8
#taskManager.py for windows
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number = 10
#定义收发队列
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)
def get_task():
	return task_queue
def get_result():
	return result_queue

#创建类似的QueueManager:
class QueueManager(BaseManager):
	pass
def win_run():
	#Windows 下绑定调用接口不能使用lambda, 所以只能先定义函数在绑定
	QueueManager.register('get_task_queue', callable = get_task)
	QueueManager.register('get_result_queue', callable = get_result)
	#绑定端口并设置验证口令，Windows下需要填写Ip地址， Linux下不填默认本地
	manager = QueueManager(address = ('127.0.0.1', 8001), authkey = bytes('qiye', encoding = 'utf8'))
	#启动
	manager.start()
	try:
		#通过网络获取任务队列和结果队列
		task = manager.get_task_queue()
		result = manager.get_result_queue()
		#添加任务
		for url in ["ImageUrl_"+str(i) for i in range(10)]:
			print('put task %s ...' % url)
			task.put(url)
		print ('try get result ...')
		for i in range(10):
			print('result is %s' % result.get(timeout = 10))
	except:
		print('Manager error')
	finally:
		manager.shutdown()
if __name__ == '__main__':
	# Windows下多线程可能会有问题，添加这句可以缓解
	freeze_support()
	win_run()		


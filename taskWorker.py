#coding:utf-8
import time
from multiprocessing.managers import BaseManager
#创建类似的QueueManager:
class QueueManager(BaseManager):
	pass
#获取queue的方法名
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
#连接到服务器
server_addr = '127.0.0.1'
print('Connect to server %s ...' % server_addr)
m = QueueManager(address=(server_addr, 8001), authkey = bytes('qiye', encoding = 'utf8'))
m.connect()
#获取queu
task = m.get_task_queue()
result = m.get_result_queue() 
while(not task.empty()):
	image_url = task.get(True, timeout = 5)
	print ('run task download %s ...' % image_url)
	time.sleep(1)
	result.put('%s--->success' & image_url)

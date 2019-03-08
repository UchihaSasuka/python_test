import threading, time, queue, random

class ProdCons():

    FINISHED = False


    def __init__(self, q):
        self.q = q

    def produce(self):
        for i in range (1, 20):
            print('生产任务'+str(i)+'开始')
            time.sleep(random.randint(1,10) * 0.2)
            self.q.put(i)
            print('生产任务'+str(i)+'完成')
        self.FINISHED = True
        print("生产任务全部完成")

    def consumer(self):
        while not self.FINISHED or not self.q.empty()  :
            i = q.get()
            print('消费任务'+str(i)+'开始')
            #time.sleep(random.randint(1, 10) * 0.1)
            print('消费任务'+str(i)+'结束')
        print("消费任务全部完成")

if __name__ == '__main__':
    q = queue.Queue()
    prod_conds = ProdCons(q)
    p1 = threading.Thread(target=prod_conds.produce)
    p2 = threading.Thread(target=prod_conds.consumer)
    p1.start()
    p2.start()


生产任务1开始
生产任务1完成
消费任务1开始
生产任务2开始
生产任务2完成
生产任务3开始
消费任务1结束
消费任务2开始
消费任务2结束
生产任务3完成
生产任务4开始
消费任务3开始
消费任务3结束
生产任务4完成
生产任务5开始
消费任务4开始
消费任务4结束
生产任务5完成
消费任务5开始
生产任务6开始
消费任务5结束
生产任务6完成
生产任务7开始
消费任务6开始
消费任务6结束
生产任务7完成
生产任务8开始
消费任务7开始
生产任务8完成
消费任务7结束
生产任务9开始
消费任务8开始
消费任务8结束
生产任务9完成
消费任务9开始
生产任务10开始
消费任务9结束
生产任务10完成
消费任务10开始
生产任务11开始
生产任务11完成
生产任务12开始
消费任务10结束
消费任务11开始
生产任务12完成
生产任务13开始
消费任务11结束
消费任务12开始
消费任务12结束
生产任务13完成
生产任务14开始
消费任务13开始
消费任务13结束
生产任务14完成
生产任务15开始
消费任务14开始
生产任务15完成
生产任务16开始
消费任务14结束
消费任务15开始
生产任务16完成
生产任务17开始
消费任务15结束
消费任务16开始
消费任务16结束
生产任务17完成
消费任务17开始
生产任务18开始
消费任务17结束
生产任务18完成
消费任务18开始
生产任务19开始
消费任务18结束
生产任务19完成
生产任务全部完成
消费任务19开始
消费任务19结束
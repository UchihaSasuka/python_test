import threading, time, queue, random
from multiprocessing.pool import Pool

class ProdCons():

    FINISHED = False


    def __init__(self, q, name):
        self.q = q
        self.name = name

    def produce(self):
        for i in range (1, 20):
            print('生产任务'+ self.name + str(i) + '开始')
            time.sleep(random.randint(1,10) * 0.2)
            self.q.put(i)
            print('生产任务'+ self.name + str(i) +'完成')
        self.FINISHED = True
        print("生产任务+" self.name + "全部完成")

    def consumer(self):
        while not self.FINISHED or not self.q.empty()  :
            i = self.q.get()
            print('消费任务'+ self.name + str(i)+'开始')
            #time.sleep(random.randint(1, 10) * 0.1)
            print('消费任务'+ self.name + str(i)+'结束')
        print("消费任务"+ self.name + "全部完成")

def main(name):
    q = queue.Queue()
    prod_conds = ProdCons(q, name)
    p1 = threading.Thread(target=prod_conds.produce)
    p2 = threading.Thread(target=prod_conds.consumer)
    p1.start()
    p2.start()

if __name__ == '__main__':
    pool = Pool()
    groups = ['一', '二', '三']
    pool.map(main, groups)
    pool.close()
    pool.join()
    



import threading, time
from queue import Queue
from collections import OrderedDict


class AtomicCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self, add_value=1):
        with self._lock:
            self.value += add_value
            return self.value

    @property
    def Value(self):
        return self.value


def do_multitask(iterations, task_fun, thread_count=3, max_queue_buffer=0):
    task_q = Queue(maxsize=max_queue_buffer)
    result_q = Queue(maxsize=max_queue_buffer)

    locker_queue = Queue(maxsize=thread_count + 1)
    for _ in range(thread_count + 1):
        locker_queue.put(threading.Event())

    def put_task():
        last_lock = None
        # 将任务放入队列
        for item in iterations:
            current_lock = locker_queue.get()
            current_lock.clear()
            task_q.put((last_lock, item, current_lock), block=True)
            last_lock = current_lock

        for _ in range(thread_count):  # 在队列中加入None，以通知所有工作线程退出
            task_q.put((None, None, None))

        last_lock.wait()

    Insert_thread = threading.Thread(target=put_task)
    Insert_thread.start()

    def worker():
        while True:
            last_lock, item, cur_lock = task_q.get(block=True)
            if item is None:
                break
            result = task_fun(item)

            if last_lock is not None:
                last_lock.wait()
                locker_queue.put(last_lock)

            result_q.put((item, result))
            cur_lock.set()

    # 启动工作线程
    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for _ in iterations:
        yield result_q.get(block=True)


# def ddd(a):
#     time.sleep(0.5)
#     return a + 10
#
#
# for p in do_multitask([1, 2, 3, 4, 5, 6, 7, 8, 9], ddd, max_queue_buffer=5):
#     print(p)
#
# time.time()

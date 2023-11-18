import threading
import multiprocessing


class GxlDynamicThreadPool:
    def __init__(self, ):
        self._threads = []

    def add_thread(self, func: callable, fun_args: list):
        thread = threading.Thread(target=func, args=fun_args)
        self._threads.append(thread)

    def start(self):
        for thread in self._threads:
            thread.start()
        self._join()

    def _join(self):
        for thread in self._threads:
            thread.join()


class GxlFixedThreadPool:
    def __init__(self, num_threads: int):
        self.pool = multiprocessing.Pool(processes=num_threads)

    def apply_async(self, func: callable, fun_args: list):
        self.pool.apply_async(func, fun_args)

    def start(self):
        self.pool.close()
        self.pool.join()

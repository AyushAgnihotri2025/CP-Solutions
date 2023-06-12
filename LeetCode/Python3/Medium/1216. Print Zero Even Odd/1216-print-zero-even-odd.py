from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zeroSem = Semaphore()
        self.oddSem = Semaphore(0)       
        self.evenSem = Semaphore(0)       

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zeroSem.acquire()
            printNumber(0)
            (self.evenSem if i % 2 else self.oddSem).release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.evenSem.acquire()
            printNumber(i)
            self.zeroSem.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.oddSem.acquire()
            printNumber(i)
            self.zeroSem.release()
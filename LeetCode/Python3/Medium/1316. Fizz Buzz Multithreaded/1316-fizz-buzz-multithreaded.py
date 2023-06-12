import threading

class FizzBuzz:
    def __init__(self, n: int):      
        self.n = n
        self.f = threading.Lock()
        self.b = threading.Lock()
        self.fb = threading.Lock()
        self.f.acquire()
        self.b.acquire()
        self.fb.acquire()
        self.main = threading.Lock()

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.f.acquire()
            if self.n == 0 :
                return
            printFizz()
            self.main.release()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.b.acquire()
            if self.n == 0:
                return
            printBuzz()
            self.main.release()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.fb.acquire()
            if self.n == 0:
                return
            printFizzBuzz()
            self.main.release()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            #print("number:",i)
            self.main.acquire()
            if i % 15 == 0:
                self.fb.release()
            elif i % 3 == 0:
                self.f.release()
            elif i % 5 == 0:
                self.b.release()
            else:
                printNumber(i)
                self.main.release()
        self.main.acquire() 
        self.n = 0
        self.f.release()
        self.b.release()
        self.fb.release()
        return
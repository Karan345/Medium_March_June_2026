from threading import Event

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self._fizz = Event()
        self._buzz = Event()
        self._fizzbuzz = Event()
        self._number = Event()
        # call the reset function to start execution
        self._res()
    
    def _res(self):
        # if we're done, allow all threads to end
        if self.i > self.n:
            self._fizz.set()
            self._buzz.set()
            self._fizzbuzz.set()
            self._number.set()
        # otherwise, set the event for the appropriate thread
        else:
            if self.i % 3 == 0 and self.i % 5 == 0:
                self._fizzbuzz.set()
            elif self.i % 3 == 0:
                self._fizz.set()
            elif self.i % 5 == 0:
                self._buzz.set()
            else:
                self._number.set()


    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while self.i <= self.n:
            self._fizz.wait()
            if self.i <= self.n:
                printFizz()
                self.i += 1
                self._fizz.clear()
                self._res()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
    	while self.i <= self.n:
            self._buzz.wait()
            if self.i <= self.n:
                printBuzz()
                self.i += 1
                self._buzz.clear()
                self._res()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while self.i <= self.n:
            self._fizzbuzz.wait()
            if self.i <= self.n:
                printFizzBuzz()
                self.i += 1
                self._fizzbuzz.clear()
                self._res()
        

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i <= self.n:
            self._number.wait()
            if self.i <= self.n:
                printNumber(self.i)
                self.i += 1
                self._number.clear()
                self._res()
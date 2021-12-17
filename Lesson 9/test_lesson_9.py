import lesson_9

class Test_fib:

    def test_fib_3(self):
        assert lesson_9.fib(3) == 1

    def test_fib_4(self):
        assert lesson_9.fib(5) == 3
    
    def test_fib_20(self):
        assert lesson_9.fib(20) == 4181

    def test_fib_50(self):
        assert lesson_9.fib(50) == 7778742049
    
    def test_fib_100(self):
        assert lesson_9.fib(100) == 218922995834555169026
    
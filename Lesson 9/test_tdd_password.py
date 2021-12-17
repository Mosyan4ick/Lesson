import lesson_9

class Test_password:
    
    def test_len(self):
        assert lesson_9.password('qwert') == False
    
    def test_digit(self):
        assert lesson_9.password("1234567") == False

    def test_one_digit(self):
        assert lesson_9.password('qwertys') == False
    
    def test_password_word(self):
        assert lesson_9.password('12passwordcheck') == False
    
    def test_good_password(self):
        assert lesson_9.password('1one2for3') == True
        
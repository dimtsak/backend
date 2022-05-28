class DigitsInException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return f'{self.value} contains digits!'

class LettersInException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return f'{self.value} contains letters!'
    
def checkForDigits(char):
    for i in char :
        if i.isdigit():
            return DigitsInException(char)


def checkForLetters(char):
    i_letters = []
    for i in char :
        if not i.isdigit():
            i_letters.append(i)
    return f'{LettersInException(char)} {i_letters}'


class SmallLengthException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return f'{self.value} is less characters than we need!'
    
class BigLengthException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return f'{self.value} is more characters than we need!'

def smallLength(param,number):
    if len(param)<number:
        return f'{SmallLengthException(param)} you need at least {number} characters'
    
def bigLength(param,number):
    if len(param)>number:
        return f'{BigLengthException(param)} you need at most {number} characters'
        

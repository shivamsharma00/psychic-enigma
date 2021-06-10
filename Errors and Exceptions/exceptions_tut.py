#
#TODO : ERRORS AND EXCEPTIONS



#! Writing own exception
class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    
    if x < 5:
        raise ValueTooSmallError('Value is too small error', x)

try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)



#! Raising an exceptions
x = -5
# if x < 0:
#     raise Exception('X should be positive.')



#! OR we can use assert keyword.
# assert(x>=0), 'x is not positive'


try:
    x = 5/1
except Exception as e:
    print(e)



try:
    x = 5/1
    y = x + 1
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    #TODO : This block will run if no exception has raised.
    print('everything is fine')
finally:
    #TODO : This block will run if an exception is occurred or not.
    print('Cleaning Up...')


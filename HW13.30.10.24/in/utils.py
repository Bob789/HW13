# __name__  = main
# Play
def input_int_number():
    """Input an int from the user until it is valid"""
    x: int = 0
    while True:
        try:
            x = int(input('Enter number: '))
            break
        except:
            print('must be int')

def print_hello():
    """print 'my first function' """
    print('my first function')

# in the python file with print_hello func
#   add """ description .... """
# add another function get_int which inputs a number
#   add """ description .... """
# after the import , in main, help (<func1>) help(<mod>)
if __name__ == '__main__':
    print('alot of code ..............')
    print('alot of code ..............')
    print('alot of code ..............')
    print('alot of code ..............')
    print('alot of code ..............')
    print('alot of code ..............')

print('[utils] what is your name? ', __name__)
# print __name__
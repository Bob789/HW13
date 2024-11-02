
# 1
from utils import input_int_number, print_hello
# 2
import utils

help(input_int_number)
help(utils)

utils.input_int_number()
input_int_number()

print('after function')
for _ in range(3):
    print_hello()

print('bye')
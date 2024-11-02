# # 13
# SENTINEL: int = 0
# counter: int = 0
# while True:
#     try:
#         num: int = int(input('enter number [0 to exit]: '))
#         if num == SENTINEL:
#             break
#         # check if num is prime, if so add 1 to counter
#         if num < 2:
#             continue
#         is_prime: bool = True
#         # 36
#         # 6 * 6
#         # 12 * 3
#         # 49
#         # 8 * 9
#         for divider in range(2, num ** 0.5 + 1):
#             if num % divider == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             counter += 1
#     except:
#         print('bad number')
#
# print(f'{counter} prime numbers...')
#

# 15
# 5  * 3 = 5 + 5 + 5
# 15 / 5 = 15 -   5 -  5 - 5
#               (1)  (2)  (3)
#                10    5   0
# 10 / 5 = 10 - 5 - 5 .. 2
mehulak: int = 15  # input ...
mehalek: int = 5 # input ...
counter: int = 0
while mehulak > 0:
    mehulak = mehulak - mehalek # 15 10 5 0
    counter += 1 # 1 2 3
print(counter)

num1: float = 3.75  # input ...
num2: float = 5.1 # input ...
# handle negative numbers also ...
#                 3.75 -     3
shever_1: float = num1 - int(num1)
shever_2: float = num2 - int(num2)
# second way
# 9 % 2 = 1
# 3.75 % 1 = 0.75
shever_1: float = num1 % 1
shever_2: float = num2 % 1
if shever_1 > shever_2:
    print(shever_1)
elif shever_2 > shever_1:
    print(shever_2)
else:
    print('equal')










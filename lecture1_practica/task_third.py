from random import shuffle
from string import *
from itertools import *

for i in product(ascii_uppercase, repeat=3):
    for j in product(digits, repeat=3):
        for k in product('!@#$%^&*', repeat=2):
            password = list(i + j + k)
            shuffle(password)
            s = ''.join(password)
            print(s)
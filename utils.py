#Lib

import string
import random


def get_random_token(n=5):
    return ''.join([random.choice(string.ascii_letters) for _ in range(n)])

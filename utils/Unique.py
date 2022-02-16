import random
import string

def random_string_generator(): 
    chars = string.ascii_letters 
    size = 12
    return ''.join(random.choice(chars) for x in range(size))

import random

def make_bingo():
    rng = random.sample(range(1, 76), 24)
    num = rng[:12] + [0] + rng[12:]
    return tuple(num[:5]), tuple(num[5:10]), tuple(num[10:15]), tuple(num[15:20]), tuple(num[20:25])


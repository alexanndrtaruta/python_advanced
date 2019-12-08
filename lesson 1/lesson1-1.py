import random

n = random.randint(1, 100)
random_list = [i for i in range(0, n)]

for i in random_list:
    if i % 2 == 0:
        print(i)
    else:
        continue
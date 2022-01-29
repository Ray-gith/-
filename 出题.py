import os
import numpy as np

if os.path.isfile('题目.txt'):
    os.remove('题目.txt')
if os.path.isfile('答案.txt'):
    os.remove('答案.txt')

count = 0
while count < 100:
    try:
        a = np.random.randint(100)
        b = np.random.randint(a)
        c = np.random.randint(2)
        count += 1
        if c == 0:
            with open('题目.txt', 'a', encoding='u8') as f:
                print(f'({count}) {a} - {b} = ', file=f)
            with open('答案.txt', 'a', encoding='u8') as f:
                print(f'({count}) {a - b}', file=f)
        else:
            with open('题目.txt', 'a', encoding='u8') as f:
                print(f'({count}) {a} + {b} = ', file=f)
            with open('答案.txt', 'a', encoding='u8') as f:
                print(f'({count}) {a + b}', file=f)
    except:
        continue

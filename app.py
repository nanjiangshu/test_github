"""this script is for testing OpenShift continuous integration"""
import random
import time

from .app1.run import App1
from .app2.run import App2


def main():
    """main procedure"""
    loop = 0
    while loop < 10:
        loop += 1
        a = 1
        b = 100
        x1 = random.randint(a, b)
        x2 = random.randint(a, b)
        x3 = random.randint(a, b)
        ap1 = App1(x1, x2)
        ap2 = App2(x3)
        print(f"loop = {loop}, x1 = {x1}, x2 = {x2}, x3 = {x3}")
        ap1.plus()
        ap1.multiplication()
        ap2.sin()
        ap2.cos()
        ap2.pow10()
        ap2.pow16()
        ap2.tan()
        time.sleep(10)


if __name__ == '__main__':
    # create a while loop for continuous running
    main()

"""this script is for testing OpenShift continuous integration"""
import random
import time

from .app1.run import app1
from .app2.run import app2


def main():
    """main procedure"""
    loop = 0
    while loop < 10:
        loop += 1
        va = 1
        vb = 100
        vx1 = random.randint(va, vb)
        vx2 = random.randint(va, vb)
        vx3 = random.randint(va, vb)
        ap1 = app1(vx1, vx2)
        ap2 = app2(vx3)
        print(f"loop = {loop}, vx1 = {vx1}, vx2 = {vx2}, vx3 = {vx3}")
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

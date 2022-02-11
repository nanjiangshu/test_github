"""Testing script"""
from .app1.run import App1
from .app2.run import App2


def main():
    """Main procedure"""
    ap1 = App1(3, 8)
    ap2 = App2(15)
    ap1.plus()
    ap1.multiplication()
    ap2.sin()
    ap2.cos()
    ap2.pow10()
    ap2.pow16()
    ap2.tan()


if __name__ == '__main__':
    main()

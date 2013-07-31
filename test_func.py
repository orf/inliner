from inliner import inline


class SillyAdder(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    @inline
    def GetArg1(self):
        return self.arg1

    @inline
    def GetArg2(self):
        return self.arg2

    def AddNumbers(self):
        return self.GetArg1() + self.GetArg2()


def inline_test():
    adder = SillyAdder(1, 2)
    print adder.AddNumbers()


import dis
dis.dis(SillyAdder.AddNumbers)
print inline_test()
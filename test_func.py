from inliner import inline

@inline
def test():
    return 42

@inline
def addNumbers(arg1, arg2=0, arg3=4):
    return arg1 + arg2 + arg3

@inline
def concatString(arg1, arg2):
    return int(arg1 + arg2)


def inline_test():
    return test() + addNumbers(0, arg2=0) + concatString("1", "0")


import dis
dis.dis(inline_test)
print inline_test()
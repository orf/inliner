from inliner import inline


class SillyGetterSetter(object):
    def __init__(self, stuff):
        self.stuff = stuff

    @inline
    def setStuff(self, obj):
        self.stuff = obj

    @inline
    def getStuff(self):
        return self.stuff


def inline_test():
    a = SillyGetterSetter(1)
    a.setStuff(None)

    if a.getStuff() is None:
        return True

import dis
dis.dis(inline_test)
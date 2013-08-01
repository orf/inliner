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

@inline
def add_stuff(x, y):
    return x + y

def add_lots_of_numbers():
    for i in xrange(10):
         add_stuff(i, i+1)

import dis
dis.dis(add_lots_of_numbers)
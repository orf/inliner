from inliner import inline

class SillySetter(object):
    @inline
    def setStuff(self, obj):
        self.stuff = obj

def inline_test():
    a = SillySetter()
    a.setStuff(None)

import dis
dis.dis(inline_test)
from astmonkey.transformers import ParentNodeTransformer
from inliner.searcher import InlineMethodLocator
from inliner.transformer import FunctionInliner
import sys
import imp
import ast


class InlineLoader(object):
    def __init__(self, module):
        self.module = module

    def load_module(self, fullname):
        return self.module


class InlineImporter(object):
    def find_module(self, fullname, path):
        file, pathname, description = imp.find_module(
            fullname.split(".")[-1], path)

        src = file.read()
        tree = ast.parse(src)
        tree = ParentNodeTransformer().visit(tree)

        function_disoverer = InlineMethodLocator()
        function_disoverer.visit(tree)
        print "found funcs: %s" % function_disoverer.functions
        tree = FunctionInliner(function_disoverer.functions).visit(tree)

        module = sys.modules.setdefault(fullname,
                                        imp.new_module(fullname))
        module.__package__ = fullname.rpartition('.')[0]
        module.__file__ = file.name
        tree = ast.fix_missing_locations(tree)

        code = compile(tree, file.name, "exec")

        exec code in module.__dict__

        return InlineLoader(module)


sys.meta_path.append(InlineImporter())
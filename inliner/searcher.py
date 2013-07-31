from inliner import utils
import ast


class InlineMethodLocator(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}

    def visit_FunctionDef(self, node):
        if any(filter(lambda d: d.id == "inline", node.decorator_list)):
            func_name = utils.getFunctionName(node)
            self.functions[func_name] = node
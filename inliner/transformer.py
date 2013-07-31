from inliner import transformers, utils
import ast


class FunctionInliner(ast.NodeTransformer):
    def __init__(self, functions_to_inline):
        self.inline_funcs = functions_to_inline

    def visit_Call(self, node):
        func = node.func
        func_name = utils.getFunctionName(func)
        if func_name in self.inline_funcs:
            func_to_inline = self.inline_funcs[func_name]
            transformer = transformers.getFunctionHandler(func_to_inline)
            if transformer is not None:
                node = transformer.inline(node, func_to_inline)

        return node
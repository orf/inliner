from inliner import transformers
import ast


class FunctionInliner(ast.NodeTransformer):
    def __init__(self, functions_to_inline):
        self.inline_funcs = functions_to_inline

    def visit_Call(self, node):
        if hasattr(node.func, "id"):
            if node.func.id in self.inline_funcs:
                func_to_inline = self.inline_funcs[node.func.id]
                transformer = transformers.getFunctionHandler(func_to_inline)
                if transformer is not None:
                    node = transformer.inline(node, func_to_inline)

        return node
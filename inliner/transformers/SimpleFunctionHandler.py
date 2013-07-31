from inliner.transformers.BaseFunctionHandler import BaseFunctionHandler
import ast


class SimpleFunctionHandler(BaseFunctionHandler):
    def inline(self, node, func_to_inline):
        # Its a simple function we have here. That means it is one statement and we can simply replace the
        # call with the inlined functions body
        body = func_to_inline.body[0]
        if isinstance(body, ast.Return):
            body = body.value

        return self.replace_params_with_objects(body, func_to_inline, node)
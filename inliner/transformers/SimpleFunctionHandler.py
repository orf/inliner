from inliner.transformers.BaseFunctionHandler import BaseFunctionHandler


class SimpleFunctionHandler(BaseFunctionHandler):
    def inline(self, node, func_to_inline):
        # Its a simple function we have here. That means it is one statement and we can simply replace the
        # call with the inlined functions body
        return_value = func_to_inline.body[0].value
        return self.replace_params_with_objects(return_value, func_to_inline, node)
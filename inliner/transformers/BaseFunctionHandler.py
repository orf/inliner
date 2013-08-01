from collections import OrderedDict
import ast


class ParamReplacer(ast.NodeTransformer):
    def __init__(self, param_mapping):
        self.mapping = param_mapping

    def visit_Name(self, node):
        return self.mapping.get(node.id, node) or node


class BaseFunctionHandler(object):
    def replace_params_with_objects(self, target_node, inline_func, call_object):
        """
        target_node is some AST object, could be the return value of a function we are inlining.
        We need to inspect its parameters and create a dictionary then use ParamReplacer to replace
        all instances of those parameters with the local references to the objects being passed in
        """
        args = inline_func.args
        default_offset = len(args.args) - len(args.defaults)

        arg_mapping = OrderedDict()
        for idx, arg in enumerate(arg for arg in args.args if not arg.id == "self"):
            arg_mapping[arg.id] = None
            if idx >= default_offset:
                arg_mapping[arg.id] = args.defaults[idx - default_offset]

            if len(call_object.args) > idx:
                arg_mapping[arg.id] = call_object.args[idx]

        for keyword in call_object.keywords:
            arg_mapping[keyword.arg] = keyword.value

        if len([arg for arg in args.args if arg.id == "self"]):
            # Ok, get the name of "self" (the instance of the class we are using)
            new_mapping = OrderedDict({"self": call_object.func.value})
            new_mapping.update(arg_mapping)
            arg_mapping = new_mapping

        return ParamReplacer(arg_mapping).visit(target_node)
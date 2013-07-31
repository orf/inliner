from collections import OrderedDict
import ast


class ParamReplacer(ast.NodeTransformer):
    def __init__(self, param_mapping):
        self.mapping = param_mapping

    def visit_Name(self, node):
        return self.mapping.get(node.id, node) or node


class BaseFunctionHandler(object):
    def replace_params_with_objects(self, target_node, inline_func, call_object):
        # target_node is a Call() object. We need to inspect its parameters and create a dictionary
        # then use ParamReplacer to replace all instances of those parameters with the objects being passed in
        args = inline_func.args
        default_offset = len(args.args) - len(args.defaults)

        arg_mapping = OrderedDict()
        for idx, arg in enumerate(args.args):
            arg_mapping[arg.id] = None
            if idx >= default_offset:
                arg_mapping[arg.id] = args.defaults[idx - default_offset]

            if len(call_object.args) > idx:
                arg_mapping[arg.id] = call_object.args[idx]

        for keyword in call_object.keywords:
            arg_mapping[keyword.arg] = keyword.value

        return ParamReplacer(arg_mapping).visit(target_node)
import ast


def getFunctionName(func):
    if hasattr(func, "id"):
        return func.id
    else:
        if isinstance(func, ast.Attribute):
            return func.attr
        # Might be a class item
        return func.name
from SimpleFunctionHandler import SimpleFunctionHandler
import ast


def getFunctionHandler(func):
    # We take an ast.FunctionDef and return a FunctionHandler that is able to inline the function
    if len(func.body) == 1:
        # Looks like a simple function
        body = func.body[0]
        #if isinstance(body, (ast.Return, ast.expr)):
        return SimpleFunctionHandler()

    return None
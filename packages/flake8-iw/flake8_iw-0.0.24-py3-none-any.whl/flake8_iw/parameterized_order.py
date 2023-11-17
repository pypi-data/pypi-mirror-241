import ast

_IW_ERROR_MSG = "IW17 parameterized must be topmost decorator"


def visit_decorators(decorator_list: list, issue_list: list):
    for i, decorator in enumerate(decorator_list):
        if isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Attribute) and decorator.func.value.id == "parameterized" and i != 0:
            issue_list.append(
                (decorator.func.lineno, decorator.func.col_offset, _IW_ERROR_MSG)
            )
            break


class ParameterizedOrderFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.issues: list[tuple] = []
        super().__init__()

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        visit_decorators(node.decorator_list, self.issues)

        self.generic_visit(node)
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        visit_decorators(node.decorator_list, self.issues)

        self.generic_visit(node)
        return node

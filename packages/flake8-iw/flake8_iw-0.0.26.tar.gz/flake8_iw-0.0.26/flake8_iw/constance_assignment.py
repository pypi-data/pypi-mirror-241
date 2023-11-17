import ast

_IW_ERROR_MSG = "IW18 direct assignment to constance, use override_config() instead."


class ConstanceAssignmentFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.issues: list[tuple] = []

        super().__init__()

    def visit_Assign(self, node: ast.Assign) -> ast.Assign:
        if len(node.targets) and isinstance(node.targets[0], ast.Attribute):
            if isinstance(node.targets[0].value, ast.Name) and node.targets[0].value.id == "config":
                self.issues.append(
                    (node.targets[0].value.lineno, node.targets[0].value.col_offset, _IW_ERROR_MSG)
                )

        self.generic_visit(node)
        return node

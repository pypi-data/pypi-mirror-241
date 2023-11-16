import ast

_IW_ERROR_INDEX_TOGETHER = "IW13 Use of index_together instead of Options.indexes"
_IW_ERROR_UNIQUE_TOGETHER = "IW14 Use of unique_together instead of Options.constraints"


class TogetherCheckFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.in_meta = []
        self.issues: list[tuple] = []

        super().__init__()

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        if node.name == "Meta":
            self.in_meta.append(True)

        self.generic_visit(node)

        if node.name == "Meta":
            self.in_meta.pop()

        return node

    def visit_Name(self, node: ast.Name) -> ast.Name:
        if self.in_meta and node.id == "unique_together":
            self.issues.append(
                (node.lineno, node.col_offset, _IW_ERROR_UNIQUE_TOGETHER)
            )
        if self.in_meta and node.id == "index_together":
            self.issues.append(
                (node.lineno, node.col_offset, _IW_ERROR_INDEX_TOGETHER)
            )

        self.generic_visit(node)
        return node

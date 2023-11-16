import ast
from typing import Any

_IW_ERROR_SETUPCLASS_MSG = "IW16 do not use setUpClass and tearDownClass inside a test case"
_METHODS_TO_INSPECT = ["setUpClass", "tearDownClass"]


class PytestSetupAndTearDownFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.issues: list[tuple] = []
        self.is_test_case = False
        self.is_method_to_inspect = False
        self.has_super_call = False

        super().__init__()

    def visit_ClassDef(self, node: ast.Attribute) -> ast.ClassDef:
        # Check if class is a TestCase as it should have setUpClass or tearDownClass
        self.is_test_case = any(isinstance(base, ast.Name) and base.id.find("TestCase") != -1 for base in node.bases)
        self.generic_visit(node)

        if self.is_test_case:
            self.is_test_case = False

        return node

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        # Check if function is one of the methods to inspect and is in the test class
        self.has_setupclass_or_teardownclass = self.is_test_case and node.name in _METHODS_TO_INSPECT

        # after visiting nodes inside the function check if a super call was made
        if self.has_setupclass_or_teardownclass:
            self.issues.append((node.lineno, node.col_offset, _IW_ERROR_SETUPCLASS_MSG))

        return node

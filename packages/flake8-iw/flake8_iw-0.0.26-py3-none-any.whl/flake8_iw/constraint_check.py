import ast

_IW_ERROR_DB_INDEX = "IW11 Use of db_index=True"
_IW_ERROR_UNIQUE = "IW12 Use of unique=True"

FIELD_TYPES = {
    "ForeignKey",
    "OneToOneField",
    "CharField",
    "BigIntegerField",
    "BinaryField",
    "BooleanField",
    "DateField",
    "DateTimeField",
    "DecimalField",
    "DurationField",
    "EmailField",
    "FileField",
    "FilePathField",
    "FloatField",
    "GenericIPAddressField",
    "ImageField",
    "IntegerField",
    "NullBooleanField",
    "PositiveIntegerField",
    "PositiveSmallIntegerField",
    "SlugField",
    "SmallIntegerField",
    "TextField",
    "TimeField",
    "URLField",
    "UUIDField",
}


class ConstraintCheckFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.issues: list[tuple] = []

        super().__init__()

    def visit_Call(self, node: ast.Call) -> ast.Call:
        is_foreign_key = (isinstance(node.func, ast.Attribute) and node.func.attr in FIELD_TYPES) or (
            isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in FIELD_TYPES
        )

        if is_foreign_key:
            if any([keyword.arg == "db_index" and keyword.value.value is True for keyword in node.keywords]):
                self.issues.append(
                    (node.func.lineno, node.func.col_offset, _IW_ERROR_DB_INDEX)
                )

            if any([keyword.arg == "unique" and keyword.value.value is True for keyword in node.keywords]):
                self.issues.append(
                    (node.func.lineno, node.func.col_offset, _IW_ERROR_UNIQUE)
                )

        self.generic_visit(node)
        return node

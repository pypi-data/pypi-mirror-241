import ast

_IW_ERROR_FACTORY_TIMEZONE_NOW_MSG = "IW15 use of timezone.now in factory, call from LazyAttribute or LazyFunction"


class FactoryTimezoneNowFinder(ast.NodeVisitor):
    def __init__(self, _, *args, **kwargs) -> None:
        self.issues: list[tuple] = []

        self._is_factory = False
        self._is_lazy_fn_or_attr = False

        super().__init__()

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        is_factory = node.name.endswith("Factory")
        if is_factory:
            self._is_factory = True

        self.generic_visit(node)
        if is_factory:
            self._is_factory = False
        return node

    def visit_Assign(self, node: ast.Assign) -> ast.Assign:
        # from django.utils import timezone
        # class TestFactory(factory.django.DjangoModelFactory):
        #    starts_at = timezone.now()
        if (self._is_factory and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Attribute)
                and isinstance(node.value.func.value, ast.Name)
                and node.value.func.value.id == "timezone"
                and node.value.func.attr == "now"):
            self.issues.append(
                (node.value.func.value.lineno, node.value.func.value.col_offset, _IW_ERROR_FACTORY_TIMEZONE_NOW_MSG)
            )

        # from django.utils.timezone import now
        # class TestFactory(factory.django.DjangoModelFactory):
        #    starts_at = now()
        if (
                self._is_factory
                and isinstance(node.value, ast.Call)
                and isinstance(node.value.func, ast.Name)
                and node.value.func.id == "now"
        ):
            self.issues.append(
                (node.value.func.lineno, node.value.func.col_offset, _IW_ERROR_FACTORY_TIMEZONE_NOW_MSG)
            )

        self.generic_visit(node)

        return node

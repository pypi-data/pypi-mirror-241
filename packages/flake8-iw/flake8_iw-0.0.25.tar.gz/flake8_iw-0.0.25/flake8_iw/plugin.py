import sys

from .bulk_batch_update import BulkUpdateFinder
from .datetime_now import DatetimeNowFinder
from .datetime_replace_tzinfo import DatetimeReplaceTzinfoFinder
from .factory_timezone_now import FactoryTimezoneNowFinder
from .freeze_time import ForbiddenTimePatchFinder
from .logging import ErrorLoggerFinder
from .patch_call import ForbiddenPatchCallFinder
from .shared_task import SharedTaskFinder
from .timezone_activate import TimezoneActivateNowFinder
from .foreign_key_check import ForeignKeyCheckFinder
from .constraint_check import ConstraintCheckFinder
from .together_check import TogetherCheckFinder
from .pytest_setup_class import PytestSetupAndTearDownFinder
from .parameterized_order import ParameterizedOrderFinder

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


class Plugin(object):
    name = "flake8_iw"
    version = importlib_metadata.version("flake8_iw")
    rules = (
        ForbiddenPatchCallFinder,
        ForbiddenTimePatchFinder,
        ErrorLoggerFinder,
        DatetimeNowFinder,
        DatetimeReplaceTzinfoFinder,
        BulkUpdateFinder,
        SharedTaskFinder,
        TimezoneActivateNowFinder,
        ForeignKeyCheckFinder,
        ConstraintCheckFinder,
        TogetherCheckFinder,
        FactoryTimezoneNowFinder,
        PytestSetupAndTearDownFinder,
        ParameterizedOrderFinder,
    )

    def __init__(self, tree) -> None:
        self.tree = tree

    def run(self):
        for rule_class in self.rules:
            parser = rule_class(self.tree)
            parser.visit(self.tree)

            for lineno, column, msg in parser.issues:
                yield (lineno, column, msg, Plugin)

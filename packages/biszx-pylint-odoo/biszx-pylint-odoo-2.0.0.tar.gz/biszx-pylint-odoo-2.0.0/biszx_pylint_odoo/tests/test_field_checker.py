from functools import reduce

from .. import messages
from . import settings
from .utils import run_pylint

DEFAULT_EXTRA_OPTIONS = [
    '--disable=all',
    f'''--enable={reduce(
        lambda a, v: f'{a},{v[1]}',
        messages.FIELD_CHECKER_MSGS.values(),
        ''
    )[1:]}''',
]


def test_field_checker():
    pylint_res = run_pylint(
        [f'./{settings.TEST_DATA_PATH}/field_checker_data.py'],
        extra_params=DEFAULT_EXTRA_OPTIONS,
        verbose=True,
    )
    real_errors = pylint_res.linter.stats.by_msg
    assert real_errors == {
        'biszx-relation2one-field-name': 3,
        'biszx-relation2many-field-name': 6,
        'biszx-boolean-field-name': 1,
        'biszx-date-field-name': 1,
        'biszx-datetime-field-name': 1,
    }

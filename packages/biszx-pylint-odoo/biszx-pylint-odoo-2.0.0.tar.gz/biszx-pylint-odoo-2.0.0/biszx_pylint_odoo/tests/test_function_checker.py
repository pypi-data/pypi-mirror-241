from functools import reduce

from .. import messages
from . import settings
from .utils import run_pylint

DEFAULT_EXTRA_OPTIONS = [
    '--disable=all',
    f'''--enable={reduce(
        lambda a, v: f'{a},{v[1]}',
        messages.FUNCTION_CHECKER_MSGS.values(),
        ''
    )[1:]}''',
]


def test_function_checker():
    pylint_res = run_pylint(
        [f'./{settings.TEST_DATA_PATH}/function_checker_data.py'],
        extra_params=DEFAULT_EXTRA_OPTIONS,
        verbose=True,
    )
    real_errors = pylint_res.linter.stats.by_msg
    assert real_errors == {
        'biszx-domain-func-name': 1,
        'biszx-default-func-name': 2,
        'biszx-search-func-name': 1,
        'biszx-compute-func-name': 2,
        'biszx-onchange-func-name': 1,
        'biszx-constrains-func-name': 1,
        'biszx-inverse-func-name': 1,
    }

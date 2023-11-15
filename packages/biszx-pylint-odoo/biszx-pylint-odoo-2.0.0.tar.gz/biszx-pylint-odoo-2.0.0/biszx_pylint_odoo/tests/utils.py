import os
import sys
import warnings
from io import StringIO

import pytest
from pylint.reporters.text import TextReporter
from pylint.testutils._run import _Run as Run
from pylint.testutils.utils import _patch_streams

from . import settings


def _run_pylint(args, out, reporter):
    with _patch_streams(out):
        with pytest.raises(SystemExit) as ctx_mgr:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                Run(args, reporter=reporter)
        return int(ctx_mgr.value.code)


def run_pylint(
    paths,
    extra_params: list = [],
    verbose=False,
    rcfile: str = '',
):
    for path in paths:
        if not os.path.exists(path):
            raise OSError('Path "{path}" not found.'.format(path=path))

    if rcfile:
        extra_params.append(f'--rcfile={rcfile}')

    sys.path.extend(paths)
    cmd = settings.DEFAULT_OPTIONS + extra_params + paths
    reporter = TextReporter(StringIO())
    with open(os.devnull, 'w', encoding='UTF-8') as f_dummy:
        _run_pylint(cmd, f_dummy, reporter=reporter)
    if verbose:
        reporter.out.seek(0)
        print(reporter.out.read())
    return reporter

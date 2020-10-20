# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.jay_module.tests.test_jay_module import suite  # noqa: E501
except ImportError:
    from .test_jay_module import suite

__all__ = ['suite']

# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .test import hello
__all__ = ['register']



def register():
    Pool.register(
        module='jay_module', type_='model')
    Pool.register(
        module='jay_module', type_='wizard')
    Pool.register(
        module='jay_module', type_='report')

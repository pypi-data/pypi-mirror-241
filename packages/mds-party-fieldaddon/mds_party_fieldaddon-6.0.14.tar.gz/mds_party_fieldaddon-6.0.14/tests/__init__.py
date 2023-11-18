# This file is part of the party-fieldaddon module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


import trytond.tests.test_tryton
import unittest

from trytond.modules.party_fieldaddon.tests.test_party import PartyTestCase


__all__ = ['suite']


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(PartyTestCase))
    return suite

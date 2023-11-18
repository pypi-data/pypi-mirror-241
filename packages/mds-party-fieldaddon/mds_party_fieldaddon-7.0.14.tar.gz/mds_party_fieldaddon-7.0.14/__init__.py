# -*- coding: utf-8 -*-
# This file is part of the party-fieldaddon module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from .party import Party, RelationAll
from .address import Address
from .configuration import (
    Configuration, ConfigurationFieldaddon, CompanyFieldaddon)


def register():
    Pool.register(
        Party,
        Address,
        Configuration,
        ConfigurationFieldaddon,
        RelationAll,
        module='party_fieldaddon', type_='model')
    Pool.register(
        CompanyFieldaddon,
        module='party_fieldaddon', type_='model', depends=['company'])

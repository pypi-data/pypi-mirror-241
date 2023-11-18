# -*- coding: utf-8 -*-
# This file is part of the party-fieldaddon module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import ModelSQL, fields
from trytond.model import ValueMixin
from trytond.pool import Pool, PoolMeta
try:
    from trytond.modules.company.model import CompanyValueMixin
except Exception:
    CompanyValueMixin = None

company_relation = fields.Many2One(
    model_name='party.relation.type', string='Company Relationship',
    help='Relationship type for linking an employee to their company.')


class Configuration(metaclass=PoolMeta):
    __name__ = 'party.configuration'

    company_relation = fields.MultiValue(company_relation)

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field in ['company_relation']:
            return pool.get('party_fieldaddon.config')
        return super(Configuration, cls).multivalue_model(field)

# end Configuration


class ConfigurationFieldaddon(ModelSQL, ValueMixin):
    'Party Configuration Field Addon'
    __name__ = 'party_fieldaddon.config'

    company_relation = company_relation

# end ConfigurationFieldaddon


if CompanyValueMixin:
    class CompanyFieldaddon(CompanyValueMixin, metaclass=PoolMeta):
        __name__ = 'party_fieldaddon.config'

        @classmethod
        def default_company(cls):
            """ current company
            """
            return Transaction().context.get('company')

    # end CompanyFieldaddon
else :
    class CompanyFieldaddon(metaclass=PoolMeta):
        __name__ = 'party_fieldaddon.config'

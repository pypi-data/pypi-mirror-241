# -*- coding: utf-8 -*-
# This file is part of the party-fieldaddon module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import PoolMeta


class Address(metaclass=PoolMeta):
    __name__ = 'party.address'

    def _get_address_substitutions(self):
        """ add fields to substitions
        """
        r1 = super(Address, self)._get_address_substitutions()

        pfields = {}
        party = getattr(self, 'party', None)
        if not isinstance(party, type(None)):
            pfields = party.vcard_field_name()
            pfields.update({
                'nickname': party.vcard_field_nickname() or '',
                'department': party.pfadepartment or '',
                'company': party.vcard_field_org() or '',
                })

        # mapping
        f_lst = [
                ('firstname', 'givenname'),
                ('familyname', 'familyname'),
                ('additionalnames', 'additionalnames'),
                ('nickname', 'nickname'),
                ('honorprefix', 'honorprefix'),
                ('honorsuffix', 'honorsuffix'),
                ('department', 'department'),
                ('company', 'company'),
            ]

        # update substitution dict
        for f1 in f_lst:
            (to_field, from_field) = f1

            val1 = pfields.get(from_field, '')
            if isinstance(val1, type([])):
                val1 = ' '.join(val1)
            r1[to_field] = val1
            r1[to_field.upper()] = val1.upper()
        return r1

# end Address

# -*- coding: utf-8 -*-
# This file is part of the party-fieldaddon module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
DEF_NONE = None


party_names = [
    'name', 'pfafirstname', 'pfafamilyname', 'pfaadditionalnames',
    'pfanickname', 'pfadepartment', 'pfacompany']


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    pfafirstname = fields.Char(string='First Name', help='Given Name')
    pfafamilyname = fields.Char(string='Family Name')
    pfaadditionalnames = fields.Char(
        string='Additional Names',
        help='2nd, 3rd and other names; comma-separated list')
    pfanickname = fields.Char(string='Nickname')
    pfadepartment = fields.Char(string='Department')
    pfacompany = fields.Char(string='Company')
    pfakeepupdt = fields.Boolean(
        string='Keep company updated',
        help="Updates the 'Company' field when the connected " +
        "party is changed.")
    pfacompanylink = fields.Function(fields.Many2One(
        string='Company Link', model_name='party.party',
        readonly=True),
        'on_change_with_pfacompanylink', searcher='search_pfacompanylink')
    pfabday = fields.Date(string='Birthday')
    pfahonpre = fields.Char(
        string='Honorific Prefixes',
        help="Prefixes like 'Dr.', 'Prof.' - as a comma-separated list")
    pfahonsuf = fields.Char(
        string='Honorific Suffixes',
        help="Suffixes like 'Jr.', 'M.D.' - as a comma-separated list")

    @classmethod
    def __register__(cls, module_name):
        super(Party, cls).__register__(module_name)
        cls.migrate_pfacompanylink(module_name)

    @classmethod
    def migrate_pfacompanylink(cls, module_name):
        """ remove column 'pfacompanylink'
        """
        pool = Pool()
        Party = pool.get('party.party')
        RelationshipType = pool.get('party.relation.type')
        Relation = pool.get('party.relation')
        Configuration = pool.get('party.configuration')
        tal_party = Party.__table__()
        table_hdl = cls.__table_handler__(module_name)
        cursor = Transaction().connection.cursor()

        if table_hdl.column_exist('pfacompanylink'):

            # check if 'pfacompanylink' is used
            query = tal_party.select(
                    tal_party.id,
                    tal_party.pfacompanylink,
                    where=tal_party.pfacompanylink != DEF_NONE)
            cursor.execute(*query)
            records = cursor.fetchall()

            if len(records) == 0:
                # nothing to do, stop
                table_hdl.drop_column('pfacompanylink')
                return

            # select relation-type (or create it)
            cfg1 = Configuration.get_singleton()
            if cfg1 and cfg1.company_relation:
                rel_type = cfg1.company_relation.id
            else:
                rel_type, = RelationshipType.create([{
                    'name': 'Employee of'}])
                if not cfg1:
                    cfg1 = Configuration()
                cfg1.company_relation = rel_type
                cfg1.save()
                rel_type = rel_type.id

            # find existing link-targets
            target_records = Party.search([
                ('id', 'in', [x[1] for x in records])])

            Relation.create([{
                'type': rel_type,
                'to': x[1],
                'from_': x[0],
                }
                for x in records
                if x[1] in [y.id for y in target_records]
                ])
            table_hdl.drop_column('pfacompanylink')

    @classmethod
    def default_pfakeepupdt(cls):
        """ default False
        """
        return False

    @fields.depends('relations')
    def on_change_with_pfacompanylink(self, name=None):
        """ show 1st company-link
        """
        Configuration = Pool().get('party.configuration')
        cfg1 = Configuration.get_singleton()

        if cfg1:
            if cfg1.company_relation:
                for rel in self.relations:
                    if rel.type and rel.to and (
                            rel.type.id == cfg1.company_relation.id):
                        return rel.to.id

    @classmethod
    def search_pfacompanylink(cls, name, clause):
        """ search in company-link
        """
        Configuration = Pool().get('party.configuration')
        cfg1 = Configuration.get_singleton()

        if cfg1:
            if cfg1.company_relation:
                query = [
                    ('relations.type', '=', cfg1.company_relation),
                    ('relations.to' +
                        clause[0][len('pfacompanylink'):],) + tuple(
                        clause[1:]),
                    ]
                return query
        return [('id', '=', -1)]

    @fields.depends(*party_names)
    def on_change_pfafirstname(self):
        self.name = self.get_rec_name(None)

    @fields.depends(*party_names)
    def on_change_pfafamilyname(self):
        self.name = self.get_rec_name(None)

    @fields.depends(*party_names)
    def on_change_pfaadditionalnames(self):
        self.name = self.get_rec_name(None)

    @fields.depends(*party_names)
    def on_change_pfadepartment(self):
        self.name = self.get_rec_name(None)

    @fields.depends(*party_names)
    def on_change_pfacompany(self):
        self.name = self.get_rec_name(None)

    def get_rec_name(self, name):
        """ generate name of party
        """
        l1 = ['pfafamilyname', 'pfafirstname']
        l2 = ['pfacompany', 'pfadepartment']

        # name
        l3 = []
        for i in l1:
            v1 = getattr(self, i)
            if isinstance(v1, type(None)):
                continue
            if v1 == '':
                continue
            if i == 'pfaadditionalnames':
                l3.append(' '.join([x.strip() for x in v1.split(',')]))
            else:
                l3.append(v1)
        t1 = ', '.join(l3)

        # company
        l3 = []
        for i in l2:
            v1 = getattr(self, i)
            if isinstance(v1, type(None)):
                continue
            if v1 == '':
                continue
            l3.append(v1)
        if len(l3) > 0:
            if len(t1) == 0:
                t1 += ', '.join(l3)
            else:
                t1 += ' [%s]' % (', '.join(l3))
        t1 = t1.strip()
        if len(t1) == 0:
            if hasattr(self, 'code'):
                t1 = super(Party, self).get_rec_name(name)
            else:
                t1 = '-'
        return t1

    @classmethod
    def search_rec_name(cls, name, clause):
        """ extend search in rec_name for new fields
        """
        query = super(Party, cls).search_rec_name(name, clause)
        query2 = [
                ('pfafirstname',) + tuple(clause[1:]),
                ('pfafamilyname',) + tuple(clause[1:]),
                ('pfaadditionalnames',) + tuple(clause[1:]),
                ('pfanickname',) + tuple(clause[1:]),
                ('pfacompany',) + tuple(clause[1:]),
                ('pfadepartment',) + tuple(clause[1:]),
            ]

        qu_ok = False
        if isinstance(query, type([])):
            if query[0] == 'OR':
                query.extend(query2)
                qu_ok = True

        if qu_ok is False:
            query3 = ['OR', query]
            query3.extend(query2)
            query = query3

        return query

    @classmethod
    def write(cls, *args):
        """ update linked parties
        """
        Party2 = Pool().get('party.party')

        actions = iter(args)
        to_write = []
        for parties, values in zip(actions, actions):
            if 'name' in values:
                p_lst = Party2.search([
                    ('pfakeepupdt', '=', True),
                    ('pfacompanylink.id', 'in', [x.id for x in parties]),
                    ])
                if p_lst:
                    to_write.extend([p_lst, {'pfacompany': values['name']}])
        if to_write:
            Party2.write(*to_write)

        super(Party, cls).write(*args)

    def vcard_field_name(self):
        """ get contents for vcard-field FN, N
        """
        return {
            'fullname': self.name or '',
            'familyname': self.pfafamilyname or '',
            'givenname': self.pfafirstname or '',
            'additionalnames': [
                x.strip() for x in (self.pfaadditionalnames or '').split(',')
                if len(x.strip()) > 0],
            'honorprefix': [
                x.strip() for x in (self.pfahonpre or '').split(',')
                if len(x.strip()) > 0],
            'honorsuffix': [
                x.strip() for x in (self.pfahonsuf or '').split(',')
                if len(x.strip()) > 0],
            }

    def vcard_field_nickname(self):
        """ get contents for vcard-field NICKNAME
        """
        return self.pfanickname

    def vcard_field_org(self):
        """ get contents for vcard-field ORG
        """
        return self.pfacompany

    def vcard_field_birthday(self):
        """ get contents for vcard-field BDAY
        """
        return self.pfabday

# end Party


class RelationAll(metaclass=PoolMeta):
    __name__ = 'party.relation.all'

    @classmethod
    def create(cls, vlist):
        """ update 'pfacompany'
        """
        pool = Pool()
        Configuration = pool.get('party.configuration')
        Party = pool.get('party.party')

        cfg1 = Configuration.get_singleton()
        if cfg1:
            if cfg1.company_relation:
                to_write_party = []

                for values in vlist:
                    if len(set({'to', 'from_', 'type'}).intersection(
                            set(values.keys()))) == 3:
                        if values.get('type', -1) == cfg1.company_relation.id:
                            to_party = values.get('to', None)
                            from_party = values.get('from_', None)

                            if (not to_party) or (not from_party):
                                continue
                            to_party = Party(to_party)
                            from_party = Party(from_party)

                            if from_party.pfakeepupdt:
                                to_write_party.extend([
                                    [from_party],
                                    {
                                        'pfacompany': to_party.name,
                                    }])
                if to_write_party:
                    Party.write(*to_write_party)

        return super(RelationAll, cls).create(vlist)

# end RelationAll

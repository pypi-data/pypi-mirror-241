# -*- coding: utf-8 -*-
# This file is part of the party-fieldaddon module for Tryton from m-ds.de.
# The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.transaction import Transaction
from datetime import date


class PartyTestCase(ModuleTestCase):
    'Test party module'
    module = 'party_fieldaddon'

    @with_transaction()
    def test_fieldaddon_create_party(self):
        """ create party, fill fields, check rec_name
        """
        Party = Pool().get('party.party')

        Party.create([{
            'name': 'full name',
            'pfafirstname': 'givenname',
            'pfafamilyname': 'family name',
            'pfaadditionalnames': '2nd, 3rd names',
            'pfanickname': 'nickname',
            'pfacompany': 'company',
            'pfadepartment': 'department'}])

        p_lst = Party.search([])
        self.assertEqual(len(p_lst), 1)
        self.assertEqual(p_lst[0].name, 'full name')
        self.assertEqual(p_lst[0].pfafirstname, 'givenname')
        self.assertEqual(p_lst[0].pfafamilyname, 'family name')
        self.assertEqual(p_lst[0].pfaadditionalnames, '2nd, 3rd names')
        self.assertEqual(p_lst[0].pfanickname, 'nickname')
        self.assertEqual(p_lst[0].pfacompany, 'company')
        self.assertEqual(p_lst[0].pfadepartment, 'department')

        self.assertEqual(
            p_lst[0].rec_name,
            'family name, givenname [company, department]')

        p2_lst = Party.search([
                ('rec_name', 'ilike', '%nick%')
            ])
        self.assertEqual(len(p2_lst), 1)

        # check list-behavior of additional names
        p_lst[0].pfaadditionalnames = '2nd-name, 3rd-name'
        p_lst[0].save()
        self.assertEqual(
            p_lst[0].rec_name,
            'family name, givenname [company, department]')

    @with_transaction()
    def test_fieldaddon_empty_fields(self):
        """ create party, no field set, check rec_name
        """
        Party = Pool().get('party.party')

        p1 = Party()
        p1.save()

        p_lst = Party.search([])
        self.assertEqual(len(p_lst), 1)
        self.assertEqual(p_lst[0].rec_name, '[%s]' % p_lst[0].code)

    @with_transaction()
    def test_fieldaddon_migrate1(self):
        """ migrate used 'pfacompanylink'
        """
        pool = Pool()
        Party = pool.get('party.party')
        RelationshipType = pool.get('party.relation.type')
        Relation = pool.get('party.relation')
        Configuration = pool.get('party.configuration')
        tab_party = Party.__table__()
        table_hdl = Party.__table_handler__('party_fieldaddon')
        cursor = Transaction().connection.cursor()

        # add column 'pfacompanylink' to check migration
        table_hdl.add_column('pfacompanylink', 'INTEGER')

        # two parties
        company, employee, = Party.create([{
            'name': 'Company',
            'addresses': [('create', [{}])]
            }, {
            'name': 'Employee',
            'addresses': [('create', [{}])]}])

        # add link old style
        query = tab_party.update(
                columns=[tab_party.pfacompanylink],
                values=[company.id],
                where=tab_party.id == employee.id)
        cursor.execute(*query)

        # migrate
        Party.migrate_pfacompanylink('party_fieldaddon')

        # we should have now a new relation-type
        rel_type, = RelationshipType.search([])
        self.assertEqual(rel_type.name, 'Employee of')

        # employee has a link to company
        self.assertEqual(employee.pfacompanylink.name, 'Company')
        self.assertEqual(employee.pfacompanylink.rec_name, 'Company')

        # a relation exists
        relation, = Relation.search([])
        self.assertEqual(relation.type.name, 'Employee of')
        self.assertEqual(relation.to.name, 'Company')
        self.assertEqual(relation.from_.name, 'Employee')

        # config is set
        cfg1 = Configuration.get_singleton()
        self.assertEqual(cfg1.company_relation.name, 'Employee of')

    @with_transaction()
    def test_fieldaddon_company_link(self):
        """ create parties, link them together
        """
        pool = Pool()
        Party = pool.get('party.party')
        RelationshipType = pool.get('party.relation.type')
        Configuration = pool.get('party.configuration')

        rel_type, rel_party2, = RelationshipType.create([
            {'name': 'to Company'},
            {'name': 'to Party 2'}])

        cfg1 = Configuration()
        cfg1.company_relation = rel_type
        cfg1.save()

        company, = Party.create([{
            'name': 'Company',
            'addresses': [('create', [{
                'street': 'Street 1',
                }])],
            }])
        party2, = Party.create([{
            'name': 'Party 2',
            'addresses': [('create', [{}])],
            }])

        employee, = Party.create([{
            'name': 'Employee',
            'addresses': [('create', [{}])],
            'pfakeepupdt': True,
            'relations': [('create', [{
                'to': company.id,
                'type': rel_type.id,
                }, {
                'to': party2.id,
                'type': rel_party2.id,
                }])]}])

        self.assertEqual(company.name, 'Company')
        self.assertEqual(company.relations, ())
        self.assertEqual(company.pfacompany, None)
        self.assertEqual(employee.name, 'Employee')
        # 'pfacompany' was written by add-link-action
        self.assertEqual(employee.pfacompany, 'Company')
        self.assertEqual(len(employee.relations), 2)
        self.assertEqual(employee.relations[0].to.name, 'Company')
        self.assertEqual(employee.relations[0].type.name, 'to Company')
        self.assertEqual(employee.relations[1].to.name, 'Party 2')
        self.assertEqual(employee.relations[1].type.name, 'to Party 2')
        self.assertEqual(employee.pfacompanylink.name, 'Company')

        # search on companylink
        self.assertEqual(
            Party.search_count([('pfacompanylink', '=', 'Company')]),
            1)
        self.assertEqual(
            Party.search_count([('pfacompanylink.rec_name', '=', 'Company')]),
            1)
        self.assertEqual(
            Party.search_count([('pfacompanylink.name', '=', 'Company')]),
            1)
        self.assertEqual(
            Party.search_count([('pfacompanylink.name', '=', 'nope')]),
            0)
        self.assertEqual(
            Party.search_count([
                ('pfacompanylink.addresses.street', 'ilike', 'street%')]),
            1)

        # update company --> should update 'pfacompany' of employee
        self.assertEqual(employee.pfacompany, 'Company')
        self.assertEqual(employee.name, 'Employee')
        self.assertEqual(company.name, 'Company')

        Party.write(*[[company], {'name': 'Company 2'}])
        employee, = Party.browse([employee])
        self.assertEqual(employee.pfacompany, 'Company 2')
        self.assertEqual(employee.name, 'Employee')
        self.assertEqual(company.name, 'Company 2')

        p_lst = Party.search([], order=[('name', 'ASC')])
        self.assertEqual(len(p_lst), 3)
        self.assertEqual(p_lst[0].name, 'Company 2')
        self.assertEqual(p_lst[0].pfacompanylink, None)
        self.assertEqual(p_lst[0].pfacompany, None)
        self.assertEqual(p_lst[1].name, 'Employee')
        self.assertEqual(p_lst[1].pfacompanylink.name, 'Company 2')
        self.assertEqual(p_lst[1].pfacompany, 'Company 2')
        self.assertEqual(p_lst[2].name, 'Party 2')

        # delete party - should clear the link
        Party.delete([p_lst[0]])

        # check employee-party
        self.assertEqual(employee.pfacompanylink, None)
        self.assertEqual(employee.pfacompany, 'Company 2')
        self.assertEqual(employee.name, 'Employee')

    @with_transaction()
    def test_fieldaddon_address_subst_fields(self):
        """ create parties, check dictionary for address substitions
        """
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')
        Country = pool.get('country.country')
        AddressFormat = pool.get('party.address.format')

        country1 = Country.create([{
            'name': 'Germany',
            'code': 'DE',
            'code3': 'DEU',
            'code_numeric': '276',
            }])

        p1 = Party.create([{
            'name': 'full name',
            'pfafirstname': 'givenname',
            'pfafamilyname': 'family name',
            'pfaadditionalnames': '2nd, 3rd names',
            'pfanickname': 'nickname',
            'pfacompany': 'company',
            'pfadepartment': 'department',
            'pfahonpre': 'prefix',
            'pfahonsuf': 'suffix'}])
        Address.create([{
            'party': p1[0],
            'street': 'Street 1',
            'postal_code': '12345',
            'city': 'City',
            'country': country1[0]}])

        p_lst = Party.search([], order=[('name', 'ASC')])
        self.assertEqual(len(p_lst), 1)
        self.assertEqual(p_lst[0].name, 'full name')
        self.assertEqual(p_lst[0].pfafirstname, 'givenname')
        self.assertEqual(p_lst[0].pfafamilyname, 'family name')
        self.assertEqual(p_lst[0].pfaadditionalnames, '2nd, 3rd names')
        self.assertEqual(p_lst[0].pfanickname, 'nickname')
        self.assertEqual(p_lst[0].pfacompany, 'company')
        self.assertEqual(p_lst[0].pfadepartment, 'department')
        self.assertEqual(p_lst[0].pfahonpre, 'prefix')
        self.assertEqual(p_lst[0].pfahonsuf, 'suffix')
        self.assertEqual(len(p_lst[0].addresses), 1)
        self.assertEqual(p_lst[0].addresses[0].street, 'Street 1')

        r1 = p_lst[0].addresses[0]._get_address_substitutions()
        self.assertEqual(r1['firstname'], 'givenname')
        self.assertEqual(r1['familyname'], 'family name')
        self.assertEqual(r1['additionalnames'], '2nd 3rd names')
        self.assertEqual(r1['nickname'], 'nickname')
        self.assertEqual(r1['honorprefix'], 'prefix')
        self.assertEqual(r1['honorsuffix'], 'suffix')
        self.assertEqual(r1['department'], 'department')
        self.assertEqual(r1['company'], 'company')

        self.assertEqual(r1['FIRSTNAME'], 'GIVENNAME')
        self.assertEqual(r1['FAMILYNAME'], 'FAMILY NAME')
        self.assertEqual(r1['ADDITIONALNAMES'], '2ND 3RD NAMES')
        self.assertEqual(r1['NICKNAME'], 'NICKNAME')
        self.assertEqual(r1['HONORPREFIX'], 'PREFIX')
        self.assertEqual(r1['HONORSUFFIX'], 'SUFFIX')
        self.assertEqual(r1['DEPARTMENT'], 'DEPARTMENT')
        self.assertEqual(r1['COMPANY'], 'COMPANY')

        AddressFormat.create([{
            'country_code': country1[0].code,
            'language_code': country1[0].code.lower(),
            'format_': """${name}
${honorprefix} ${firstname} ${familyname}
${nickname}
${street}
${postal_code} ${city}
${subdivision}
${COUNTRY}
"""}])
        with Transaction().set_context({
                'language': 'de'}):
            self.assertEqual(
                p_lst[0].address_get().get_full_address(None),
                """prefix givenname family name
nickname
Street 1
12345 City
GERMANY""")

    @with_transaction()
    def test_fieldaddon_vcard_name(self):
        """ create party, fill fields, check vcard-field 'name'
        """
        Party = Pool().get('party.party')

        Party.create([{
            'name': 'full name',
            'pfafirstname': 'givenname',
            'pfafamilyname': 'family name',
            'pfaadditionalnames': '2nd, 3rd names',
            'pfanickname': 'nickname',
            'pfacompany': 'company',
            'pfadepartment': 'department',
            'pfahonpre': 'Dr.,Prof.',
            'pfahonsuf': 'med.'}])

        p_lst = Party.search([])
        self.assertEqual(len(p_lst), 1)
        r1 = p_lst[0].vcard_field_name()
        self.assertEqual(len(r1.keys()), 6)
        self.assertEqual(r1['fullname'], 'full name')
        self.assertEqual(r1['familyname'], 'family name')
        self.assertEqual(r1['givenname'], 'givenname')
        self.assertEqual(r1['additionalnames'], ['2nd', '3rd names'])
        self.assertEqual(r1['honorprefix'], ['Dr.', 'Prof.'])
        self.assertEqual(r1['honorsuffix'], ['med.'])

    @with_transaction()
    def test_fieldaddon_vcard_nickname(self):
        """ create party, fill fields, check vcard-field 'nickname'
        """
        Party = Pool().get('party.party')

        Party.create([{
            'name': 'full name',
            'pfanickname': 'nickname'}])

        p_lst = Party.search([])
        self.assertEqual(len(p_lst), 1)
        self.assertEqual(p_lst[0].vcard_field_nickname(), 'nickname')

    @with_transaction()
    def test_fieldaddon_vcard_bday(self):
        """ create party, fill fields, check vcard-field 'bday'
        """
        Party = Pool().get('party.party')

        Party.create([{
            'name': 'full name',
            'pfabday': date(2010, 1, 1)}])

        p_lst = Party.search([])
        self.assertEqual(len(p_lst), 1)
        self.assertEqual(p_lst[0].vcard_field_birthday(), date(2010, 1, 1))

# end PartyTestCase


del ModuleTestCase

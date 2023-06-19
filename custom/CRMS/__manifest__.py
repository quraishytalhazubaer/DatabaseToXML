# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'New System',
    'version' : '1.0',
    'summary': 'do fun things here',
    'sequence': 11,
    'description': """ I will be implementing different modules here """,
    'category': '',
    'website': 'https://www.google.com/',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : [],
    'data': [
            'security/ir.model.access.csv',
            'views/crms.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

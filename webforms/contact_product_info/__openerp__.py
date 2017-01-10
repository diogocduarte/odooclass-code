# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Get Product Info Form',
    'version': '1.1',
    'category': 'Web',
    'summary': 'Get Product Info Form',
    'description': """
Form Contact on Product
=======================

    """,
    'website': 'https://diogocduarte.github.io',
    'depends': [
                'website_sale', 'website_form'
    ],
    'data': [
             'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'qweb': [],
}

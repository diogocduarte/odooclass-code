{
    'name': 'Point of Sale Membership',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Point of Sale Membership',
    'description': """
This module Point of Sale Membership Code to POS Screen
""",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_assets_template.xml',
        'views/partner_view.xml',
    ],
    'qweb': [
       "static/src/xml/clientline.xml",
    ],
    'installable': True,
    'auto_install': False,
}

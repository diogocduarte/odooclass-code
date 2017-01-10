{
    'name': 'Barcode Scanner',
    'version': '2.0',
    'category': 'Extra Tools',
    'summary': 'Barcodes Scanning',
    'description': """
This module adds kiosk for barcode scanning and parsing.

""",
    'depends': ['web', 'barcodes', 'stock'],
    'data': [
        'views/web_asset_backend_template.xml',
        'views/barcodebench_view.xml',
    ],
    'qweb': [
        "static/src/xml/bench.xml",
    ],
    'installable': True,
    'auto_install': False,
}

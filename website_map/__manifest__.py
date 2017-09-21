{
    'name': 'Website Map',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Website Geojson Map',
    'description': """
This module adds a map that loads data from Leafletjs using GeoJson
""",
    'depends': ['website', 'base_geolocalize'],
    'data': [
        'views/map_templates.xml',
        #'views/partner_view.xml',
    ],
    'qweb': [
    ],
    'installable': True,
    'auto_install': False,
}

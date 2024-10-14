{
    'name': 'Blueprint Measurement and Estimation Tool',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Upload blueprints, take measurements, and manage cost estimations',
    'description': """
        This module provides a comprehensive tool for users to:
        - Upload and view multi-sheet PDF blueprints
        - Take measurements (area, perimeter, volume)
        - Organize takeoffs
        - Manage equations for cost estimation
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/blueprint_views.xml',
        'views/measurement_views.xml',
        'views/item_views.xml',
        'views/equation_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'blueprint_measurement/static/src/js/pdf_viewer.js',
            'blueprint_measurement/static/src/scss/pdf_viewer.scss',
            'blueprint_measurement/static/src/xml/pdf_viewer.xml',
        ],
    },
    'application': True,
    'installable': True,
}
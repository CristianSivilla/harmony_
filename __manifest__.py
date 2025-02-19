# -*- coding: utf-8 -*-
{
    'name': "Harmony",

    'summary': """
        Haz una playlist de tus temas favoritos""",

    'description': """
        Harmony es un modulo de Odoo en el que tus empleados, pueden crear sus playlist favoritas
    """,

    'author': "Cristian Sivilla",
    'website': "https://www.lasallegracia.cat/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Music',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/artista_view.xml',
        'views/cancion_view.xml',
        'views/lista_view.xml',


       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True
}
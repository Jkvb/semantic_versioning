# -*- coding: utf-8 -*-
{
    'name': "Versionado Semántico",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.odoo.com""",

    'description': """

    """,

    'author': "Juan Carlos Vázquez Beas",
    'website': "",

    # Categories can be used to filter modules in modules listing
    'category': 'proyect',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/semantic_versioning.xml'
    ]
}

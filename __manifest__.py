# -*- coding: utf-8 -*-
{
    'name': "partner_api_key",
    'summary': "Adds field to partner model for use as middleware API key",
    'description': "Adds field to partner model for use as middleware API key",
    'author': "3XE Ltd",
    'website': "https://github.com/3XE/partner_api_key",
    'category': 'Partner',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/partner_api_key_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

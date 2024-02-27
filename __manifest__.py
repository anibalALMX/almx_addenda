# -*- coding: utf-8 -*-
{
    'name': "Addendas Alamex",

    'summary': """
        Este módulo agrega complementos al XML de una factura al timbrarse.""",

    'description': """
        Este módulo agrega un complemento al XML de la factura al timbrarse, este mismo es definido mediante una vista.
    """,

    'author': "Alamex",
    'website': "https://www.alam.mx",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account','l10n_mx_edi'],

    # always loaded
    'data': [
    #Views
        'data/addenda_mavi.xml',
        'views/account_move.xml'
       
    ],  
     'qweb': [
        
         ]
        ,
    'demo': [
    ],
    'application': True,
}

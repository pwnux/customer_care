# -*- coding: utf-8 -*-

{
    'name': 'Agribank Card Service',
    'version': '1.0.0',
    'category': 'Tools',
    'sequence': 1,
    'author': 'Walter',
    'website': 'http://www.agribank.com',
    'summary': 'Agribank Card Service',
    'description': """""",
    'depends': [
        'base',
    ],
    'data': [
        'views/card_service_menu.xml',
        'views/debit_domestic_view.xml',
        'views/debit_foreign_view.xml',
        'views/credit_foreign_view.xml',
        'views/pos_service_view.xml',
        'views/atm_service_view.xml',
        'views/network_transaction_view.xml',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

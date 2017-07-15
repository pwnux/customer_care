# -*- coding: utf-8 -*-

{
    'name': 'Agribank E-Mobile Banking',
    'version': '1.0.0',
    'category': 'Tools',
    'sequence': 1,
    'author': 'Walter',
    'website': 'http://www.agribank.com',
    'summary': 'Agribank E-Mobile Banking',
    'description': """""",
    'depends': [
        'base',
    ],
    'data': [
        'views/e-mobile_banking_menu.xml',
        'views/sms_banking_view.xml',
        'views/vntopup_service_view.xml',
        'views/atransfer_service_view.xml',
        'views/apaybill_service_view.xml',
        'views/emobile_banking_view.xml',
        'views/internet_banking_view.xml',
        'views/agribank_m_plus_view.xml',
        'views/vnmart_view.xml',
        'views/edong_view.xml',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

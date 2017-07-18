# -*- coding: utf-8 -*-

{
    'name': 'Agribank Domestic Money Transfer',
    'version': '1.0.0',
    'category': 'Tools',
    'sequence': 1,
    'author': 'Walter',
    'website': 'http://www.agribank.com',
    'summary': 'Agribank Domestic Money Transfer',
    'description': """""",
    'depends': [
        'base',
    ],
    'data': [
        'views/domestic_money_transfer_menu.xml',
        'views/domestic_money_transfer_view.xml',
        'views/multiple_location_transfer_view.xml',
        'views/domestic_money_transfer_id_view.xml',
        'views/customer_pay_view.xml',
        'views/revenue_service_view.xml',
        'views/revenue_check_service_view.xml',
        'views/reference_question_view.xml',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

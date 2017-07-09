# -*- coding: utf-8 -*-

{
    'name': 'Agribank Q&A',
    'version': '1.0.0',
    'category': 'Tools',
    'sequence': 1,
    'author': 'Walter',
    'website': 'http://www.agribank.com',
    'summary': 'Agribank Question Bank',
    'description': """""",
    'depends': [
        'base',
    ],
    'data': [
        'views/customer_care_menu.xml',
	'views/major_collection_view.xml',
        'views/major_view.xml',
        'views/major_collection_categories_view.xml',
        'views/product_collection_view.xml',
        'security/customer_care_security.xml',
        'security/ir.model.access.csv',
    ],
    'sequence': 1,
    'application': True,
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# -*- coding: utf-8 -*-
{
    'name': 'User Product Groups',
    'version': '0.1.0',
    'author': 'Benlever Pvt Ltd',
    'company': 'Benelever Pvt Ltd',
    'website': 'https://www.benlever.com',
    'maintainer': 'Benlever Pvt Ltd',
    'category': 'Sales/Sales',
    'sequence': 6,
    'summary': 'Allows you to restrict user to specific product groups',
    'description': """
Allows you to restrict user to specific product groups
""",
    'depends': ['product'],
    'data': [
        'views/product_category_groups.xml',
        'views/res_users.xml',
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rules.xml'
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

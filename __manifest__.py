# -*- coding: utf-8 -*-
{
    'name': 'Ipay Payment Acquirer',
    'category': 'Accounting/Payment Acquirers',
    'author': 'Nelson Mongare - SDL',
    'summary': 'Payment Acquirer: Ipay Gateway',
    'version': '1.1',
    'description': """Ipay Payment Acquirer""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_template.xml',
        'data/payment_acquirer_data.xml',
    ],
    'installable': True,
    'application': True,
    'post_init_hook': 'create_missing_journal_for_acquirers',
}

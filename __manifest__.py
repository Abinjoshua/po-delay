# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Delay",
    'version': "1.0",
    'licence': "LGPL-3",
    'author': "Cybrosys",
    'website': "http://www.cybrosys.com",
    'sequence': 1,
    'application': True,
    'depends': ['purchase'],
    'auto_install': True,
    'data': ['data/ir_cron_create_invoice.xml',
             'data/mail_template_data.xml']
}
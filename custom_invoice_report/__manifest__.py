# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Custom Invoice Report",
    'category': "Hidden",
    'summary': 'Customisation of invoice report',

    'description': """
        Customisation of invoice report
    """,

    'depends': ['account','web'],

    'data': [
            'views/page_header_visibility.xml',
            'report/invoice_report.xml',
            'report/invoice_report_template.xml'
    ],
    'installable': True,
    'qweb': [

    ],
}

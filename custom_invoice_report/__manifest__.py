# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Custom Invoice Report",
    'category': "Hidden",
    'summary': 'Customisation of invoice report',

    'description': """
        Customisation of invoice report
    """,
    "license": "LGPL-3",

    'depends': ['account', 'web', 'sale', 'stock'],

    'data': [
        'views/page_header_visibility.xml',
        'report/reports_format_changes.xml',
        'report/invoice_report.xml',
        'report/invoice_report_template.xml',
        'report/header_and_footer_for_reports.xml',
        'report/delivery_slip_report_inherit.xml',
        'report/picking_operations_report.xml',
    ],
    'installable': True,
}

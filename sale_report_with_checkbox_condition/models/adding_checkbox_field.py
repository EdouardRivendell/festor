# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from odoo.tools.translate import html_translate

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    x_studio_verberg_prijs = fields.Boolean(string='Check for unit price visibility', help="If set to true, the quantity will not display in report.")


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    account_line_unit_price_visibility = fields.Boolean(string='Account line unit price visibility checkbox', help="If set to true, the invoice line will not display in report and portal.")

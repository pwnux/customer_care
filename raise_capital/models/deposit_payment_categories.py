# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DepositPaymentCategories(models.Model):
    _name = "deposit.payment.categories"

    name = fields.Char(string="Sản phẩm")
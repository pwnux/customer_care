# -*- coding: utf-8 -*-

from odoo import api, fields, models


class BondFinanceCategories(models.Model):
    _name = "bond.finance.categories"

    name = fields.Char(string="Sản phẩm")
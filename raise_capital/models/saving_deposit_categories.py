# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SavingDepositCategories(models.Model):
    _name = "saving.deposit.categories"

    name = fields.Char(string="Sản phẩm")
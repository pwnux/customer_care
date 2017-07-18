# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MoneyTransferCategories(models.Model):
    _name = "money.transfer.categories"

    name = fields.Char(string="Quy chế")
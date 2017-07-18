# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MoneyExchangeCategories(models.Model):
    _name = "money.exchange.categories"

    name = fields.Char(string="Quy chế")
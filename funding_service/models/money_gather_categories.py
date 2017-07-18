# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MoneyGatherCategories(models.Model):
    _name = "money.gather.categories"

    name = fields.Char(string="Quy chế")
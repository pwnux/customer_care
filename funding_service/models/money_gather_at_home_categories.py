# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MoneyGatherHomeCategories(models.Model):
    _name = "money.gather.home.categories"

    name = fields.Char(string="Quy chế")
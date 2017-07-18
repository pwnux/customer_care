# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DomesticMoneyTransferCategories(models.Model):
    _name = "domestic_money.transfer.categories"

    name = fields.Char(string="Quy chế")
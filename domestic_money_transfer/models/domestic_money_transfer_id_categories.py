# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DomesticMoneyTransferIDCategories(models.Model):
    _name = "domestic_money.transfer_id.categories"

    name = fields.Char(string="Quy chế")
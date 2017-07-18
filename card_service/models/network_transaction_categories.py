# -*- coding: utf-8 -*-

from odoo import api, models, fields


class NetworkTransactionCategories(models.Model):
    _name = "network.transaction.categories"

    name = fields.Char(string="Quy chế")
# -*- coding: utf-8 -*-

from odoo import api, models, fields


class InternetBankingCategories(models.Model):
    _name = "internet.banking.categories"

    name = fields.Char(string="Quy chế")
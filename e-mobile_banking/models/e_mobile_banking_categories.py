# -*- coding: utf-8 -*-

from odoo import api, models, fields


class EMobileBankingCategories(models.Model):
    _name = "emobile.banking.categories"

    name = fields.Char(string="Quy chế")
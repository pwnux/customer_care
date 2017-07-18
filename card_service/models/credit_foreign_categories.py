# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CreditForeignCategories(models.Model):
    _name = "credit.foreign.categories"

    name = fields.Char(string="Quy chế")
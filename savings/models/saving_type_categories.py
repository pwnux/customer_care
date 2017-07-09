# -*- coding: utf-8 -*

from odoo import api, models, fields


class SavingTypeCategories(models.Model):
    _name = "saving.type.categories"

    name = fields.Char(string="Loại tiết kiệm")

# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CreditCardCategories(models.Model):
    _name = "credit.card.categories"

    name = fields.Char(string="Sản phẩm")
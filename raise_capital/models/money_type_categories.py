# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MoneyTypeCategories(models.Model):
    _name = "money.type.categories"

    name = fields.Char(string="Loại tiền gửi")
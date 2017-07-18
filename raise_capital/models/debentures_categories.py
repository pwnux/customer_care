# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DebenturesCategories(models.Model):
    _name = "debentures.categories"

    name = fields.Char(string="Sản phẩm")
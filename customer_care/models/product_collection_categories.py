# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MajorCollectionCategories(models.Model):
    _name = "product.collection.categories"

    name = fields.Char(string="Sản phẩm")
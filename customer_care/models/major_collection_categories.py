# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MajorCollectionCategories(models.Model):
    _name = "major.collection.categories"

    name = fields.Char(string="Quy chế")
    # categories = fields.Char(string="Tra cứu")

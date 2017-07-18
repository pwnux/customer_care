# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PreservationPropertyCategories(models.Model):
    _name = "preservation.property.categories"

    name = fields.Char(string="Quy chế")
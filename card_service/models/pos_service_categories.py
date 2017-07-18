# -*- coding: utf-8 -*-

from odoo import api, models, fields


class POSServiceCategories(models.Model):
    _name = "pos.service.categories"

    name = fields.Char(string="Quy chế")
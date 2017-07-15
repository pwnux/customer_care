# -*- coding: utf-8 -*-

from odoo import api, models, fields


class VnmartServiceCategories(models.Model):
    _name = "vnmart.service.categories"

    name = fields.Char(string="Quy chế")
# -*- coding: utf-8 -*-

from odoo import api, models, fields


class RevenueServiceCategories(models.Model):
    _name = "revenue.service.categories"

    name = fields.Char(string="Quy chế")
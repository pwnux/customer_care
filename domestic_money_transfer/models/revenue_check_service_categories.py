# -*- coding: utf-8 -*-

from odoo import api, models, fields


class RevenueCheckServiceCategories(models.Model):
    _name = "revenue_check.service.categories"

    name = fields.Char(string="Quy chế")
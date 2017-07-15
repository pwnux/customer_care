# -*- coding: utf-8 -*-

from odoo import api, models, fields


class APaybillServiceCategories(models.Model):
    _name = "apaybill.service.categories"

    name = fields.Char(string="Quy chế")
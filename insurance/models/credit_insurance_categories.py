# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CreditInsuranceCategories(models.Model):
    _name = "credit.insurance.categories"

    name = fields.Char(string="Quy chế")
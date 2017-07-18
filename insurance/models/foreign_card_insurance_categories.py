# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ForeignCardInsuranceCategories(models.Model):
    _name = "foreign_card.insurance.categories"

    name = fields.Char(string="Quy chế")
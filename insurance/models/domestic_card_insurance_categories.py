# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DomesticCardInsuranceCategories(models.Model):
    _name = "domestic_card.insurance.categories"

    name = fields.Char(string="Quy chế")
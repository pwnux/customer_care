# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ATMServiceCategories(models.Model):
    _name = "atm.service.categories"

    name = fields.Char(string="Quy chế")
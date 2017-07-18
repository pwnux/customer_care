# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SafetyDepositBoxCategories(models.Model):
    _name = "safety_deposit.box.categories"

    name = fields.Char(string="Quy chế")
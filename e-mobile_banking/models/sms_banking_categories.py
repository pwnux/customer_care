# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SmsBankingCategories(models.Model):
    _name = "sms.banking.categories"

    name = fields.Char(string="Quy chế")
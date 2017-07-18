# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DebitDomesticCategories(models.Model):
    _name = "debit.domestic.categories"

    name = fields.Char(string="Quy chế")
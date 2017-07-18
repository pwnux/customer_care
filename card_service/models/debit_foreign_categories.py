# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DebitForeignCategories(models.Model):
    _name = "debit.foreign.categories"

    name = fields.Char(string="Quy chế")
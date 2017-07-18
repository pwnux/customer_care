# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MultipleLocationTransferCategories(models.Model):
    _name = "multiple_location.transfer.categories"

    name = fields.Char(string="Quy chế")
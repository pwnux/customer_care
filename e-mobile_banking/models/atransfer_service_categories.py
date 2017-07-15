# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ATransferServiceCategories(models.Model):
    _name = "atransfer.service.categories"

    name = fields.Char(string="Quy chế")
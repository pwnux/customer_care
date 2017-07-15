# -*- coding: utf-8 -*-

from odoo import api, models, fields


class EDongServiceCategories(models.Model):
    _name = "edong.service.categories"

    name = fields.Char(string="Quy chế")
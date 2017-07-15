# -*- coding: utf-8 -*-

from odoo import api, models, fields


class AgribankMPlusCategories(models.Model):
    _name = "mplus.service.categories"

    name = fields.Char(string="Quy chế")
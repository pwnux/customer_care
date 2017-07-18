# -*- coding: utf-8 -*-

from odoo import api, models, fields


class CustomerPayCategories(models.Model):
    _name = "customer.pay.categories"

    name = fields.Char(string="Quy chế")
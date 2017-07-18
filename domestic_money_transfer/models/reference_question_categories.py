# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ReferenceRevenueQuestionCategories(models.Model):
    _name = "reference_revenue.question.categories"

    name = fields.Char(string="Sản phẩm")
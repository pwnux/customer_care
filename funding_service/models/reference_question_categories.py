# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ReferenceFundingQuestionCategories(models.Model):
    _name = "reference_funding.question.categories"

    name = fields.Char(string="Sản phẩm")
# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ReferenceInsuranceQuestionCategories(models.Model):
    _name = "reference_insurance.question.categories"

    name = fields.Char(string="Sản phẩm")
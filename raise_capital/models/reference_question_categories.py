# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ReferenceQuestionCategories(models.Model):
    _name = "reference.question.categories"

    name = fields.Char(string="Sản phẩm")
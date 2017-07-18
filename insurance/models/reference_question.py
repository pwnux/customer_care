# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ReferenceInsuranceQuestion(models.Model):
    _name = "reference_insurance.question"

    name = fields.Many2one("reference_insurance.question.categories", required=True)
    key_search = fields.Char(string="Tiểu mục 1")
    key_search_2 = fields.Char(string="Tiểu mục 2")
    question = fields.Text(string="Câu hỏi")
    content = fields.Text(string="Nội dung trả lời")
    document_reference = fields.Char(string="Dẫn chiếu văn bản")

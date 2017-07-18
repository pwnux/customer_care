# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ReferenceRevenueQuestion(models.Model):
    _name = "reference_revenue.question"

    name = fields.Many2one("reference_revenue.question.categories", required=True)
    key_search = fields.Char(string="Tiểu mục 1")
    key_search_2 = fields.Char(string="Tiểu mục 2")
    question = fields.Text(string="Câu hỏi")
    content = fields.Text(string="Nội dung trả lời")
    document_reference = fields.Char(string="Dẫn chiếu văn bản")

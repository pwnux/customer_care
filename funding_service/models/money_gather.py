# -*- coding: utf-8 -*-

from odoo import api, models, fields


class MoneyGather(models.Model):
    _name = "money.gather"

    name = fields.Many2one("money.gather.categories", required=True)
    key_search = fields.Char(string="Tiểu mục 1")
    key_search_2 = fields.Char(string="Tiểu mục 2")
    question = fields.Text(string="Câu hỏi")
    content = fields.Text(string="Nội dung trả lời")
    document_reference = fields.Char(string="Dẫn chiếu văn bản")
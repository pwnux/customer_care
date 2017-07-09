# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MajorCollection(models.Model):
    _name = "major.collection"

    name = fields.Many2one("major.collection.categories", required=True)
    key_search = fields.Char(string="Tra cứu")
    question = fields.Text(string="Câu hỏi")
    content = fields.Text(string="Nội dung trả lời")
    document_reference = fields.Char(string="Dẫn chiếu văn bản")


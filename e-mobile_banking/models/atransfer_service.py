# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ATransferService(models.Model):
    _name = "atransfer.service"

    name = fields.Many2one("atransfer.service.categories", required=True)
    key_search = fields.Char(string="Tiểu mục 1")
    key_search_2 = fields.Char(string="Tiểu mục 2")
    question = fields.Text(string="Câu hỏi")
    content = fields.Text(string="Nội dung trả lời")
    document_reference = fields.Char(string="Dẫn chiếu văn bản")
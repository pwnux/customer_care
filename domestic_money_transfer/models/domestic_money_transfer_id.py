# -*- coding: utf-8 -*-

from odoo import api, models, fields


class DomesticMoneyTransferID(models.Model):
    _name = "domestic_money.transfer_id"

    name = fields.Many2one("domestic_money.transfer_id.categories", required=True)
    key_search = fields.Char(string="Tiểu mục 1")
    key_search_2 = fields.Char(string="Tiểu mục 2")
    question = fields.Text(string="Câu hỏi")
    content = fields.Text(string="Nội dung trả lời")
    document_reference = fields.Char(string="Dẫn chiếu văn bản")
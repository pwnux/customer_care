# -*- coding: utf-8 -*-

from odoo import api, fields, models


class MoneyType(models.Model):
    _name = "money.type"

    name = fields.Many2one("money.type.categories", required=True)
    key_search = fields.Char(string="Dạng tiền gửi")
    product_properties = fields.Text(string="Đặc tính sản phẩm")
    product_procedure = fields.Text(string="Thủ tục")
    product_object = fields.Text(string="Đối tượng áp dụng")

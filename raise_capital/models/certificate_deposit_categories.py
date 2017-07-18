# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CertificateDepositCategories(models.Model):
    _name = "certificate.deposit.categories"

    name = fields.Char(string="Sản phẩm")
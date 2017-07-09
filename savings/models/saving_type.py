# -*- coding: utf-8 -*

from odoo import api, models, fields


class SavingType(models.Model):
    _name = "saving.type"

    name = fields.Many2one("saving.type.categories", required=True)

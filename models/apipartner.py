# -*- coding: utf-8 -*-

from odoo import fields, models

class ApiPartner(models.Model):
    _inherit = 'res.partner'
    api_key = fields.Char(string='API Key', readonly=False, index=True, required=False)

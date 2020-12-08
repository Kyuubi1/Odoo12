# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWCaloHistory(models.Model):
    _name = 'lw.calo.history'
    _description = 'User Calo History per day'

    partner_id = fields.Many2one('res.partner', string="Customer", ondelete='cascade', required=True)
    calo_input = fields.Float(string="Calo Input")
    calo_ouput = fields.Float(string="Calo Input")

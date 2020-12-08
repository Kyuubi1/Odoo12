# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWWeightlossAreaPartner(models.Model):
    _name = 'lw.weightloss.area.partner'
    _description = 'User Weightloss Area'

    partner_id = fields.Many2one('res.partner', string="Customer", ondelete='cascade', required=True)
    weightloss_area_id = fields.Many2one('lw.weightloss.area', string="WeightLoss Area", ondelete='cascade',
                                         required=True)
    active = fields.Boolean(string="Active", required=1, default=True)

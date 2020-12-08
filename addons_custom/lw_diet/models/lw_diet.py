# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWDiet(models.Model):
    _name = 'lw.diet'
    _description = 'Diet for user'

    partner_id = fields.Many2one('res.partner', string="Partner", required=1)
    lw_week_id = fields.Many2one('lw.week', string="Day of Week", required=1)
    lw_menu_id = fields.Many2one('lw.menu', string="Menu", required=1)
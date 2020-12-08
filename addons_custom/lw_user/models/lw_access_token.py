# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWAccessToken(models.Model):
    _name = 'lw.access.token'
    _description = 'User Access Token'

    partner_id = fields.Many2one('res.partner', string="Customer", ondelete='cascade', required=True)
    token = fields.Char(string="Registration Token", required=1)
    device_id = fields.Char(string="Device ID", required=1)

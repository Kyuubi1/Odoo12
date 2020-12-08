# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFCMToken(models.Model):
    _name = 'lw.fcm.token'
    _description = 'User FCM Token'

    partner_id = fields.Many2one('res.partner', string="Customer", ondelete='cascade', required=True)
    token = fields.Char(string="Registration Token", required=1)
    device_id = fields.Char(string="Device ID", required=1)

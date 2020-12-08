# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWDietToday(models.Model):
    _name = 'lw.diet.today'
    _description = 'Diet for user Today'

    diet_id = fields.Many2one('lw.diet', string="Diet")
    status = fields.Boolean(string="Status")

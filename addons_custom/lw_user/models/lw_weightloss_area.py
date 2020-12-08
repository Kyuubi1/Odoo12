# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWWeightlossArea(models.Model):
    _name = 'lw.weightloss.area'
    _description = 'User Weightloss Area: Master Data'

    name = fields.Char(string='Name', required=1)

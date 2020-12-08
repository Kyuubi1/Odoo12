# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWWeightlossArea(models.Model):
    _name = 'lw.weightloss.area'
    _description = 'Weight loss Area'

    name = fields.Char(string="Name", required=1)

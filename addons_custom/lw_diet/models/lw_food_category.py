# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFoodCategory(models.Model):
    _name = 'lw.food.category'
    _description = 'Food Category'

    food_id = fields.Many2many('lw.food',string="Food", required=1)
    category_code = fields.Char(string="Code", required=1)
    partner_id = fields.Many2one('res.partner', string="Customer")

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFoodMenuPartner(models.Model):
    _name = 'lw.food.star'
    _description = 'Food Star of Partner'

    food_id = fields.Many2one('lw.food',string="Food", required=1)
    star = fields.Integer(string="Star")
    res_partner_id = fields.Many2one('res.partner', string="Customer", required=1)
    like_flag = fields.Integer(string="Like Flag")

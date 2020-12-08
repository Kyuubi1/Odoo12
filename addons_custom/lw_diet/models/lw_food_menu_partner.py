# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFoodMenuPartner(models.Model):
    _name = 'lw.food.menu.partner'
    _description = 'Menu Food For Partner'

    food_id = fields.Many2many('lw.food',string="Food", required=1)
    menu_code = fields.Char(string="Code", required=1)
    partner_id = fields.Many2one('res.partner', string="Customer", required=1)
    lw_menu_id = fields.Many2one('lw.menu', string="Menu")
    day_of_week = fields.Char(string="Day of Week", required=1)

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFoodMenuPartnerToday(models.Model):
    _name = 'lw.food.menu.partner.today'
    _description = 'Menu Food For Partner Today'

    status = fields.Char(string="Status")
    lw_food_menu_partner_id = fields.Many2one('lw.food.menu.partner', string="Menu Food For Partner")

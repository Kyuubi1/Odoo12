# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWMenu(models.Model):
    _name = 'lw.menu'
    _description = 'Food'

    name = fields.Char(string="Name", required=1)
    total_kcal = fields.Float(string="Total Kcal", required=1, default=0)
    food_ids = fields.Many2many('lw.food', string="Food", ondelete='cascade')
    code = fields.Char(string="Menu Code")

    def name_get(self):
        res = []
        for item in self:
            res.append((item.id, item.name))
        return res

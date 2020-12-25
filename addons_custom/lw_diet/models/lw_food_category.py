# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFoodCategory(models.Model):
    _name = 'lw.food.category'
    _description = 'Food Category'

    food_id = fields.Integer(string="Food", required=1)
    category_code = fields.Char(string="Code", required=1)
    partner_id = fields.Many2one('res.partner', string="Customer")

    @api.multi
    def name_get(self):
        res = []
        for category in self:
            category_name = self.env['lw.category'].sudo().search([('code', '=', category.category_code)])[0]
            res.append((category.id, category_name.name))

        return res


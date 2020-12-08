# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerUer(models.Model):
    _inherit = 'res.partner'

    x_lw_password = fields.Char(string="Password", required=1, default='123')
    x_lw_height = fields.Float(string="Height", required=1, default=0)
    x_lw_weight = fields.Float(string="Weight", required=1, default=0)
    x_lw_bmi = fields.Float(string="BMI", required=1, compute="_compute_bmi")
    x_lw_dob = fields.Datetime(string="BirthDay")
    x_lw_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender", required=1, default='female')
    x_lw_expected_weight = fields.Float(string="Expected Weight")
    x_lw_steps_per_day = fields.Float(string="Steps Per Day")
    x_lw_meals_per_day = fields.Float(string="Meals Per Day", default=3)
    x_lw_power = fields.Selection([
        ('week', 'Weak'),
        ('quite_weak', 'Quite Weak'),
        ('normal', 'Normal'),
        ('strong', 'Strong'),
        ('very_strong', 'Very Strong')
    ], string="Power", required=1, default='normal')

    def _compute_bmi(self):
        for item in self:
            try:
                item.x_lw_bmi = item.x_lw_weight / pow(item.x_lw_height, 2)
            except Exception:
                item.x_lw_bmi = 0

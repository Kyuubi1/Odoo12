# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExercisePartnerWeek(models.Model):
    _name = 'lw.ex.partner.week'
    _description = 'Exercise for Partner in a week'

    lw_week_id = fields.Many2one('lw.week', string="Day of Week", required=1)
    lw_exercise_partner_id = fields.Many2one('lw.exercise.partner', string="Exercise in Week", required=1)
    active = fields.Boolean(string="Active", default=True, required=1)
    finish_flag = fields.Boolean(string="Finish Flag")
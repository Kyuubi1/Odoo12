# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExercisePartner(models.Model):
    _name = 'lw.exercise.partner'
    _description = 'Exercise for specific Partner'

    exercise_id = fields.Many2one("lw.exercise", string="Exercise", required=1)
    partner_id = fields.Many2one("res.partner", string="Partner", required=1)
    progress = fields.Float(string="Progress (%)", default=0, required=1)
    emotion = fields.Selection([
        ('over','Over'),
        ('fine','Fine'),
        ('comfortable','Comfortable'),
        ('easy','Easy'),
    ], string="Emotion", help="Emotion after practicing exercise")
    finish_flag = fields.Boolean(string="Finish Flag")
    finish_date = fields.Char(String="Finish Date")

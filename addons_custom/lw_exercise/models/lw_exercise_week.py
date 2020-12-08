# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExerciseWeek(models.Model):
    _name = 'lw.exercise.week'
    _description = 'Exercise\'s Video'

    exercise_id = fields.Many2one("lw.exercise", string="Exercise", required=1)
    day_of_week = fields.Char(string="Day of Week")

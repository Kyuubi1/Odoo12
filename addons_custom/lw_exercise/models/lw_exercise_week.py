# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExerciseWeek(models.Model):
    _name = 'lw.exercise.week'
    _description = 'Exercise\'s Video'
    _rec_name = 'day_of_week'

    exercise_id = fields.Many2one("lw.exercise", string="Exercise", required=1)
    week_id = fields.Many2one('lw.week', string="Day of Week")
    day_of_week = fields.Char(string="Day of Week")


    @api.model
    def create(self, val):
        exercise_id = val.get('exercise_id')
        week_id = val.get('week_id')

        week = self.env['lw.week'].sudo().search([('id', '=', week_id)])
        res = super(LWExerciseWeek, self).create([{
            'exercise_id': exercise_id,
            'day_of_week': week.day_of_week,
            'week_id': week_id
        }])
        return res


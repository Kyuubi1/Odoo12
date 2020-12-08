# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExerciseVideo(models.Model):
    _name = 'lw.exercise.video'
    _description = 'Exercise\'s Video'

    exercise_id = fields.Many2one("lw.exercise", string="Exercise", required=1)
    partner_id = fields.Many2one("res.partner", string="Customer")
    video_id = fields.Many2one("lw.video", string="Video")

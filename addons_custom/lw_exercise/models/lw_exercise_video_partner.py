# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExerciseVideoPartner(models.Model):
    _name = 'lw.exercise.video.partner'
    _description = 'Exercise\'s Video for Partner'

    exercise_video_id = fields.Many2one("lw.exercise.video", string="Exercise Video")
    partner_id = fields.Many2one("res.partner", string="Customer")
    finish_flag = fields.Boolean(string="Finish Flag")
    finish_date = fields.Date(string="Finish Date")
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWExercise(models.Model):
    _name = 'lw.exercise'
    _description = 'Exercise'

    name = fields.Char(string="Name", required=1)
    duration = fields.Integer(string="Duration", help='Duration for 1 exercise in second', required=1)
    description = fields.Text(string="Description", help='Show how to practice this exercise', required=1)
    kcal = fields.Float(string="Kcal", help="Calories consumed after completing the exercise")
    min_weight = fields.Float(string="Min Weight", help="Min Weight that can fit exercises")
    max_weight = fields.Float(string="Max Weight", help="Max Weight that can fit exercises")
    min_height = fields.Float(string="Min Height", help="Min Height that can fit exercises")
    max_height = fields.Float(string="Max Height", help="Max Height that can fit exercises")
    fixed = fields.Boolean(string="Fixed", help="Type of exercise", required=1, default=True)
    weightloss_area_ids = fields.Many2many("lw.weightloss.area", string="WeightLoss Area")
    image = fields.Char(string="Image Url")
    video = fields.Char(string="Video Url")

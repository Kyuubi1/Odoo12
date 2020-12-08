# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWFood(models.Model):
    _name = 'lw.food'
    _description = 'Food'

    name = fields.Char(string="Name", required=1)
    calo = fields.Float(string="Calo", required=1, default=0)
    description = fields.Text(string="Description", required=1, help="Show how to cook that and image of this food")
    total_like = fields.Integer(string="Total Likes", required=1, default=0)
    recommend_level = fields.Selection([
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    ], string="Recommend Level")
    prepare_time = fields.Float(string="Prepare Time", required=1, help="Time for preparing in minutes")
    cooking_time = fields.Float(string="Cooking Time", required=1, help="Time for cooking in minutes")
    category_id = fields.Many2one(string="Category", requried=1)
    image = fields.Char(string="Image Url")

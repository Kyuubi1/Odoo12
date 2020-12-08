# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWVideo(models.Model):
    _name = 'lw.video'
    _description = 'Exercise\'s Video'

    video_name = fields.Char(string="Video Name", required=1)
    image = fields.Char(string="Image")
    url = fields.Char(string="URL")
    description = fields.Char(string="Description", required=1)
    calo = fields.Float(string="Calo", required=1)
    category_ids = fields.Many2many(comodel_name='lw.category', column1='lw_video_id', column2='lw_category_id', string='Category')

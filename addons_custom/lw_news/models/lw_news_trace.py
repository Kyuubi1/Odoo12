# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWNewsTrace(models.Model):
    _name = 'lw.news.trace'
    _description = 'News/ Article Trace'

    partner_id = fields.Many2one("res.partner", string="Partner", required=1)
    news_id = fields.Many2one("lw.news", string="News", required=1)
    read_flg = fields.Boolean(string="Read Flag", required=1, default=False)
    like_flg = fields.Boolean(string="Like Flag", required=1, default=False)

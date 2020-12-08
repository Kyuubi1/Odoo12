# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LWWeek(models.Model):
    _name = 'lw.week'
    _description = 'Day of Week'

    day_of_week = fields.Char(string="Day of Week")

    @api.multi
    def name_get(self):
        res = []
        for item in self:
            res.append((item.id, ("%s") % (item.day_of_week)))
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=8):
        args = args or []
        domain_name = [('day_of_week', 'ilike', name)]
        recs = self.search(domain_name + args, limit=limit)
        return recs.name_get()

# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re


class LWNews(models.Model):
    _name = 'lw.news'
    _description = 'News/ Article'
    _rec_name = 'title'

    title = fields.Char(string="Title", required=1)
    description = fields.Text(string="Description")
    total_like = fields.Integer(string="Total Likes", required=1, default=0)
    total_views = fields.Integer(string="Total Views", required=1, default=0)
    image_url_list = fields.Char(string="Image URL list")

    @api.multi
    def name_get(self):
        res = []
        for item in self:
            res.append((item.id, ("%s") % (item.title)))
        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=8):
        args = args or []
        domain_name = [('title', 'ilike', name)]
        recs = self.search(domain_name + args, limit=limit)
        return recs.name_get()

    @api.model
    def create(self, vals):
        res = super(LWNews, self).create(vals)

        # update description with image
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        res.description = res.description.replace('src="/web/image', f'src="{base_url}/web/image')
        reg = r'src=".*"'
        r = re.search(reg,res.description)
        print(r)
        # get 3 or less image in html
        return res

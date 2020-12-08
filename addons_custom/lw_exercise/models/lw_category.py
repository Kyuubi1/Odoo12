from odoo import models, fields, api


class LWCategory(models.Model):
    _name = 'lw.category'
    _description = 'Category of Video'

    name = fields.Char(string="Name", required=1)
    code = fields.Char(string="Code", required=1)
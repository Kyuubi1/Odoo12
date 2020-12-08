# -*- coding: utf-8 -*-
from odoo import http

# class LwDiet(http.Controller):
#     @http.route('/lw_diet/lw_diet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lw_diet/lw_diet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lw_diet.listing', {
#             'root': '/lw_diet/lw_diet',
#             'objects': http.request.env['lw_diet.lw_diet'].search([]),
#         })

#     @http.route('/lw_diet/lw_diet/objects/<model("lw_diet.lw_diet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lw_diet.object', {
#             'object': obj
#         })
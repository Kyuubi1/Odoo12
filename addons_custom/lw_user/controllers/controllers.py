# -*- coding: utf-8 -*-
from odoo import http

# class LwUser(http.Controller):
#     @http.route('/lw_user/lw_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lw_user/lw_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lw_user.listing', {
#             'root': '/lw_user/lw_user',
#             'objects': http.request.env['lw_user.lw_user'].search([]),
#         })

#     @http.route('/lw_user/lw_user/objects/<model("lw_user.lw_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lw_user.object', {
#             'object': obj
#         })
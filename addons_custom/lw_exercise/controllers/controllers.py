# -*- coding: utf-8 -*-
from odoo import http

# class LwExercise(http.Controller):
#     @http.route('/lw_exercise/lw_exercise/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lw_exercise/lw_exercise/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lw_exercise.listing', {
#             'root': '/lw_exercise/lw_exercise',
#             'objects': http.request.env['lw_exercise.lw_exercise'].search([]),
#         })

#     @http.route('/lw_exercise/lw_exercise/objects/<model("lw_exercise.lw_exercise"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lw_exercise.object', {
#             'object': obj
#         })
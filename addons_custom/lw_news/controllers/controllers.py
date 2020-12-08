# -*- coding: utf-8 -*-
from odoo import http

# class LwNews(http.Controller):
#     @http.route('/lw_news/lw_news/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lw_news/lw_news/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lw_news.listing', {
#             'root': '/lw_news/lw_news',
#             'objects': http.request.env['lw_news.lw_news'].search([]),
#         })

#     @http.route('/lw_news/lw_news/objects/<model("lw_news.lw_news"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lw_news.object', {
#             'object': obj
#         })
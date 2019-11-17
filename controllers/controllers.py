# -*- coding: utf-8 -*-
from odoo import http

# class ExamYourName(http.Controller):
#     @http.route('/exam__your__name/exam__your__name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exam__your__name/exam__your__name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exam__your__name.listing', {
#             'root': '/exam__your__name/exam__your__name',
#             'objects': http.request.env['exam__your__name.exam__your__name'].search([]),
#         })

#     @http.route('/exam__your__name/exam__your__name/objects/<model("exam__your__name.exam__your__name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exam__your__name.object', {
#             'object': obj
#         })
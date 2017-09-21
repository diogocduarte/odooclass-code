# -*- coding: utf-8 -*-
from odoo import http

class IrastorageAccount(http.Controller):
    @http.route('/irastorage_account/irastorage_account/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/irastorage_account/irastorage_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('irastorage_account.listing', {
#             'root': '/irastorage_account/irastorage_account',
#             'objects': http.request.env['irastorage_account.irastorage_account'].search([]),
#         })

#     @http.route('/irastorage_account/irastorage_account/objects/<model("irastorage_account.irastorage_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('irastorage_account.object', {
#             'object': obj
#         })
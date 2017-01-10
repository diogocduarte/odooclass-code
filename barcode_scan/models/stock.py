# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def product_scan(self, barcode):
        """ Receive a barcode scanned from the Bench Mode and get information about the product
        """
        product = self.search([('barcode', '=', barcode)], limit=1)
        msg = {'warning': _('Barcode: %(barcode)s - Product: %(name)s - Price: %(price)s') %
                          {'barcode': barcode, 'name': product.name, 'price': product.list_price}}
        return product and msg or \
               {'warning': _('There is no product corresponding to barcode %(barcode)s') % {'barcode': barcode}}

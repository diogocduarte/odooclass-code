# -*- coding: utf-8 -*-

from odoo import models, fields, api


class irastorage_account(models.Model):
    _name = 'irastorage_account.irastorage_account'

    @api.depends('expecting_inventories.total_qty')
    def _compute_total(self):
        total = 0
        for x in self.expecting_inventories:
            total += x.qty

        x.update({
            'total_qty': total,
        })


    name = fields.Char('First Name', required=True)
    lastname = fields.Char('Last Name', required=True)
    accountnumber = fields.Char('Account Number', required=True)
    date_opened = fields.Datetime('Date Opened', required=True)
    accounttype = fields.Selection(selection=[('Commingled', 'Commingled'), ('Segregated', 'Segregated')])
    expecting_inventories = fields.One2many('expectinginventory', 'account_id', string='Expecting Inventories')
    total_qty = fields.Float(compute='_compute_total')

class product_description(models.Model):
    _name = 'product_description.product_description'

    name = fields.Char('Product Name', required=True)
    type = fields.Char('Type', required=True)


class expectinginventory(models.Model):
    _name = "expectinginventory"
    _description = "Expecting Inventory"

    @api.multi
    @api.depends('order_line.qty')
    def _total_deliver(self):
        for order in self:
            total = 0
            for line in order.order_line:
                total += line.qty

            order.update({
                'total_qty': total,
            })

    account_id = fields.Many2one('irastorage_account.irastorage_account', string='Account Reference', required=True, ondelete='cascade')
    name = fields.Char(string='Metal Name')
    order_line = fields.One2many('inventoryorders', 'order_id', string='Order Lines')
    total_qty = fields.Float(string='Total Expected', compute='_total_deliver')
    total_recieved_qty = fields.Float(string='Total Recieved Quantity')
    products = fields.Many2one('product_description.product_description')
    commodity = fields.Selection(
        selection=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Palladium', 'Palladium')])
    qty = fields.Float(string='To be delivered')
    is_pending = fields.Boolean()
    date_opened = fields.Datetime('Date Opened', required=True)
    date_received = fields.Datetime('Date Received')

class inventoryorders(models.Model):
    _name = "inventoryorders"
    _description = "Expecting Inventory Orders"

    order_id = fields.Many2one('expectinginventory', string='Order Reference', required=True, ondelete='cascade')
    name = fields.Char(string='Product Name')
    commodity = fields.Selection(
        selection=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Platinum', 'Platinum'), ('Palladium', 'Palladium')],
        required=True)
    products = fields.Many2one('product_description.product_description', required=True)
    qty = fields.Float(string='To be delivered')
    received_qty = fields.Float(string='Total Delivered')
    possible_issue = fields.Selection(
        selection=[('Not enough product', 'Not enough product'), ('Too much product', 'Too much product')])
    possible_solution = fields.Selection(
        selection=[('Not enough product', 'Not enough product'), ('Too much product', 'Too much product')])

class pending_accounts(models.Model):
    _name = 'pending.accounts'
    _description = 'Pending Accounts'

    name = fields.Char()
    firstname = fields.Char()
    lastname = fields.Char()
    expected_qty = fields.Float()
    recieved_qty = fields.Float()
    possible_reason = fields.Selection(selection=[('Not enough product', 'Not enough product'), ('Too much product','Too much product'),('Incorrect Product','Incorrect Product'),('Issue with receiving the shipment ','Issue with receiving the shipment')])
    possible_solution = fields.Selection(selection=[('Wait for product to arrive', 'Wait for product to arrive'),('Adjust Inventory','Adjust Inventory'),('Generate Shipping Label','Generate Shipping Label'),('Wait for correct product','Wait for correct product'),('Return Prodcut','Return Product')])
    notes = fields.Html(string="Notes", required=True)

class possible_reasons(models.Model):
    _name = 'possible.reasons'

    name = fields.Char()

class possible_solutions(models.Model):
    _name = 'possible.solutions'

    name = fields.Char()

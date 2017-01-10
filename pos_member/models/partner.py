# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    membership_code = fields.Char('Membership')

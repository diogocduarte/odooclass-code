# -*- coding: utf-8 -*-
from openerp import models, SUPERUSER_ID


class Lead(models.Model):
    _inherit = 'crm.lead'

    def website_form_input_filter(self, request, values):
        values.update({'priority': '3'})
        return values

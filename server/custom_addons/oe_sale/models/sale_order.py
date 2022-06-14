# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pickup_point_id = fields.Many2one(
        'pickup.point', string='Pickup Point',
        required=1, ondelete='restrict',
    )

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['pickup_point_id'] = self.pickup_point_id.id
        return invoice_vals


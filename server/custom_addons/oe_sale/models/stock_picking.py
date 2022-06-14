# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    pickup_point_id = fields.Many2one(
        'pickup.point', string='Pickup Point', ondelete='restrict',
        readonly=False, store=True, compute='_compute_pickup_point_id',
    )

    @api.depends('sale_id')
    def _compute_pickup_point_id(self):
        for picking in self:
            so_id = picking.sale_id
            if so_id:
                picking.pickup_point_id = so_id.pickup_point_id.id
            else:
                picking.pickup_point_id = False

    @api.model
    def oe_print_invoices(self):
        invoice_ids = []
        so_id = self.mapped('sale_id')
        if so_id:
            for invoice_id in so_id.invoice_ids:
                if invoice_id.state in ('draft', 'posted'):
                    invoice_ids.append(invoice_id.id)

        if not invoice_ids:
            raise UserError(_('Invoice report not found!'))
        return self.env.ref('account.account_invoices').report_action(invoice_ids)

# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    pickup_point_id = fields.Many2one('pickup.point', string='Pickup Point', ondelete='restrict')

    def get_delivery_date(self):
        if self.invoice_line_ids:
            so_id = self.invoice_line_ids.mapped('sale_line_ids.order_id')
            if so_id and so_id.commitment_date:
                return so_id.commitment_date
        return False

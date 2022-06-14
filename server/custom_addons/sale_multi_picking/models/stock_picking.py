# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class StockMoveInherit(models.Model):
    _inherit = 'stock.move'

    @api.constrains('picking_id')
    def check_picking_id_from_move(self):
        for rec in self:
            if rec.picking_id:
                if rec.fresh_type == 'fresh':
                    # sequence = self.env['ir.sequence'].next_by_code('fresh.picking')
                    sequence = '%s/F' % self.origin
                    rec.picking_id.sudo().write({
                        'is_fresh': True,
                        'name': sequence,
                    })
                if rec.fresh_type == 'none_fresh':
                    # sequence = self.env['ir.sequence'].next_by_code('nonfresh.picking')
                    sequence = '%s/NF' % self.origin
                    rec.picking_id.sudo().write({
                        'is_non_fresh': True,
                        'name': sequence,
                    })
                if not rec.fresh_type:
                    sequence = '%s' % self.origin
                    rec.picking_id.sudo().write({
                        'name': sequence,
                    })

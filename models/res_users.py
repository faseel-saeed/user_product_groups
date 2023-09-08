# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.addons.bus.models.bus_presence import AWAY_TIMER
from odoo.addons.bus.models.bus_presence import DISCONNECTION_TIMER


class ResUsers(models.Model):
    _inherit = "res.users"

    product_category_group = fields.Many2one('product.category.groups',
                                         string="Product Category Group",
                                         help="Product categories user has has access to",
                                         check_company=True,
                                         required=False)

    @api.model
    def create(self, vals):
        self.clear_caches()
        return super(ResUsers, self).create(vals)

    def write(self, vals):
        self.clear_caches()
        return super(ResUsers, self).write(vals)

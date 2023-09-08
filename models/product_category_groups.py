# -*- coding: utf-8 -*-

import logging
import re
from operator import itemgetter

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class ProductCategoryGroups(models.Model):
    _name = "product.category.groups"
    _description = "Product Category Groups"
    _order = "name"

    name = fields.Char(required=True)
    company_id = fields.Many2one('res.company', string='Company', required=True,
                                 default=lambda self: self.env.company.id)
    product_categories = fields.Many2many(
        'product.category',
        string='Product Categories')

    @api.model
    def create(self, vals):
        self.clear_caches()
        return super(ProductCategoryGroups, self).create(vals)

    def write(self, vals):
        self.clear_caches()
        return super(ProductCategoryGroups, self).write(vals)

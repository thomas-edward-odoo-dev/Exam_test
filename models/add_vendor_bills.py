from odoo import models, fields, api


class add_vendor_bills(models.Model):
    _inherit = 'purchase.order'
    products = fields.Many2one("product.template", string='Products')

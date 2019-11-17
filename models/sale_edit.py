from odoo import models, fields, api


class sale_edit(models.Model):

    _inherit = 'sale.order'
    qunt = fields.Integer( string='Qunt')
    deg = fields.Integer( string='Deg')


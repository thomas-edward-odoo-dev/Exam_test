from odoo import models, fields, api


class inventory_edit(models.Model):
    _inherit = 'stock.move.line'

    s_barcode = fields.Char(string='Exam', related='product_id.barcode')

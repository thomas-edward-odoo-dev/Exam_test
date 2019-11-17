from odoo import models, fields, api


class project_edit(models.Model):
    _inherit = 'project.task'
    exam = fields.Char( string='Exam')
    name_partner = fields.Many2one('res.partner'," Name Partner ")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender", default="male")

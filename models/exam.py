from odoo import models, fields, api
from odoo.exceptions import except_orm, Warning
from datetime import datetime

STATE = [('created', 'Created'),
         ('solved', 'Solved'),
         ('finished', 'Finished'),
         ]
STATE_TYPE =[('draft', 'Draft'),
         ('finished', 'Finished'),
         ]
class exam_exam(models.Model):
    _name= 'exam.exam'

    name = fields.Many2one("hr.employee", "employee")
    exam_ids = fields.Many2many("exam.type", "exam_rel", "exam_id", "type_id",
                                   "Exam type Information")
    # exam_ids = fields.One2many("exam.type", "exam_id", "Exam Type")
    exam_num = fields.Char(string="serial of exam_type",related="exam_ids.serial")
    exam_length = fields.Integer("name length",readonly=True,compute='_get_len_name')
    start_date = fields.Datetime("Start Date", readonly=True ,default=datetime.now())
    end_date = fields.Datetime("End Date" , required=True)
    marks = fields.Float("Marks" , readonly=True)
    state = fields.Selection(STATE, "Status", readonly=True, default="created")


    @api.one
    @api.depends('name')
    def _get_len_name(self):
        if self.name :
            self.exam_length = len(self.name.name)

    @api.constrains('end_date')
    def _check_release_date(self):
        for record in self:
            if record.end_date and record.end_date < record.start_date:
                raise models.ValidationError('Release date must be in the future')

        # register first year

    @api.multi
    def solve(self):
        if self.state == 'created':
            self.state = 'solved'

    @api.multi
    def back(self):
        if self.state == 'solved':
            self.state = 'created'

    @api.multi
    def finish(self):
        if self.state == 'solved':
            self.state = 'finished'

    @api.multi
    def solve_again(self):
        if self.state == 'finished':
            self.state = 'solved'


##############################################################
class exam_type(models.Model):
    _name= 'exam.type'
    exam_id = fields.Many2one("exam.exam", "Exam", ondelete="cascade")
    name = fields.Char("Name",required=True)
    serial= fields.Char("serial",required=True)
    state = fields.Selection(STATE_TYPE, "Status", readonly=True, default="draft")


    @api.multi
    def finished(self):
        if self.state == 'draft':
            self.state = 'finished'

    @api.multi
    def draft(self):
        if self.state == 'finished':
            self.state = 'draft'

    @api.model
    def default_get(self, fields):
        res = super(exam_type, self).default_get(fields)
        next_seq = self.env['ir.sequence'].get('exam.serial.sequence')
        res.update({'serial': next_seq})
        return res
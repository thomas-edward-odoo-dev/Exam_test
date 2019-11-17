from odoo import models, fields, api


STATE = [('excellent', 'Excellent'),
         ('vgood', 'Vgood'),
         ('good', 'Good'),
         ('fair', 'Fair'),
         ('poor', 'Poor'),
         ]

class student_evaluation(models.Model):
    _name= 'student.evaluation'

    name = fields.Many2one("hr.employee", "employee")
    student_grade = fields.Integer("student grade",)
    final_grade = fields.Integer("Final grade")
    student_percentage = fields.Integer("student percentage % ", readonly=True,compute='_student_per')
    state = fields.Selection(STATE, "Status", readonly=True,compute='_get_degree')

    @api.one
    @api.depends('student_grade','final_grade')
    def _student_per(self):
        if self.student_grade and self.final_grade:
            self.student_percentage = (self.student_grade/self.final_grade) * 100
    @api.one
    @api.depends('student_percentage')
    def _get_degree(self):
        if self.student_percentage :
            if self.student_percentage < 50 :
                self.state = 'poor'
            elif self.student_percentage > 50 and self.student_percentage < 65 :
                self.state = 'fair'
            elif self.student_percentage > 65 and self.student_percentage < 75 :
                self.state = 'good'
            elif self.student_percentage > 75 and self.student_percentage < 85 :
                self.state = 'vgood'
            elif self.student_percentage > 85 :
                self.state = 'excellent'

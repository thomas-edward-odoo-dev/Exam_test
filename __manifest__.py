# -*- coding: utf-8 -*-
{
    'name': "Exam_Your_Name",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Thomas Edward",
    'website': "http://www.thomasedward.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'project', 'purchase', 'stock', 'sale_management'],

    # always loaded
    'data': [
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/exam.xml',
        'views/exam_type.xml',
        'views/student_evaluation.xml',
        'views/add_vendor_bills.xml',
        'views/project_edit.xml',
        'views/inventory_edit.xml',
        'views/sale_edit.xml',
        'report/student_report.xml',
        'report/exam_info.xml',
        'views/report_saleorder.xml',
        'views/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
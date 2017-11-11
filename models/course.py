# -*- coding: utf-8 -*-

from odoo import fields, models, _

class Course(models.Model):
    _name = 'course.course'
    _description = "Course"
    name = fields.Char('Course Name', required=True, translate=True)
    
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Course name already exists !"),
    ]

from odoo import models, fields, api

class Equation(models.Model):
    _name = 'blueprint.equation'
    _description = 'Equation'

    name = fields.Char(string='Name', required=True)
    equation = fields.Text(string='Equation', required=True)
    variable_ids = fields.One2many('blueprint.equation.variable', 'equation_id', string='Variables')

class EquationVariable(models.Model):
    _name = 'blueprint.equation.variable'
    _description = 'Equation Variable'

    name = fields.Char(string='Variable Name', required=True)
    equation_id = fields.Many2one('blueprint.equation', string='Equation')
    measurement_type = fields.Selection([
        ('area', 'Area'),
        ('perimeter', 'Perimeter'),
        ('volume', 'Volume')
    ], string='Measurement Type')
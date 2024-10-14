from odoo import models, fields, api

class Measurement(models.Model):
    _name = 'blueprint.measurement'
    _description = 'Measurement'

    name = fields.Char(string='Name', required=True)
    blueprint_id = fields.Many2one('blueprint.blueprint', string='Blueprint', required=True)
    measurement_type = fields.Selection([
        ('area', 'Area'),
        ('perimeter', 'Perimeter'),
        ('volume', 'Volume')
    ], string='Measurement Type', required=True)
    value = fields.Float(string='Value')
    unit = fields.Char(string='Unit')
    coordinates = fields.Text(string='Coordinates')  # Store as JSON
    is_highlighted = fields.Boolean(string='Highlighted', default=False)
    item_ids = fields.Many2many('blueprint.item', string='Related Items')
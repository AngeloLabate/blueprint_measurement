from odoo import models, fields, api
import base64
import PyPDF2
import json

class Blueprint(models.Model):
    _name = 'blueprint.blueprint'
    _description = 'Blueprint'

    name = fields.Char(string='Name', required=True)
    pdf_file = fields.Binary(string='PDF File', attachment=True, required=True)
    scale_factor = fields.Float(string='Scale Factor', default=1.0)
    reference_dimension = fields.Float(string='Reference Dimension')
    measurement_ids = fields.One2many('blueprint.measurement', 'blueprint_id', string='Measurements')
    page_count = fields.Integer(string='Page Count', compute='_compute_page_count', store=True)
    pdf_data = fields.Text(string='PDF Data', compute='_compute_pdf_data', store=True)

    @api.depends('pdf_file')
    def _compute_page_count(self):
        for record in self:
            if record.pdf_file:
                pdf_content = base64.b64decode(record.pdf_file)
                pdf_reader = PyPDF2.PdfReader(pdf_content)
                record.page_count = len(pdf_reader.pages)
            else:
                record.page_count = 0

    @api.depends('pdf_file')
    def _compute_pdf_data(self):
        for record in self:
            if record.pdf_file:
                pdf_content = base64.b64decode(record.pdf_file)
                pdf_reader = PyPDF2.PdfReader(pdf_content)
                pdf_data = []
                for page in pdf_reader.pages:
                    pdf_data.append({
                        'width': page.mediabox.width,
                        'height': page.mediabox.height,
                    })
                record.pdf_data = json.dumps(pdf_data)
            else:
                record.pdf_data = '[]'
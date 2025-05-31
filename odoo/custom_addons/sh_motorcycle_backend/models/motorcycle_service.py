from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class MotorcycleService(models.Model):
    _name = 'motorcycle.service'
    _description = 'Servicio de Motocicleta'
    _rec_name = 'name'

    name = fields.Char('Número de Servicio', required=True, copy=False, readonly=True, 
                      default=lambda self: self.env['ir.sequence'].next_by_code('motorcycle.service.sequence') or 'Nuevo')
    
    motorcycle_ids = fields.Many2many(
        'motorcycle.motorcycle',
        'motorcycle_service_rel',  # misma tabla relacional
        'service_id', 'motorcycle_id',  # campos invertidos
        string='Motocicletas',
        required=True
    )
    description = fields.Text(string='Descripción')
    labor_description = fields.Text(string='Descripción del Trabajo')

    currency_id = fields.Many2one('res.currency', string='Moneda', 
        default=lambda self: self.env.company.currency_id)

    service_line_ids = fields.One2many('motorcycle.service.line', 'service_id', string='Líneas del Servicio')

    total_parts_cost = fields.Monetary(string='Costo de Repuestos', currency_field='currency_id', compute='_compute_totals', store=True, default=0.0)
    total_service_cost = fields.Monetary(string='Costo Total', currency_field='currency_id', compute='_compute_totals', store=True, default=0.0)

    step_ids = fields.One2many('motorcycle.service.step', 'service_id', string='Pasos del servicio')

    @api.depends('service_line_ids.subtotal')
    def _compute_totals(self):
        for service in self:
            total = sum(line.subtotal for line in service.service_line_ids if line.display_type == 'line')
            service.total_parts_cost = total
            service.total_service_cost = total

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        args = args or []
        if name:
            keywords = re.split(r'\s+', name.strip())
            domain_parts = [[
                '|', '|',
                ('name', 'ilike', kw),
                ('description', 'ilike', kw),
                ('motorcycle_ids.name', 'ilike', kw)
            ] for kw in keywords]

            domain = args + domain_parts[0]
            for part in domain_parts[1:]:
                domain = expression.AND([domain, part])
            records = self.search(domain, limit=limit)
        else:
            records = self.search(args, limit=limit)
        return records.name_get()



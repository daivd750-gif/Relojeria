from odoo import models, fields
from datetime import timedelta

class Reloj(models.Model):
    _name = 'relojeria.reloj'
    _description = 'Clase de reloj'

    calidad = fields.Selection([
        ('basica', 'Basica'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ], string='Calidad', required=True, help='Calidad del reloj', default='media')

    tamaño = fields.Float(string='Tamaño', required=True, help='Tamaño del reloj')
    materiales = fields.Char(string='Materiales', required=True, help='Materiales utilizados')
    peso = fields.Float(string='Peso', help='Peso del reloj')

    tipo_Reloj = fields.Selection([
        ('analogico', 'Analogico'),
        ('digital', 'Digital'),
        ('inteligente', 'Inteligente (Smartwatch)'),
    ], string='Tipo de reloj', required=True, help='Tipo de reloj')

    resistencia_Agua = fields.Selection([
        ('no', 'Sin resistencia al agua'),
        ('30m', '30 metros'),
        ('50m', '50 metros'),
        ('100m', '100 metros'),
        ('200m', '200 metros'),
    ], string='Resistencia al agua', help='Resistencia al agua del reloj', default='no')

    resistencia_GolpesArañazos = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ], string='Resistencia a golpes y arañazos', help='Resistencia del reloj a golpes y arañazos', default='media')

    durabilidad = fields.Integer(string='Durabilidad', help='Durabilidad del reloj')
    personalizacion = fields.Text(string='Personalizacion', help='Opciones de personalizacion del reloj')
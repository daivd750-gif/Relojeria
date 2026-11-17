from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Proveedores(models.Model):
    _name = 'relojeria.proveedores'
    _description = 'Proveedores de relojes inteligentes'
    _rec_name = 'nombre_proveedor'

    nombre_proveedor = fields.Selection([
        ('xiaomi', 'Xiaomi'),
        ('huawei', 'Huawei'),
        ('samsung', 'Samsung'),
        ('mediamarkt', 'MediaMarkt'),
        ('amazfit', 'Amazfit'),
        ('apple', 'Apple'),
    ], string='Proveedor', required=True)

    precio_compra = fields.Float(string='Precio', required=True)
    telefono = fields.Integer(string='Telefono', required=True)
    direccion = fields.Char(string='Direccion', required=True)

    metodo_pago = fields.Selection([
    ('transferencia', 'Transferencia'),
    ('tarjeta', 'Tarjeta'),
    ], string='Metodo de pago', default='transferencia')

    plazo_entrega = fields.Selection([
    ('24h', '24 horas'),
    ('3d', '3 dias'),
    ('1s', '1 semana'),
    ('2s', '2 semanas'),
    ], string='Plazo de entrega')

    fecha_alta = fields.Date(string='Fecha de alta', default=fields.Date.today)
    ultima_entrega = fields.Datetime(string='Ultima entrega')
    activo = fields.Boolean(string='Activo', default=True)
    notas = fields.Text(string='Notas')
    foto_adjunta = fields.Binary(string='Foto adjunta', attachment=True)
    pedidos = fields.Integer(string='Pedidos', default=0)
    total_relojes = fields.Integer(string='Total de relojes', compute='_compute_total_relojes')

    #un proveedor puede tener muchos relojes
    reloj_ids = fields.One2many('relojeria.reloj', 'proveedor_id', string='Relojes', help='Relojes del proveedor')
    consulta_ids = fields.One2many('relojeria.servicio_cliente', 'proveedor_id', string='Consultas')

    #api depends, cuenta cuantos relojes tiene el proveedor
    @api.depends('reloj_ids')
    def _compute_total_relojes(self):
        for proveedor in self:
            proveedor.total_relojes = len(proveedor.reloj_ids)

    #api constrains, valida que el precio de compra sea mayor que 0
    @api.constrains('precio_compra')
    def _check_precio_compra(self):
        for proveedor in self:
            if proveedor.precio_compra <= 0:
                raise ValidationError('El precio de compra debe ser mayor que 0')
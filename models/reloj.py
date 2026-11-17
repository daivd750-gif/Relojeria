from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Reloj(models.Model):
    _name = 'relojeria.reloj'
    _description = 'Clase de reloj'

    calidad = fields.Selection([
        ('basica', 'Basica'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ], string='Calidad', required=True, help='Calidad del reloj', default='media')

    name = fields.Char(string='Modelo', required=True, help='Nombre o modelo del reloj')
    tamano = fields.Float(string='Tamano', required=True, help='Tamano del reloj')
    materiales = fields.Char(string='Materiales', required=True, help='Materiales utilizados')
    peso = fields.Float(string='Peso', help='Peso del reloj')

    tipo_Reloj = fields.Selection([
        ('analogico', 'Analogico'),
        ('digital', 'Digital'),
        ('inteligente', 'Inteligente'),
    ], string='Tipo de reloj', required=True, help='Tipo de reloj')

    resistencia_Agua = fields.Selection([
        ('no', 'Sin resistencia al agua'),
        ('30m', '30 metros'),
        ('50m', '50 metros'),
        ('100m', '100 metros'),
    ], string='Resistencia al agua', help='Resistencia al agua del reloj', default='no')

    resistencia_GolpesAranazos = fields.Selection([
        ('baja', 'Baja'),
        ('media', 'Media'),
        ('alta', 'Alta'),
    ], string='Resistencia a golpes y aranazos', help='Resistencia del reloj a golpes y aranazos', default='media')

    durabilidad = fields.Integer(string='Durabilidad', help='Durabilidad del reloj')
    personalizacion = fields.Text(string='Personalizacion', help='Opciones de personalizacion del reloj')
    fecha_fabricacion = fields.Date(string='Fecha de fabricacion')
    fecha_ingreso = fields.Datetime(string='Fecha de ingreso', default=fields.Datetime.now)
    disponible = fields.Boolean(string='Disponible', default=True)
    precio_venta = fields.Float(string='Precio de venta')
    foto_adjunta = fields.Binary(string='Foto adjunta', attachment=True)
    margen_beneficio = fields.Float(string='Margen de beneficio', compute='_compute_margen_beneficio')

    #many2one cada reloj tiene un proveedor
    proveedor_id = fields.Many2one('relojeria.proveedores', string='Proveedor', required=True, help='Proveedor del reloj')
    #many2many cada reloj puede tener varias consultas y cada consulta puede tener varios relojes
    consulta_ids = fields.Many2many('relojeria.servicio_cliente', string='Consultas')
    #many2many cada reloj puede tener varios relojes similares y cada reloj puede ser similar a varios relojes
    similar_ids = fields.Many2many('relojeria.reloj', 'relojeria_reloj_similar_rel', 'reloj_id', 'similar_id', string='Relojes similares')
    #store true, el nombre del proveedor se almacena en la base de datos para poder buscarlo y ordenarlo
    nombre_proveedor = fields.Selection(related='proveedor_id.nombre_proveedor', string='Nombre del proveedor', store=True)

    #api constrains, valida que el tamaño sea mayor que 0
    @api.constrains('tamano')
    def _check_tamano(self):
        for reloj in self:
            if reloj.tamano <= 0:
                raise ValidationError('El tamano del reloj debe ser mayor que 0')

    #api constrains, valida que el precio de venta no sea negativo
    @api.constrains('precio_venta')
    def _check_precio_venta(self):
        for reloj in self:
            if reloj.precio_venta < 0:
                raise ValidationError('El precio de venta no puede ser negativo')

    #api depends, calcula el margen de beneficio en porcentaje, si el precio de compra es 0 con el else se queda en 0
    @api.depends('precio_venta', 'proveedor_id.precio_compra')
    def _compute_margen_beneficio(self):
        for reloj in self:
            precio_compra = reloj.proveedor_id.precio_compra
            if precio_compra > 0:
                reloj.margen_beneficio = ((reloj.precio_venta - precio_compra)/ precio_compra) * 100
            else:
                reloj.margen_beneficio = 0
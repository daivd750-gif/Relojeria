from odoo import models, fields

class Proveedores(models.Model):
    _name = 'relojeria.proveedores'
    _description = 'Proveedores de relojes inteligentes'

    nombre_proveedor = fields.Selection([
        ('xiaomi', 'Xiaomi'),
        ('huawei', 'Huawei'),
        ('samsung', 'Samsung'),
        ('mediamarkt', 'MediaMarkt'),
        ('amazfit', 'Amazfit'),
        ('apple', 'Apple'),
    ], string='Proveedor', required=True)

    precio_compra = fields.Float(string='Precio', required=True)
    telefono = fields.Char(string='Telefono', required=True)
    direccion = fields.Char(string='Direccion', required=True)
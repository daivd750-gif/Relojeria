from odoo import models, fields

class ServicioCliente(models.Model):
    _name = 'relojeria.servicio_cliente'
    _description = 'Servicio al cliente'

    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email', required=True)
    preguntas = fields.Text(string='Preguntas', required=True)
    peticiones = fields.Text(string='Mensaje', required=True)
    devoluciones = fields.Text(string='Devoluciones', required=True)
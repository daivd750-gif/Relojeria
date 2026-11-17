from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ServicioCliente(models.Model):
    _name = 'relojeria.servicio_cliente'
    _description = 'Servicio al cliente'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    preguntas = fields.Text(string='Preguntas')
    peticiones = fields.Text(string='Mensaje')
    devoluciones = fields.Text(string='Devoluciones')

    tipo_consulta = fields.Selection([
    ('pregunta', 'Pregunta'),
    ('peticion', 'Peticion'),
    ('devolucion', 'Devolucion'),
    ('reclamacion', 'Reclamacion'),
    ], string='Tipo de consulta', required=True, default='pregunta')

    prioridad = fields.Selection([
    ('baja', 'Baja'),
    ('media', 'Media'),
    ('alta', 'Alta'),
    ], string='Prioridad', default='media')

    contacto = fields.Selection([
    ('email', 'Email'),
    ('telefono', 'Teléfono'),
    ('tienda', 'En tienda'),
    ('web', 'Web'),
    ], string='Canal de contacto')

    fecha_consulta = fields.Datetime(string='Fecha de la consulta', default=fields.Datetime.now)
    fecha_limite = fields.Date(string='Fecha limite de respuesta')
    foto_adjunta = fields.Binary(string='Foto adjunta', attachment=True)
    resuelto = fields.Boolean(string='Resuelto', default=False)

    #many2many cada consulta puede tener muchos relojes
    reloj_ids = fields.Many2many('relojeria.reloj', string='Relojes', help='Relojes de la consulta')
    #many2one cada consulta puede tener un proveedor implicado
    proveedor_id = fields.Many2one('relojeria.proveedores', string='Proveedor implicado')
    #many2one cada consulta puede tener una consulta origen
    consulta_origen_id = fields.Many2one('relojeria.servicio_cliente', string='Consulta anterior')
    #one2many cada consulta puede tener muchos seguimientos
    seguimiento_ids = fields.One2many('relojeria.servicio_cliente', 'consulta_origen_id', string='Seguimientos')

    #api constrains, valida que la fecha limite de respuesta sea mayor a la fecha de la consulta
    @api.constrains('fecha_consulta', 'fecha_limite')
    def _check_fecha_limite(self):
        for consulta in self:
            if consulta.fecha_limite and consulta.fecha_consulta:
                if consulta.fecha_limite < consulta.fecha_consulta.date():
                    raise ValidationError('La fecha limite no puede ser anterior a la fecha de la consulta')

    #api constrains, valida que el email tenga arroba
    @api.constrains('email')
    def _check_email(self):
        for consulta in self:
            if consulta.email and '@' not in consulta.email:
                raise ValidationError('El email no es valido')
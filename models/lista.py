import re
from odoo import models, fields, api, exceptions

class Lista(models.Model):
    _name = 'lista'
    _description = 'Modelo de lista'

    id_lista = fields.Integer(string='Id_Lista', required=True, index=True, help='Id de la lista')
    nom = fields.Char(string='Nom', help='Nombre de la lista')
    lista = fields.Many2one('hr.employee', string='Empleado de la lista', required=True, domain="[('active','=',True)]")
    canciones = fields.One2many('cancion', 'id_lista', string='Canciones')

    @api.constrains('nom')
    def _check_nom(self):
        for record in self:
            if record.nom and not re.match(r'^[a-zA-Z]+$', record.nom):
                raise exceptions.ValidationError('El nombre de la lista solo puede contener letras')
    
    @api.constrains('id_lista')
    def _validar_id_cancion(self):
        for record in self:
            if not record.id_cancion.isdigit():
                raise exceptions.ValidationError("El id de la canción ha de ser numérico")


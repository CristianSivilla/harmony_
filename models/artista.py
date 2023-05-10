from odoo import models, fields, api, exceptions

class Artista(models.Model):
    _name = 'artista'
    _description = 'Modelo de artista'

    id_artista = fields.Integer(string='Id_Artista', help='Id del artista')
    nombre = fields.Char(string='Nombre', required=True, help='Nombre del artista')
    nacionalidad = fields.Char(string='Nacionalidad', help='Nacionalidad del artista')
    

    @api.constrains('nombre')
    def _check_nombre(self):
        for record in self:
            if not record.nombre.isalpha():
                raise exceptions.ValidationError("El nombre del artista, ha de ser un texto.")

    @api.constrains('nacionalidad')
    def _check_nacionalidad(self):
        for record in self:
            if not record.nacionalidad.isalpha():
                raise exceptions.ValidationError("La nacionalidad del artista , ha de ser un texto.")


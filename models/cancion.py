from odoo import models, fields, api, exceptions

class Cancion(models.Model):
    _name = 'cancion'
    _description = 'Modelo de canción'

    id_cancion = fields.Integer(string='Id_Cancion', help='Id de la canción')
    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la canción')
    descripcion = fields.Text(string='Descripción', help='Descripción de la canción')
    id_artista = fields.Many2one('artista', string='Artista', required=True, help='Artista de la canción')
    id_lista = fields.Many2one('lista', string='Lista', required=True, help='Lista de la canción')

    @api.constrains('nombre')
    def _validar_nombre(self):
        for record in self:
            if not record.nombre.isalpha():
                raise exceptions.ValidationError("El nombre de la canción ha de ser un texto")

    @api.constrains('descripcion')
    def _validar_descripcion(self):
        for record in self:
            if not record.descripcion.isalpha():
                raise exceptions.ValidationError("La descripción de la canción ha de ser un texto")


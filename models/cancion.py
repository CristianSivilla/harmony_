from odoo import models, fields

class Cancion(models.Model):
    _name = 'cancion'
    _description = 'Modelo de canción'

    id_cancion = fields.Integer(string='Id_Cancion', required=True, index=True, help='Id de la canción')
    nombre = fields.Char(string='Nombre', required=True, help='Nombre de la canción')
    descripcion = fields.Text(string='Descripción', help='Descripción de la canción')
    id_artista = fields.Many2one('artista', string='Artista', required=True, help='Artista de la canción')
    id_lista = fields.Many2one('lista', string='Lista', required=True, help='Lista de la canción')

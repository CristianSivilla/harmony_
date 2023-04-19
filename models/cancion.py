from odoo import models, fields

class Cancion(models.Model):
    _name = 'cancion'
    _description = 'Modelo de canción'

    id_cancion = fields.Integer(string='Id_Cancion', required=True, index=True, help='Id de la canción')
    id_artista = fields.Many2one('artista', string='Id_Artista', required=True, help='Artista de la canción')
    id_lista = fields.Many2one('lista', string='Id_Lista', required=True, help='Lista de la canción')
